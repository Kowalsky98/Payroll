# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee"

    slip_ids = fields.One2many(
        "hr.payslip", "employee_id", string="Payslips", readonly=True
    )
    payslip_count = fields.Integer(
        compute="_compute_payslip_count",
        groups="payroll.group_payroll_user",
    )

    def _compute_payslip_count(self):
        for employee in self:
            employee.payslip_count = len(employee.slip_ids)

    dependent_children_ids = fields.One2many(
        "hr.employee.dependent", "employee_id",
        string="Hijos Dependientes"
    )

    def action_add_child(self):
        """ Abre un formulario para agregar un hijo dependiente. """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Añadir Hijo Dependiente',
            'res_model': 'hr.employee.dependent',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_employee_id': self.id},
        }