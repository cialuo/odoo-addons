# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2001-2015 Zhuhai sunlight software development co.,ltd. All Rights Reserved.
#    Author: Kenny
#    Website: http://zhsunlight.cn
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

from openerp.osv import fields, osv

class website(osv.osv):
    _inherit = "website" # Avoid website.website convention for conciseness (for new api). Got a special authorization from xmo and rco
    _columns = {
        'social_weibo': fields.char('Weibo Account'),
        'social_qq': fields.char('QQ Account'),
        'social_weixin': fields.char('Weixin Account'),
        # 'social_renren': fields.char('Renren Account'),
        'social_phone': fields.char('Phone Account'),
        'social_mail': fields.char('Mail Account'),
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
