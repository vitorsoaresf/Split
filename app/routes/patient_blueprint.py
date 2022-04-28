from flask import Blueprint
from app.controllers import patient_controller

bp = Blueprint("patients", __name__, url_prefix="/patients")

bp.post("")(patient_controller.create_patient)
bp.get("")(patient_controller.get_patients)
bp.delete("/<int:id>")(patient_controller.delete_patient)