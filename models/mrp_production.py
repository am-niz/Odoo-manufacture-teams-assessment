from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    mrp_team_id = fields.Many2one("manufacturing.teams", string="Manufacture Team")
