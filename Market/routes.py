from Market import app
from flask import render_template,redirect,url_for,flash, get_flashed_messages
from Market.models import item,user
from Market.forms import Register_Form
from Market import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = item.query.all()
    return render_template('market.html', items=items)

@app.route('/registration',methods=['POST','GET'])
def registration_page():
    form = Register_Form()
    if form.validate_on_submit():
        newuser = user(uName = form.username.data, email_add=form.email_add.data, password_hash = form.password1.data)
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error while creating the use : {err_msg}',category='Danger')
    return render_template('register.html',form=form)