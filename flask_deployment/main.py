#pip install flask
#from crypt import methods
#from urllib import request
from flask import Flask,render_template,request
import joblib
#initialize the app
app=Flask(__name__)
#load the model
model=joblib.load('diabetes_79.pkl')
@app.route("/")
def home():
    return render_template('main.html')
@app.route("/contact_us")
def contact():
    return render_template('contact_us.html')
@app.route("/blog")
def blogs():
    return render_template('blog.html')
@app.route("/form",methods=['post'])
def form():
    
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    predi=request.form.get('predi')
    age=request.form.get('age')
    
    

    result=model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(predi),int(age)]])
    if result[0]==1:
        data='person is diabetic'
    else:
        data='person is diabetic'
    return data







#run the app
app.run(debug=True) #created a server