# routes/create.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import db
from models import Remesa, Inventario, Proveedores, Ventas, Pagos, Paciente

# Definir el Blueprint para agregar información
create_bp = Blueprint('create', __name__, url_prefix='/crear')  # El url_prefix ya está correctamente establecido.

# Ruta para agregar remesas
@create_bp.route('/agregar_remesa', methods=['GET', 'POST'])
def agregar_remesa():
    if request.method == 'POST':
        # Obtener datos del formulario
        id = request.form['id']
        Proveedor = request.form['Proveedor']
        CodigoElemento = request.form['CodigoElemento']
        Modelo = request.form['Modelo']
        Nombre = request.form['Nombre']
        Num_Entradas = request.form['Num_Entradas']
        Factura = request.form['Factura']
        Fecha = request.form['Fecha']

        # Crear una nueva instancia de Remesa
        nueva_remesa = Remesa(
            id=id,
            Proveedor=Proveedor,
            CodigoElemento=CodigoElemento,
            Modelo=Modelo,
            Nombre=Nombre,
            Num_Entradas=Num_Entradas,
            Factura=Factura,
            Fecha=Fecha
        )

        # Agregar la nueva remesa a la base de datos
        db.session.add(nueva_remesa)
        db.session.commit()

        # Mostrar mensaje de éxito y redirigir
        flash('Remesa agregada con éxito', 'success')
        return redirect(url_for('create.agregar_remesa'))  # Correcto, vuelve a la misma página

    # Si el método es GET, mostrar el formulario para agregar remesa
    return render_template('crearinformacion/remesa.html')


@create_bp.route('/agregar_inventario', methods=['GET', 'POST'])
def agregar_inventario():
    if request.method == 'POST':
        # Obtener datos del formulario
        Código_Prod = request.form['Código_Prod']
        Id_Proveedor = request.form['Id_Proveedor']
        Nombre_Prod = request.form['Nombre_Prod']
        Precio = request.form['Precio']
        Modelo = request.form['Modelo']
        Cantidad = request.form['Cantidad']
        Materiales = request.form['Materiales']

        # Crear una nueva instancia de Inventario
        nuevo_producto = Inventario(
            Código_Prod=Código_Prod,
            Id_Proveedor=Id_Proveedor,
            Nombre_Prod=Nombre_Prod,
            Precio=Precio,
            Modelo=Modelo,
            Cantidad=Cantidad,
            Materiales=Materiales
        )

        # Agregar el nuevo producto a la base de datos
        db.session.add(nuevo_producto)
        db.session.commit()

        # Mostrar mensaje de éxito y redirigir
        flash('Producto agregado con éxito', 'success')
        return redirect(url_for('create.agregar_inventario'))

    # Si el método es GET, obtener las listas de inventarios y proveedores para el formulario
    
    proveedores = Proveedores.query.all()  # Aquí consulta los proveedores desde el modelo Proveedores
    
    # Extraer solo los atributos necesarios de los productos
  

    # Pasar las listas a la plantilla
    return render_template('crearinformacion/inventario.html',  proveedores=proveedores)






# Ruta para agregar proveedor
@create_bp.route('/agregar_proveedor', methods=['GET', 'POST'])
def agregar_proveedor():
    if request.method == 'POST':
        # Obtener datos del formulario
        Id_Proveedor = request.form['Id_Proveedor']
        Código_Prod = request.form['Código_Prod']
        Nombre_Prov = request.form['Nombre_Prov']
        Correo = request.form['Correo']
        Dirección = request.form['Dirección']
        Teléfono = request.form['Teléfono']

        # Crear una nueva instancia de Proveedor
        nuevo_proveedor = Proveedores(
            Id_Proveedor=Id_Proveedor,
            Código_Prod=Código_Prod,
            Nombre_Prov=Nombre_Prov,
            Correo=Correo,
            Dirección=Dirección,
            Teléfono=Teléfono
        )

        # Agregar el nuevo proveedor a la base de datos
        db.session.add(nuevo_proveedor)
        db.session.commit()

        # Mostrar mensaje de éxito y redirigir
        flash('Proveedor agregado con éxito', 'success')
        return redirect(url_for('create.agregar_proveedor'))  # Correcto, vuelve a la misma página

    # Si el método es GET, mostrar el formulario para agregar proveedor
    return render_template('crearinformacion/proveedores.html')


@create_bp.route('/agregar_venta', methods=['GET', 'POST'])
def agregar_venta():
    if request.method == 'POST':
        # Obtener datos del formulario
        Id_Paciente = request.form['Id_Paciente']
        Graduacion = request.form['Graduacion']
        Armason = request.form['Armason']
        Tratamiento = request.form['Tratamiento']
        Anticipo = request.form['Anticipo']
        Adeudo = request.form['Adeudo']
        Fecha = request.form['Fecha']

        # Crear una nueva instancia de Venta
        nueva_venta = Ventas(
            Id_Paciente=Id_Paciente,
            Graduacion=Graduacion,  # Ahora coincide con el modelo
            Armason=Armason,
            Tratamiento=Tratamiento,
            Anticipo=Anticipo,
            Adeudo=Adeudo,
            Fecha=Fecha
        )



        # Agregar la nueva venta a la base de datos
        db.session.add(nueva_venta)
        db.session.commit()

        flash('Venta agregada con éxito', 'success')
        return redirect(url_for('create.agregar_venta'))

    # Obtener la lista de pacientes desde la base de datos
    pacientes = db.session.query(Paciente).all()  
    return render_template('crearinformacion/ventas.html', pacientes=pacientes)







@create_bp.route('/agregar_pago', methods=['GET', 'POST'])
def agregar_pago():
    # Obtener pacientes y ventas desde la base de datos
    pacientes = Paciente.query.all()
    ventas = Ventas.query.all()

    if request.method == 'POST':
        # Obtener datos del formulario
        Id_Pago = request.form['Id_Pago']
        Id_Paciente = request.form['Id_Paciente']
        Id_Venta = request.form['Id_Venta']
        SaldoAPagar = request.form['SaldoAPagar']
        Abono = request.form['Abono']
        SaldoActual = request.form['SaldoActual']
        Fecha = request.form['Fecha']

        # Crear una nueva instancia de Pago
        nueva_pago = Pagos(
            Id_Pago=Id_Pago,
            Id_Paciente=Id_Paciente,
            Id_Venta=Id_Venta,
            SaldoAPagar=SaldoAPagar,
            Abono=Abono,
            SaldoActual=SaldoActual,
            Fecha=Fecha
        )

        # Agregar el nuevo pago a la base de datos
        db.session.add(nueva_pago)
        db.session.commit()

        # Mensaje de éxito y redirección
        flash('Pago agregado con éxito', 'success')
        return redirect(url_for('create.agregar_pago'))

    # Si el método es GET, mostrar el formulario con los datos de pacientes y ventas
    return render_template('crearinformacion/pagos.html', pacientes=pacientes, ventas=ventas)





@create_bp.route('/agregar_paciente', methods=['GET', 'POST'])
def agregar_paciente():
    if request.method == 'POST':
        # Obtener datos del formulario
        Nombre_Pa = request.form['Nombre_Pa']
        Apellidos = request.form['Apellidos']
        Teléfono1 = request.form['Teléfono1']
        Teléfono2 = request.form['Teléfono2']
        Dirección = request.form['Dirección']
        Correo = request.form['Correo']

        # Crear una nueva instancia de Venta
        nueva_paciente = Pagos(
            
            Nombre_Pa=Nombre_Pa,
            Apellidos=Apellidos,
            Teléfono1=Teléfono1,
            Teléfono2=Teléfono2,
            Dirección=Dirección,
            Correo=Correo
        )

        # Agregar la nueva venta a la base de datos
        db.session.add(nueva_paciente)
        db.session.commit()

        # Mostrar mensaje de éxito y redirigir
        flash('Paciente agregado con exito', 'success')
        return redirect(url_for('create.agregar_paciente'))  # Correcto, vuelve a la misma página

    # Si el método es GET, mostrar el formulario para agregar venta
    return render_template('crearinformacion/pacientes.html')



