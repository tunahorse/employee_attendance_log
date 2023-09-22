{
    'name': 'Employee Attendance Log',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Log employee attendance and calculate hours worked.',
    'author': 'Fabian Anguiano',
    'license': 'AGPL-3',
    'website': 'https://www.fabiananguiano.com',
    'depends': ['base', 'hr'],
    'data': [
        'views/attendance_log_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
