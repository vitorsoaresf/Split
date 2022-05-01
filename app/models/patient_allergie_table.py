from app.configs.database import db


patients_allergies = db.Table ( "patients_allergies",
        db.Column("patients_allergies_id", db.Integer, primary_key=True),
        db.Column("patient_id",db.Integer, db.ForeignKey("patients.patient_id") ),
        db.Column("allergy_id", db.Integer,db.ForeignKey("allergies.allergy_id"))
)