from turtle import st
from odoo import models, fields, api,  _
from odoo.exceptions import ValidationError
import json

class Feature(models.Model):
    _name = 'empoyer.feature'
    _description = 'feature'
    _rec_name = "feature"

    feature = fields.Char(string = "feature", required=True,)
    descr = fields.Char(string ="feature description")
    
    def export_to_json(self):
        for i in self:        
            data={
                'feature':i.feature,
                'describe':i.descr,
            }          
        with open("feature_json_details.json", "w") as emp:
            json.dump(data, emp)
        print(f"JSON file Created.......................................{data}............{type(self.feature)}............................................")