from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_field = fields.Char(string="Champ personnalisé", store=True)
    project_reference = fields.Char(string="Référence projet", store=True)
