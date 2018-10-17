"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, flash, redirect, url_for, request
from .forms import LogUserForm, secti,masoform, DetiForm
from ..data.database import db
from ..data.models import Deti

blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

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

@blueprint.route('/zapis',methods=['GET', 'POST'])
def ZapisDeti():
    form = DetiForm()
    if form.validate_on_submit():
       Deti.create(**form.data)
    return render_template("public/zapisDeti.tmpl", form=form)

@blueprint.route('/list', methods=['GET','POST'])
def DetiList():
    detiList = db.session.query(Deti).all()
    return render_template('public/list.tmpl', detiList = detiList)

@blueprint.route('/edit/<int:id>', methods=['GET','POST'])
def DetiEdit(id):
    user = db.session.query(Deti).get(id)
    form = DetiForm(obj=user)
    if form.validate_on_submit():
        user.update(**form.data)
        flash("Ulozeno",category="info")
        return redirect(request.args.get('next') or url_for('public.DetiList'))
    return render_template('public/zapisDeti.tmpl', form=form)

@blueprint.route('/delete/<int:id>', methods=['GET','POST'])
def DetiDel(id):
    delDeti = db.session.query(Deti).get(id)
    db.session.delete(delDeti)
    db.session.commit()
    flash("Smazano", category="info")
    return redirect(request.args.get('next') or url_for('public.DetiList'))
