# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeAttendanceLog(http.Controller):
#     @http.route('/employee_attendance_log/employee_attendance_log', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_attendance_log/employee_attendance_log/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_attendance_log.listing', {
#             'root': '/employee_attendance_log/employee_attendance_log',
#             'objects': http.request.env['employee_attendance_log.employee_attendance_log'].search([]),
#         })

#     @http.route('/employee_attendance_log/employee_attendance_log/objects/<model("employee_attendance_log.employee_attendance_log"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_attendance_log.object', {
#             'object': obj
#         })
