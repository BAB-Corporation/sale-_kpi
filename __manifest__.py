{
    'name': 'Sales KPI Module',
    'version': '1.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_kpi_views.xml',
                'data/sales_kpi_data.xml',

    ],
    'installable': True,
    'application': True,
}
