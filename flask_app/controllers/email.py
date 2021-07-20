from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.emails import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def show_email():
    emails = Email.show()
    return render_template('success.html', emails = emails)

@app.route('/create_email', methods = ['POST'])
def create_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    
    email = Email.make(request.form)
    return redirect('/success')



