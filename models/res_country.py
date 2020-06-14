# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields



class ResCountry(models.Model):
    _inherit = 'res.country'

    bc_code = fields.Char(u'Código BC', size=5)
    ibge_code = fields.Char(u'Código IBGE', size=5)
    siscomex_code = fields.Char(u'Código Siscomex', size=4)


class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    ibge_code = fields.Char(u'Código IBGE', size=2)

class ResStateCity(models.Model):

    _name = 'res.state.city'
    _description = u'Município'

    name = fields.Char(string='Nome', size=64, required=True)
    state_id = fields.Many2one(comodel_name='res.country.state',
                               string='Estado',
                               required=True)
    ibge_code = fields.Char(string=u'Código IBGE', size=7, copy=False)
