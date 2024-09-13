from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    manufacturing_team = fields.Many2one("manufacturing.teams", string="Manufacture Team")
