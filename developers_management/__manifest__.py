{
    'name': 'developers_management',
    'version': '1.0',
    'summary': 'Viktors test',
    'author': 'Viktor Kruts',
    'description': 'test task odoo',
    'category': 'test',
    'website': 'https://www.youtube.com/',
    'licence': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/developer.xml',
        'views/company.xml',
    ],
    'test': [
        'tests/test_developer_model.py',
    ],
}
