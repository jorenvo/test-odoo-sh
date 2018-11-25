# -*- coding: utf-8 -*-
from odoo import http

# class MyModule(http.Controller):
#     @http.route('/my_model/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_model/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module.listing', {
#             'root': '/my_model',
#             'objects': http.request.env['my_model'].search([]),
#         })

#     @http.route('/my_model/objects/<model("my_model"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module.object', {
#             'object': obj
#         })