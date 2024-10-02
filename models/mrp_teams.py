from odoo import fields, models


class ManufacturingTeams(models.Model):
    _name = "manufacturing.teams"
    _description = "Manufacturing Team Management"
    _rec_name = "team_name"

    member_ids = fields.One2many("manufacture.team.member", "team_id", string="Team Members")
    team_name = fields.Char(string="Manufacturing Team")
    team_leader = fields.Many2one("res.partner", string="Team Leader")
    company_name = fields.Many2one("res.company", string="Company")



















