# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution#
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

{
    'name': 'Partner multiple addresses',
    'version': '0.008',
    'category': 'Customizations',
    'sequence': 16,
    'complexity': 'normal',
    'description': '''== Partner multiple addresses ==\n\n
''',
    'author': 'Mohamed Mtloob',
    'license': 'AGPL-3',
    'website': 'http://linkedin.com/in/mohamed-mtloob-62b33b76',
    'images': ['images/oerp61.jpeg',
               ],
    'depends': [
        'contacts'
    ],
    'data': [
        'data/res.state.city.csv',
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/br_base_view.xml',
    ],
    'init': [],
    'demo': [],
    'update': [],
    'installable': True,
    'application': False,
    # If it's True, the modules will be auto-installed when all dependencies
    # are installed
    'auto_install': False,
    'certificate': '',
}
