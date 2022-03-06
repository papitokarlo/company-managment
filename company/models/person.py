from odoo import api, fields, models
from odoo.exceptions import ValidationError
import datetime
from dateutil.relativedelta import relativedelta

import json

from odoo.tools.sql import existing_tables

class Company_Persons(models.Model):
    _name = "company.employee"
    _inherit = ["mail.thread"]
    _description = "Company Empoyee"

    name = fields.Char(string='Name', required=True, translate=True)
    lastname = fields.Char(string ="Lastname", required =True)
    selfid = fields.Char(string='Personal ID', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other',)
    birthdate = fields.Date(string = "date  of birth",)
    age=fields.Integer(string="age", compute="_get_age", store =True )
    birthplace = fields.Char(string = "palce of birth")
    sitizen = fields.Char(string="Citizen:")
    departament = fields.Many2one("employeer.departament", string="departament")
    feature = fields.Many2many("empoyer.feature", string ="feature" )
    note = fields.Text(string='Description')
    image=fields.Binary(string="Person Image")
    image2=fields.Binary(string="Second Person Image")
            
    def export_to_json(self):
        #data="[{'name':self.name, 'lastname':self.lastname, 'Id':self.selfid, 'gender':self.gender, 'place of birth':self.birthplace, 'date of birt':self.birthdate,}]" 
        for i in self:
            formated_date=i.birthdate.isoformat()
            dep=i.departament
            formated_departament=str(dep)
            for j in i.feature:
                print(j)        
            
            data={
                'name':i.name,
                'lastname':i.lastname,
                'Id':i.selfid,
                'gender':i.gender,
                'place of birth':i.birthplace, 
                'date of birt':formated_date,
                'departament':formated_departament,                
                'note':i.note
            }          
        with open("employeer_json_details.json", "w") as emp:
            json.dump(data, emp)
        print(f"JSON file Created.......................................{data}............{type(self.feature)}............................................")

    #date years
    @api.depends("birthdate")
    def _get_age(self):
        today= datetime.date.today()
        for em in self:
            if em.birthdate:
                #birthdate = fields.Datetime.to_datetime(em.birthdate).date()
                total_age=relativedelta(today, em.birthdate).years
                print(f'______________________{total_age}')
                em.age = total_age
                if em.age<18:
                    raise ValidationError('Employeer age is unappripiate/ he/she must be 18+')


    @api.constrains('selfid')
    def _check_employeer_id(self):        
        if self.selfid.isdigit()==True:
            for i in self:
                if len(i.selfid) > 11:
                    raise ValidationError(f'it must contain 11 digits, it contains more than 11 digits')

                elif len(i.selfid) < 11:
                    raise ValidationError(f'it must contain 11 digits, it contains less than 11 digits')           
        
        else:
            raise ValidationError('Validation error / write only integers!!!')

    
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s  %s' % (rec.name, rec.lastname)))
        return res