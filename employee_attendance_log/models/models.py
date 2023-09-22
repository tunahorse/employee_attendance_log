# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class employee_attendance_log(models.Model):
#     _name = 'employee_attendance_log.employee_attendance_log'
#     _description = 'employee_attendance_log.employee_attendance_log'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
