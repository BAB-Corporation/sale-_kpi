from odoo import models, fields, api

class SalesKPI(models.Model):
    _name = 'sales.kpi'
    _description = 'Sales KPIs'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='KPI Name', required=True, track_visibility='onchange'
    tag_ids = fields.Many2many('some.model', string='Tags')  # 
    description = fields.Text(string='Description')
    target_value = fields.Float(string='Target Value', required=True, track_visibility='onchange')
    actual_value = fields.Float(string='Actual Value', compute='_compute_actual_value', store=True)
    percentage_achieved = fields.Float(string='Achievement (%)', compute='_compute_percentage_achieved', store=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    lead_id = fields.Many2one('crm.lead', string='Related Lead', track_visibility='onchange')
    partner_id = fields.Many2one('res.partner', string='Related Partner', track_visibility='onchange')

    @api.depends('target_value', 'actual_value')
    def _compute_percentage_achieved(self):
        for record in self:
            if record.target_value:
                record.percentage_achieved = (record.actual_value / record.target_value) * 100
            else:
                record.percentage_achieved = 0

    @api.depends('lead_id')
    def _compute_actual_value(self):
        for record in self:
            record.actual_value = record.lead_id.planned_revenue
