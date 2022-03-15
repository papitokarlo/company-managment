from odoo import tools,  models, fields,  _


class DepartamentReport(models.AbstractModel):
    _name = 'departament.report.sql'
    _rec_name = "departament"


    departament = fields.Char(string="Departament")
    amount = fields.Integer(string="Departament members")
    manager = fields.Char(string="manager")
    
    

    def init(self):
        tools.drop_view_if_exists(self._cr, 'departament_report_sql')
        self._cr.execute("""
                        CREATE OR REPLACE VIEW departament_report_sql AS (
                            SELECT row_number() OVER () AS id, employeer_departament.departament AS departament, 
                            company_employee.name AS manager, 
                            COUNT(company_employee.departament) AS amount
                            FROM employeer_departament 
                            LEFT JOIN company_employee ON employeer_departament.id = company_employee.departament
                            GROUP BY employeer_departament.departament, company_employee.name
                        )""")
