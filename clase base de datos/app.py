from flask import Flask, render_template, request
from formulario import formulario_estudiante
import os

app = Flask(__name__)

app.secret_key=os.urandom(24)

app.route("/")


def formulario_estudiante():
    form= formulario_estudiante()
    return render_template("formulario.html", form=form)

if (__name__=="__main__"):
    app.run(debug=True)