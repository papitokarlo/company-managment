from odoo import models


class EmployeerXls(models.AbstractModel):
    _name = 'report.company.report_employeer_xlsx'
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
            sheet.write(0, 0, 'Name', format1)
            sheet.write(0, 1, lines.name, format2)
            sheet.write(1, 0, 'lastname', format1)
            sheet.write(1, 1, lines.lastname, format2)
            sheet.write(2, 0, 'id', format1)
            sheet.write(2, 1, lines.selfid, format2)
            sheet.write(3, 0, 'gender', format1)
            sheet.write(3, 1, lines.gender, format2)
            sheet.write(4, 0, 'date of birth', format1)
            sheet.write(4, 1, lines.birthdate, format2)            
            sheet.write(5, 0, 'age', format1)
            sheet.write(5, 1, lines.age, format2)            
            sheet.write(6, 0, 'place of birth', format1)
            sheet.write(6, 1, lines.birthplace, format2)                        
            sheet.write(7, 0, 'moqalaqeoba', format1)
            sheet.write(7, 1, lines.sitizen, format2)
            
            sheet.write(8, 0, 'departament', format1)
            sheet.write(8, 1, str(lines.departament), format2)
            sheet.write(9, 0, 'feature', format1)
            sheet.write(9, 1, str(lines.feature), format2)
            
        