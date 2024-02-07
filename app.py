from flask import Flask, render_template, request

app = Flask(__name__)#creating the app instance
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        
        name=request.form['name']
        email=request.form['email']
        return render_template('thankyou.html',name=name, email=email)
    return render_template('submit.html')

@app.route('/thank_you.html')
def thank_you():
    return render_template('submit.html')

    
   

