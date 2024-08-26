from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SalesKPI(models.Model):
    _name = 'sales.kpi'
    _description = 'Sales KPIs'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='KPI Name', required=True, track_visibility='onchange')
    description = fields.Text(string='Description')
    target_value = fields.Float(string='Target Value', required=True, track_visibility='onchange')
    actual_value = fields.Float(string='Actual Value', compute='_compute_actual_value', store=True, default=0.0,track_visibility='onchange')
    percentage_achieved = fields.Float(string='Achievement (%)', compute='_compute_percentage_achieved', store=True, default=0.0)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    partner_id = fields.Many2one('res.partner', string='Related Partner', track_visibility='onchange')

    @api.depends('target_value', 'actual_value')
    def _compute_percentage_achieved(self):
        for record in self:
            if record.target_value:
                record.percentage_achieved = (record.actual_value / record.target_value) * 100
            else:
                record.percentage_achieved = 0

    @api.depends('start_date', 'end_date')
    def _compute_actual_value(self):
        for record in self:
            # Example placeholder logic
            # Here, you can include any business logic to determine the actual value
            # For demonstration, we assume actual_value is a random number between 0 and target_value
            if record.start_date and record.end_date:
                # Example logic for demonstration
                record.actual_value = min(record.target_value, 0.5 * record.target_value)
            else:
                record.actual_value = 0.0

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date > record.end_date:
                raise ValidationError("Start Date must be before End Date.")
