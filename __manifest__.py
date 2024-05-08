# -*- coding: utf-8 -*-
{
    'name': "DTI interconnexion Zeendoc",

    'summary': """
        mise à jour du referenciel fournisseurs de Odoo sur le logiciel Zeendoc.
    """,

    'description': """
        mise à jour du referenciel fournisseurs de Odoo sur le logiciel Zeendoc.
    """,

    'author': "Systhen-DTI",
    'website': "https://www.systhen.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '1.0.0',

    # notre module est basé sur le modele res.partner qui se trouve dans le module contact
    'depends': ['contact'],

    'data': ['views/fournisseur_view.xml'],

    'application': True,
    'auto_install': True,
}
