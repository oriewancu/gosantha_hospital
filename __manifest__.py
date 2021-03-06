{
    'name': 'Rumah Sakit',
    'version': '12.0.1.0.0',
    'description': 'Modul untuk Manajemen Rumah Sakit',
    'summary': 'Modul untuk Manajemen Rumah Sakit',
    'author': 'Gosantha',
    'website': 'http://www.gosantha.com',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'depends': ['mail', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'data/data.xml',
        'data/mail_template.xml',
        'wizards/create_appointment.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
    ],
    'demo': [],
    'auto_install': False,
    'application': True,
    'installable': True,
}