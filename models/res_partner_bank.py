# models/res_partner_bank.py
from odoo import models, fields

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    x_type = fields.Selection([
        ('national', 'V'),
        ('foreign', 'E'),
        ('juridical', 'J'),
        ('passport', 'P'),
        ('government', 'G'),
    ], string="Tipo de Identificación", help="Tipo de Identificación: V: Venezolano, E: Extranjero, J: Jurídico, P: Pasaporte, G: Gobierno")
    x_identification_id = fields.Char(string="Cédula")
    x_payment_type = fields.Selection([
        ('Abono de Cuenta BdV', '1'),
        ('Transferencia Swift', '2'),
        ('Cheque de Gerencia', '3'),
    ], string="Tipo de Pago", help="Tipo de Pago: 1: Abono de Cuenta BdV, 2: Transferencia Swift, 3: Cheque de Gerencia")
    x_credit_reference = fields.Char(string="N° de Referencia de Crédito")
    x_account_type = fields.Selection([
        ('corriente', 'C'),
        ('ahorro', 'A'),
    ], string="Tipo de Cuenta", help="Tipor de cuenta Bancaria C: Corriente, A: Ahorro")
    x_check_duration = fields.Integer(string="Duración del Cheque (Días)")
    x_beneficiary_email = fields.Char(string="Email del Beneficiario")
