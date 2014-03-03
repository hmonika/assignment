from bottle import route, run, template, get, post, request,delete,put
patient_details={}


  
@post('/patient/create')
def create_patient():
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    patient_info={}
    patient_info["Name"] = p_name
    patient_info["Gender"] = p_gender
    patient_info["Age"] = p_age
    patient_info["Address"] = p_address
    patient_info["Phone"] = p_phone
    patient_details.update({p_id:patient_info})
    return patient_details

@get('/patient/read/<p_id>')
def read_patient(p_id):
    if p_id not in patient_details.keys():
        return 'This is not a correct patient id'
    else:
        return patient_details[p_id]

@put('/patient/update/<p_id>')
def update_patient(p_id):
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    patient_info={}
    patient_info["Name"] = p_name
    patient_info["Gender"] = p_gender
    patient_info["Age"] = p_age
    patient_info["Address"] = p_address
    patient_info["Phone"] = p_phone
    patient_details.update({p_id:patient_info})
    return patient_details
   


@delete('/patient/delete/<p_id>')
def delete_patient(p_id):
    patient_details.pop(p_id)
    return patient_details


run(host='localhost',port=7002)
