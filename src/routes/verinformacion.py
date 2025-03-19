# routes/verinformacion.py
from flask import Blueprint, render_template
from models import Remesa, Inventario, Proveedores, Ventas, Paciente, Pagos

verinformacion_bp = Blueprint('verinformacion', __name__)

@verinformacion_bp.route('/remesas', methods=['GET'])
def ver_remesas():
    remesas = Remesa.query.all()
    return render_template('verinformacion/remesa.html', datos=remesas)

@verinformacion_bp.route('/inventarios', methods=['GET'])
def ver_inventarios():
    inventarios = Inventario.query.all()
    return render_template('verinformacion/inventarios.html', datos=inventarios)

@verinformacion_bp.route('/proveedores', methods=['GET'])
def ver_proveedores():
    proveedores = Proveedores.query.all()
    return render_template('verinformacion/proveedores.html', datos=proveedores)

@verinformacion_bp.route('/ventas', methods=['GET'])
def ver_ventas():
    ventas = Ventas.query.all()
    return render_template('verinformacion/ventas.html', datos=ventas)

@verinformacion_bp.route('/pacientes', methods=['GET'])
def ver_pacientes():
    pacientes = Paciente.query.all()
    return render_template('verinformacion/paciente.html', datos=pacientes)

@verinformacion_bp.route('/pagos', methods=['GET'])
def ver_pagos():
    pagos = Pagos.query.all()
    return render_template('verinformacion/pagos.html', datos=pagos)


