# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Mohamed Mtloob
#    Copyright (C) Mohamed Mtloob
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################



from odoo import fields, models, api, _

class PartnerAddress(models.Model):
    _name = 'partner.address'

    partner_id = fields.Many2one('res.partner', u'Partner')
    name = fields.Char('Address', compute='_get_address')
    zip = fields.Char(u'Zip')
    street = fields.Char(u'Street')
    street2 = fields.Char(u'Street2')
    area = fields.Char(u'Area')
    group = fields.Char(u'Group')
    building = fields.Char(u'Building')
    flat = fields.Char(u'Flat')
    country_id = fields.Many2one('res.country', u'Country',
                                 default=lambda self: self.env.user.company_id.country_id.id or False)
    state_id = fields.Many2one('res.country.state', u'State')
    city_id = fields.Many2one('res.state.city', u'City')
    type = fields.Selection([('w', u'Work'), ('r', u'Residential')], default='w', string=u'Type')
    active = fields.Boolean('Active', default=True)
    is_main = fields.Boolean('Is Main ?')
    phone = fields.Char('Phone')
    mobile = fields.Char('Mobile')
    email = fields.Char('Email')
    website = fields.Char('Website')
    @api.one
    @api.depends('area','group','building','flat','zip', 'street', 'street2', 'state_id', 'city_id')
    def _get_address(self):
        address = ''
        if self.area:
            address = address +' A: '+ self.area
        if self.group:
            address = address +', G: '+ self.group
        if self.building:
            address = address +', B: '+ self.building
        if self.flat:
            address = address +', F: '+ self.flat
        if self.street:
            address = address + ', ' + self.street
        if self.street2:
            address = address + ', ' + self.street2
        if self.city_id:
            address = address + ', ' + self.city_id.name
        if self.state_id:
            address = address + ', ' + self.state_id.code
        if self.zip:
            address = address + ' Z- ' + self.zip

        self.name = address

class ResPartner(models.Model):
    _inherit = "res.partner"

    address_ids = fields.One2many('partner.address', 'partner_id', string=u'Emails')
    area = fields.Char(u'Area')
    group = fields.Char(u'Group')
    building = fields.Char(u'Building')
    flat = fields.Char(u'Flat')
    fullfy_partner_id = fields.Char("ID")
    frist_name = fields.Char('Frist Name')
    middle_name = fields.Char('Midle Name')
    last_name = fields.Char('Last Name')

    @api.one
    @api.depends('frist_name', 'middle_name', 'last_name')
    def _get_partner_full_name(self):
        fullname = ''
        if self.frist_name:
            fullname+= self.frist_name
        if self.middle_name:
            fullname+= " "+self.middle_name
        if self.last_name:
            fullname+= " "+self.last_name
        self.name =fullname

    @api.model
    def create(self, vals):
        fullname=''
        if 'frist_name' in vals and vals.get('frist_name'):
            fullname += vals['frist_name']
        if 'middle_name' in vals and vals.get('middle_name'):
            fullname += " " + vals['middle_name']
        if 'last_name' in vals and vals.get('last_name'):
            fullname += " " + vals['last_name']
        vals['name'] = fullname

        return super(ResPartner, self).create(vals)

    @api.multi
    def write(self, vals):
        frist_name = self.frist_name
        if 'frist_name' in vals and vals.get('frist_name'):
            frist_name = vals['frist_name']
        middle_name = self.middle_name
        if 'middle_name' in vals and vals.get('middle_name'):
            middle_name = vals['middle_name']
        last_name = self.last_name
        if 'last_name' in vals and vals.get('last_name'):
            last_name = vals['last_name']
        vals['name'] =  frist_name+" " +middle_name+" "+ last_name
        return super(ResPartner, self).write(vals)

