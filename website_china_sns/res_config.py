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

class website_config_settings(osv.osv_memory):
    _inherit = 'website.config.settings'

    _columns = {        
        'social_weibo': fields.related('website_id', 'social_weibo', type="char", string='Weibo Account'),
        'social_qq': fields.related('website_id', 'social_qq', type="char", string='QQ Account'),
        'social_weixin': fields.related('website_id', 'social_weixin', type="char", string='Weixin Account'),
        'social_renren': fields.related('website_id', 'social_renren', type="char", string='Renren Account'),
        'social_phone': fields.related('website_id', 'social_phone', type="char", string='Phone Account'),
        'social_mail': fields.related('website_id', 'social_mail', type="char", string='Mail Account'),
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
