from flask import Flask, render_template, request
import joblib
from pathlib import Path


app = Flask(__name__)

#load the model
model = joblib.load(open('model/diabetic_80.pkl','rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/images')
def images():
    return render_template("images.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/data', methods = ['post'])
def data():
    first_name = request.form.get("first_name")
    second_name = request.form.get("second_name")
    phone_number = request.form.get("phone_number")
    email = request.form.get("email") 
    print(first_name, second_name, phone_number, email)
    return "data received"

@app.route('/predict', methods=['post'])
def predict():
    # names = ['preg' , 'plas' , 'pres', 'skin' , 'test', 'mass' , 'pedi', 'age', 'class']
    preg = int(request.form.get('preg'))
    plas = int(request.form.get('plas'))
    pres = int(request.form.get('pres'))
    skin = int(request.form.get('skin'))
    test = int(request.form.get('test'))
    mass = int(request.form.get('mass'))
    pedi = int(request.form.get('pedi'))
    age = int(request.form.get('age'))

    print(preg, plas, pres, skin, test, mass, pedi, age)


    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])[0]
    print(result)

    if result == 1:
        data = 'person is diabetic'
    else:
        data = 'person is NOT diabetic'
    print(data)
    return render_template('predict.html', data = data)

app.run(debug=True)
