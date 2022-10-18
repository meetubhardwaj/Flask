#pip install flask
from flask import Flask,render_template
#initialize the app
app=Flask(__name__)
@app.route("/")
def home():
    return render_template('main.html')
@app.route("/contact_us")
def contact():
    return render_template('contact_us.html')
@app.route("/blog")
def blogs():
    return render_template('blog.html')

#run the app
app.run(debug=True) #created a server