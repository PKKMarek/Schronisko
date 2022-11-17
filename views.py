from flask import Blueprint, render_template

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/NasiOpiekunowie")
def NasiOpiekunowie():
    return render_template("indexNasiOpiekunowie.html")

@views.route("/NaszePsiaki")
def NaszePsiaki():
    return render_template("indexNaszePsiaki.html")

@views.route("/Kontakt")
def Kontakt():
    return render_template("indexKontakt.html")