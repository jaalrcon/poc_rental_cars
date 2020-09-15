# -*- coding: utf-8 -*-

from odoo import models, fields

class CarsCars(models.Model):
        _name = 'cars.cars'
        
        code = fields.Char(string = 'Code', required = True)
        model = fields.Char(string = 'Model')
        year = fields.Integer(string = 'Year')
        photo = fields.Binary(string='Image')
        contact = fields.Char(string = 'Contact')
        status = fields.Selection([('rented', 'Rented'), ('norented', 'No Rented')], stringa = 'Status')
        details = fields.Text(string = 'Details')
