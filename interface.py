from flask import Flask ,render_template ,jsonify,request,redirect, url_for

import config

from Project_app.utils import MedicalInsurance

app  = Flask(__name__)
###########################################################################################
############################### Base API ##################################################
###########################################################################################
@app.route("/") # HOME API
def hello_flask():
    print("Welcome to flask")
    return render_template("login.html")

@app.route('/result/<name>')
def result(name):
    return f"Hello {name}"


@app.route('/testing/<student_name>')
def testing1(student_name):
    return f"Hello {student_name}"


@app.route('/marks/<float:score>')
def marks(score):
    return f"Hello {score}"

@app.route('/login',methods = ['POST','GET'])
def login():
    print("hello")
    if request.method == 'POST':

        data = request.form
        name = data['name']
        print("Name : ",name)
        return redirect(url_for('result',name == name))


###########################################################################################

@app.route("/predict_charges")
def get_insurance_charges():
    
    print("We are using POST Method")
    data = request.form
    print("Data :",data)
    age = eval(data['age'])
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker  = data['smoker']
    region = data['region']

    print("age,sex,bmi,children,smoker,region",age,sex,bmi,children,smoker,region)

    med_ins = MedicalInsurance(age,sex, bmi,children,smoker,region)
    charges = med_ins.get_predicted_charges()

    return jsonify ({"Result": f"Predicted medical insurance charges are:{charges}"})






if __name__ == "__main__":
    app.run()