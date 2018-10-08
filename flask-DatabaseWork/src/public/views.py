"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, flash
from .forms import LogUserForm, secti,masoform, VstupForm, gameuserForm
from ..data.database import db
from ..data.models import LogUser, GameUser
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/vstup', methods=['GET','POST'])
def vstup():
    form = VstupForm()
    if form.validate_on_submit():
        return render_template('public/vystup2.tmpl', ks=form.ks.data, cena=form.cena.data, DPH=form.DPH.data,
                               celkem=float(form.cena.data)*float(form.ks.data)*float((float(form.DPH.data)/100)+1))
    return render_template('public/vstup.tmpl',form = form)

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

@blueprint.route('/newgameuser', methods=['GET','POST'])
def gameuseredit():
    form = gameuserForm()
    if form.validate_on_submit():
        new_gameuser = GameUser.create(**form.data)
    return render_template('public/gameuser.tmpl', form=form)

@blueprint.route('/gameuseredit/<int:id>', methods=['GET','POST'])
def gameusere(id):
    user = db.session.query(GameUser).get(id)
    form = gameuserForm(obj=user)
    if form.validate_on_submit():
        user.update(**form.data)
        flash("Ulozeno",category="info")
    return render_template('public/gameuser.tmpl', form=form)

@blueprint.route('/gameuserlist', methods=['GET','POST'])
def gameuserlist():
    userList = db.session.query(GameUser).all()
    return render_template('public/gameuserlist.tmpl', userList = userList)