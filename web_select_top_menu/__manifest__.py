# pylint: disable=missing-docstring
# Copyright 2021 Nicolas JEUDY
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Web Select Top Menu',
    'summary': """
        Select top menus per user to create simple backend entry
        By default top menus are menu that have no parent_id""",
    'version': '12.0.1.0.2',
    'license': 'AGPL-3',
    'author': 'Nicolas JEUDY'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/web',
    'depends': [
        'web',
        'base',
    ],
    'data': [
        'views/res_users.xml',
    ],
    'demo': [
    ],
    'installable': True,
}
