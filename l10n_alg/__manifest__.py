# -*- coding: utf-8 -*-

{
    'name': "Comptabilité - Algérie",

    'category': 'Localization',

    'summary': """ Ce module gére le plan comptable pour l'Algérie sur odoo 12 """,

    "contributors": [
        "1 <Djamel Eddine YAGOUB>",
        "2 <Nassim REFES>",
        "3 <Kamel BENCHEHIDA>",
    ],

    'sequence': 1,

    'version': '1.0',

    "license": "LGPL-3",

    'author': 'Elosys',

    'website': 'http://igpro-online.net/',

    "price": 0.0,

    "currency": 'EUR',

    'depends': ['base','account'],

    'data': [
        'data/account_group.xml',
        'data/l10n_alg_chart_data.xml',
        'data/account_account_template_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_data.xml',
        'data/account_tax_data.xml',
        'data/account_fiscal_position_template_data.xml',
        'data/account_chart_template_configure_data.xml',

        'views/account_group.xml',
        'views/account_account.xml',
    ],
    'images': [
                'images/main_screenshot.png',
            ],

    'post_init_hook': '_preserve_tag_on_taxes',

    # les proprités d'installation #
    'installable': True,
    'auto_install': False,
    "application":False,
}
