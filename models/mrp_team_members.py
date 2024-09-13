from odoo import fields, models


class ManufacturingTeamMembers(models.Model):
    _name = "manufacture.team.member"
    _description = "Manufacturing Team Members"

    manufacture_team_id = fields.Many2one("manufacturing.teams", string="Manufacture Team")
    team_member_name = fields.Many2one("res.partner", string="Members")

