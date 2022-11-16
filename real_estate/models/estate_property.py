from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "properties"
    
    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()