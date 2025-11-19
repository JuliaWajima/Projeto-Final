from app import app,db
from flask import render_template,url_for,request,redirect,flash
from app.models import User
from app.forms import Userform,LoginForm
from app import login_manager
from app.models import User
from flask_login import login_user,logout_user,current_user



@app.route('/',methods=['GET','POST'])
def homepage():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.senha.data):
            login_user(user)
            return(redirect(url_for('homepage')))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('index.html',form=form)

@app.route('/pag/inicio/bem-vindo')
def paginicio():
    return render_template('info.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/cadastrar',methods=['GET','POST'])
def cadastro():
    form=Userform()
    if form.validate_on_submit():
        user=form.save()
        login_user(user,remember=True)
        return redirect(url_for('homepage'))
    return render_template('cadastro.html',form=form)

@app.route('/sair/')
def logout():
    logout_user()
    return redirect(url_for('homepage'))
