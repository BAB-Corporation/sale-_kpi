{
    'name': 'Sales KPI Module',
    'version': '1.0',
    'depends': ['base', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_kpi_views.xml',
    ],
    'installable': True,
    'application': True,
}
