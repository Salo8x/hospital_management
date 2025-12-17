{
    "name":"Hospital Management",
    "depends":['mail'],
    
    "data":[
        "security/ir.model.access.csv",
        
        "views/patient_view.xml",
        "views/female_patients.xml",
        "views/appointment_view.xml",
        "views/menu.xml",   
    ],
    
    "installable": True,
    "application" :True,
    "license": "LGPL-3",
    "sequence":-100
}