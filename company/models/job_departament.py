from odoo import api, tools, models, fields,  _
import json

class Departament(models.Model):
    _name = 'employeer.departament'
    _description = 'departament'
    _rec_name = "departament"

    departament = fields.Char(string = "departament", required=True,) 
    dep_members_ids = fields.One2many("company.employee", "departament", string="All employeers of departament", domain= "[('departament', '=', False)]")
    departament_manager = fields.Many2one("company.employee", string="manager") #domain  domain="[('id', '=', dep_members_ids)]
    departament_employeer_amount = fields.Integer(string = "Number of registred empoyeers", compute="_compute_departament_employeer_amount")

            
    def _compute_departament_employeer_amount(self):
        for rec in self:
            self.departament_employeer_amount=len(rec.dep_members_ids)                     
           

    def export_into_json(self):
        for i in self:        
            data={
                'feature':i.departament,
                'describe':i.departament_employeer_amount,
                'departament members': str(i.dep_members_ids),
            }          
        with open("departament_json_details.json", "w") as emp:
            json.dump(data, emp)






"""class DepartamentReport(models.AbstractModel):
    _name = 'departament.report.sql'
    _rec_name = "departament_name"


    departament_name = fields.Many2one('employeer.departament',string="Departament")
    manager = fields.Many2one('company.employee',string="Manager")

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'departament_report_sql' )"""