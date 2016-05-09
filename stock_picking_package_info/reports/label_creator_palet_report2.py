# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more summary.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

#from barcode.writer import ImageWriter
#from barcode import generate
from Code128 import Code128
import base64
from StringIO import StringIO

import time
import math
from openerp.osv import osv
from openerp.report import report_sxw


class label_creator_palet2(report_sxw.rml_parse):

    def _generateBarcode(self, barcode_string):  #, height, width):
        fp = StringIO()
        #generate('CODE39', barcode_string, writer=ImageWriter(), add_checksum=False, output=fp)
        #barcode_data = base64.b64encode(fp.getvalue())
        #return '<img style="width: 25mm;height: 7mm;" src="data:image/png;base64,%s" />'%(barcode_data)
        #return barcode_data
        Code128().getImage(barcode_string, path="./").save(fp,"PNG")
        barcode_data = base64.b64encode(fp.getvalue())
        return barcode_data

    def __init__(self, cr, uid, name, context):
        super(label_creator_palet2, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'generateBarcode':self._generateBarcode,
        })


class report_product_barcode_print(osv.AbstractModel):
    _name = 'report.stock_picking_package_info.label_creator_palet_report_document2'
    _inherit = 'report.abstract_report'
    _template = 'stock_picking_package_info.label_creator_palet_report_document2'
    _wrapped_report_class = label_creator_palet2

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
