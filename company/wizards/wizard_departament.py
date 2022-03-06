from odoo import models, fields


class CreateDepartament(models.TransientModel):
    _name = 'temporary.create.departament'
    _description = 'Create Departament Wizard'
    


    departament = fields.Many2one('employeer.departament', string="deprtament")
    departament_manager = fields.Many2one('company.employee',  string = "manager")
    amount = fields.Integer(string="Number of employeers")
    """

    def init(self):
        departaments =self.env['employeer.departament'].search([])
        print('__------------------------------------_____------', self.env['employeer.departament'])
        dep = []
        man = []
        am = []
        for i in departaments:
            print('__------------------------------------_____------', i)
            dep.append(i.departament)
            man.append(i.departament_manager)
            am.append(i.departament_employeer_amount)
        self.departament= dep
        self.departament_manager= man
        self.amount = am

        print('_________________--------------_-------------_-------_-_--_-',self.departament, dep, self.departament_manager, man, am)"""