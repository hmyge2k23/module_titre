{
    'name': 'Personnalisation des Devis',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Ajout d\'un titre pour les devis',
    'author': 'Ton Nom',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
        'views/report_saleorder_document.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
