# Copyright 2020 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Band Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Akretion',
    'website': 'www.akretion.com',
    'depends': [
        # Booking features
        "band_booking", # https://github.com/clementmbr/crm-booking
        # Improve UX :
        "base_usability",  # https://github.com/akretion/odoo-usability
        "web_form_background_color",  # https://github.com/clementmbr/band-booking
        "disable_odoo_online", # https://github.com/OCA/server-brand
        "remove_odoo_enterprise", # https://github.com/OCA/server-brand
    ],
    'data': [
    ],
    'demo': [
    ],
}
