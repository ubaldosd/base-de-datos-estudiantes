# documento StringField
# nombre StringField
# ciclo SelectField
# genero StringField
# estado BooleanField

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, submitField

class formulario_estudiante(FlaskForm):
    documento = StringField("documento")
    nombre = StringField("nombre")
    ciclo = SelectField("ciclo",choices=[("ciclo1"),("ciclo2"),("ciclo3")])
    genero = SelectField("genero",choices=[("femenino"),("masculino")])
    estado = BooleanField("estado")
    guardar = submitField("guardar", render_kw={})
    insertar = submitField("insertar", render_kw={})
    eliminar = submitField("eliminar", render_kw={})
    actualizar = submitField("actualizar", render_kw={})
