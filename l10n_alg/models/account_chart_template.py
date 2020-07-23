# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

class AccountChartTemplate(models.Model):
    _inherit = 'account.chart.template'

    @api.one
    def try_loading_for_current_company(self):
        res = super(AccountChartTemplate, self).try_loading_for_current_company()
        if self.id == self.env.ref('l10n_alg.l10n_alg_pcg_chart_template').id:
            self.load_for_current_company()
        return res

    def load_for_current_company(self):
        # lié chaque compte au group parent
        for aa_id in self.env['account.account'].search([]):
            chapitre_niveau_4_code = aa_id.code[0:4]
            chapitre_niveau_3_code = aa_id.code[0:3]
            chapitre_niveau_2_code = aa_id.code[0:2]
            code_par_niveau = [chapitre_niveau_4_code, chapitre_niveau_3_code, chapitre_niveau_2_code]
            code_index = 0

            while code_index < len(code_par_niveau):
                ag_id = self.env['account.group'].search([('code_prefix', '=', code_par_niveau[code_index])], limit=1)
                if ag_id:
                    aa_id.write({'group_id': ag_id.id})
                    break
                code_index += 1
