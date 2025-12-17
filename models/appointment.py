from odoo import models, api, fields


class HospitalAppointment(models.Model):
    
    
    _name = "hospital.management.appointment"
    # _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Hospital Appointments"
    _order = "create_date DESC"
    # _rec_name= "ref"
   
    patient_id = fields.Many2one('hospital.management.patient', string="Patient")
    doctor_id =  fields.Many2one('hospital.management.doctor', string="Doctor")
    patient_name = fields.Char(related=patient_id.name)
    doctor_name = fields.Char(related=doctor_id.name)
    gender = fields.Selection(related="patient_id.gender")
    ref = fields.Char(related="patient_id.ref")
    appointment_time = fields.Datetime(string="Choose Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Choose Date", default=fields.Date.context_today)
    
    
    