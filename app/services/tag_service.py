from app.models.tag_model import Tag, TagSchema
from app.models.patient_model import Patient, PatientSchema

def svc_create_tag(tags, patient, session):
    for tag in tags:

        obj = {
            "tag": tag.casefold(),
            "alert_tag": False,
        }
        new_tag = Tag(**obj)
        session.add(new_tag)
        patient.tags.append(new_tag)

def svc_create_alert_tag(alerts, patient, session):
    for alert in alerts:
            obj = {
                "tag": alert.casefold(),
                "alert_tag": True,
            }
            new_tag = Tag(**obj)
            session.add(new_tag)
            patient.tags.append(new_tag)

def svc_update_delete_tag(tags, alerts, patient, session):
    patient.tags = []
    svc_create_tag(tags, patient, session)
    svc_create_alert_tag(alerts, patient, session)