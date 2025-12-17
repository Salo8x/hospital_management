from odoo import models, fields, api


class HospitalDoctor(models.Model):
    _name = "hospital.management.doctor"
    # _inherit = ["hospital.base.model"]

    _description = "Data of doctors"
    _order = "create_date desc"
    # _rec_name = "specialty"
    
    name = fields.Char(string="Doctor Name", required=True)
    qualification = fields.Char(string="Qualification", required=True)
    specialty = fields.Selection([("cardiology","Cardiology"),("dermatology",'Dermatology'),("neurology","Neurology"),("oncology","Oncology")],string="Specialization", required=True)
    # user_id = fields.Many2one('res.users',string='Related User')
    # Rename phone field label for doctors
    phone = fields.Char(string="Office Phone")  # This overrides inherited field
    is_available = fields.Boolean(string="Available", default=True)

    
   
    
    
    
   
    
        
   