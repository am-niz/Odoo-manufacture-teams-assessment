from odoo import fields, models


class ManufacturingTeams(models.Model):
    _name = "manufacturing.teams"
    _description = "Manufacturing Team Management"
    _rec_name = "manufacturing_team_name"

    team_member_ids = fields.One2many("manufacture.team.member", "manufacture_team_id", string="Team Members")
    manufacturing_team_name = fields.Char(string="Manufacturing Team")
    manufacturing_team_leader = fields.Many2one("res.partner", string="Team Leader")
    manufacturing_company_name = fields.Many2one("res.company", string="Company")

