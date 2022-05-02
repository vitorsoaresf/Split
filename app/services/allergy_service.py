from app.models.allergy_model import Allergy, AllergySchema

def svc_create_allergy(allergies, session):
    list_allergies = []
    for allergy in allergies:
        
        #Normalization
        allergy = allergy.casefold()

        al = Allergy.query.filter_by(name=allergy).first()

        if not al:
            obj = {"name": allergy}

            schemaAllergy = AllergySchema()
            schemaAllergy.load(obj)

            al = Allergy(**obj)

            session.add(al) 
            session.commit()

        list_allergies.append(al)

    return list_allergies

def svc_update_allergy(patient, allergies, session):
    patient.allergies = []
    for allergy in allergies:
        
        #Normalization
        allergy = allergy.casefold()

        al = Allergy.query.filter_by(name=allergy).first()

        if not al:
            obj = {"name": allergy}

            schemaAllergy = AllergySchema()
            schemaAllergy.load(obj)

            al = Allergy(**obj)

            session.add(al) 
            session.commit()

        patient.allergies.append(al)
    
