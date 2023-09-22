from odoo import models, fields, api

class AttendanceLog(models.Model):
    _name = 'attendance.log'
    _description = 'Employee Attendance Log'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    check_in = fields.Datetime(string='Check In', required=True)
    check_out = fields.Datetime(string='Check Out')
    hours_worked = fields.Float(string='Hours Worked', compute='_compute_hours_worked')

    @api.depends('check_in', 'check_out')
    def _compute_hours_worked(self):
        for record in self:
            if record.check_in and record.check_out:
                delta = record.check_out - record.check_in
                record.hours_worked = delta.total_seconds() / 3600
            else:
                record.hours_worked = 0.0


