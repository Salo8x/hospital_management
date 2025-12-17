from odoo import models, api, fields
from datetime import date

class HospitalPatient(models.Model):
    
    
    _name = "hospital.management.patient"
    # _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Hospital Patient"
    _order = "create_date DESC"
   
    
    
    name = fields.Char(string='Name' ,required=True, tracking=True)
    age = fields.Integer(string='Age', compute="_compute_age", inverse="_inverse_age", readonly=False)
    ref = fields.Char(string="Reference")
    gender = fields.Selection([('male', 'Male'),('female','Female')], string='Gender',required=True)
    dob = fields.Date(string='Date of Birth')
    
    active = fields.Boolean(string="Active", default=True)
    appointments = fields.One2many("hospital.management.appointment","patient_id", string="Appointments")
    
    @api.depends('dob')
    def _compute_age(self):
      
        today = fields.Datetime.now()
        print(f"Compute methoid is called ")
       
        for rec in self:
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age =0 
    
    
    # @api.onchange('dob')
    # def _compute_age(self):
      
    #     today = fields.Datetime.now()
    #     print(f"Compute methoid is called ")
       
    #     for rec in self:
    #         if rec.dob:
    #             rec.age = today.year - rec.dob.year
    #         else:
    #             rec.age =0 
                
                
    def _inverse_age(self):
        today = fields.Datetime.now()
        
        for rec in self:
            if rec.age:
                year = today.year - rec.age
                rec.dob = date(year,1,1)
            else:
                rec.dob = False
    
    
    #on_create
    
    #write()
    