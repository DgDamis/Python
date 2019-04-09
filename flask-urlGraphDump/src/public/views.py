"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, jsonify,
import urllib2
from .forms import LogUserForm, secti,masoform
from ..data.database import db
from ..data.models import LogUser
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

@blueprint.route('/data', methods=['GET','POST'])
def dataout():
        import json
        import os
        from ..data.models import Data
        os.environ["no_proxy"]="*"
        natahnuteData = urllib2.urlopen('http://192.168.10.1:5000/data.json',)
        natahnuteData = json.load(natahnuteData)
        print natahnuteData
        natahnuteData = Data(id="",,hodnota=natahnuteData['CPU'])
        db.session.add(natahnuteData)
        return render_template('public/datavystup.tmpl',data = natahnuteData)

