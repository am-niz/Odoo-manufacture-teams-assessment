# -*- coding: utf-8 -*-
{
    'name': "manufacturing_team_management",

    'summary': "Can set manufacture team with team members",

    'description': """
Can set manufacture team with team members
    """,

    'author': "Amzsys",
    'website': "http://www.amzsys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'mrp',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_teams_views.xml',
        'views/mrp_production_views.xml',
        'report/report_mrp_team.xml',

    ],
    "application": True,
    "sequence": -105,

}

