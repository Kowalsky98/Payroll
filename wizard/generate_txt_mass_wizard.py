import os
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class GenerateTxtMassWizard(models.TransientModel):
    _name = 'generate.txt.mass.wizard'
    _description = 'Generador masivo de archivo TXT a partir de nóminas seleccionadas'

    payslip_ids = fields.Many2many(
        'hr.payslip',
        string="Nóminas a Procesar",
        required=True
    )
     
    payment_date = fields.Date(
        string="Fecha de Pago",
        required=True,
        default=fields.Date.context_today,
    )

    def action_generate_txt(self):
        self.ensure_one()

        if not self.payslip_ids:
            raise UserError(_("No se han seleccionado nóminas para procesar."))

        # Construir el HEADER global
        header = "HEADER  " + "00000001" + "00000002" + "V" + "12345678" + \
            self.payment_date.strftime("%d/%m/%Y") + self.payment_date.strftime("%d/%m/%Y")

        debit_lines = []
        credit_lines = []
        secuencia = 1

        for payslip in self.payslip_ids:
            # Supongamos que cada nómina tiene un campo bank_id que apunta a res.partner.bank
            bank = payslip.bank_id
            if not bank:
                raise UserError(_("La nómina %s no tiene asignado un banco en el socio.") % payslip.name)

            # Validar datos necesarios
            if not bank.x_identification_id or len(bank.x_identification_id.strip()) < 4:
                raise UserError(_("La nómina %s tiene datos incompletos en el banco.") % payslip.name)
            if not bank.acc_number or len(bank.acc_number.strip()) != 20:
                raise UserError(_("La nómina %s tiene un número de cuenta inválido (debe ser de 20 dígitos).") % payslip.name)

            # Construir la línea de Débito para este registro
            debit_line = (
                "DEBITO  " +
                str(secuencia).zfill(8) +
                (bank.x_type.upper() if bank.x_type else "V") +
                bank.x_identification_id +
                (bank.partner_id.name.upper() if bank.partner_id.name else "").ljust(35) +
                self.payment_date.strftime("%d/%m/%Y") +
                ("00" if bank.x_account_type == 'corriente' else "01") +
                bank.acc_number +
                "00000000000000000000" +  # Aquí deberás colocar el monto o valor correspondiente
                "VEB40"
            )

            # Construir la línea de Crédito para este registro
            # Se usa información de ejemplo; en la práctica, puede venir de otros campos o cálculos
            credit_line = (
                "CREDITO " +
                str(secuencia).zfill(8) +
                (bank.x_type.upper() if bank.x_type else "V") +
                "XXXXXXXXXX".ljust(10) +
                (bank.partner_id.name.upper() if bank.partner_id.name else "").ljust(30) +
                "00000000000000000000" +
                "10" +
                "BSCHVECA".ljust(10)
            )

            debit_lines.append(debit_line)
            credit_lines.append(credit_line)
            secuencia += 1

        # Ejemplo de línea TOTAL (deberás calcular la cantidad y el monto real a partir de tus datos)
        num_lines = len(credit_lines)
        total_amount = "0000000000000013158.02,00"  # Este monto se debe calcular según tus datos reales
        total_line = "TOTAL   " + str(num_lines).zfill(5) + str(num_lines).zfill(5) + total_amount

        # Determinar la ruta del archivo (se usa /tmp por portabilidad; se puede parametrizar)
        file_dir = "/tmp"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_name = "NOMINAS_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        file_path = os.path.join(file_dir, file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(header + "\n")
                for dl in debit_lines:
                    f.write(dl + "\n")
                for cl in credit_lines:
                    f.write(cl + "\n")
                f.write(total_line + "\n")
        except Exception as e:
            raise UserError(_("Error al generar el archivo TXT: %s") % e)

        # Se notifica al usuario que el archivo se generó exitosamente.
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'generate.txt.mass.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_message': _("El archivo TXT ha sido generado en: %s") % file_path},
        }
