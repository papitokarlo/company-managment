from odoo import models


class EmployeerXls(models.AbstractModel):
    _name = 'report.company.report_departament_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, line):
        c = 0
        for lines in line:
            c += 1
            format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
            format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter', })
            sheet = workbook.add_worksheet('person %s' % (c))
            sheet.set_column(1, 1, 50)
            sheet.set_column(0, 0, 30)
            sheet.write(0, 0, 'Departament', format1)
            sheet.write(0, 1, lines.departament, format2)
            sheet.write(1, 0, 'Manager', format1)
            sheet.write(1, 1, str(lines.departament_manager), format2)
            sheet.write(2, 0, 'count', format1)
            sheet.write(2, 1, lines.departament_employeer_amount, format2)