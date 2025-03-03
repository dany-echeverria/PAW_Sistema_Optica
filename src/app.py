from flask import Flask, render_template
import pyodbc

app = Flask(__name__)



def get_connection():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost\\SQLEXPRESS;'
                          'Database=Optica_DB;'  # Cambia el nombre a tu base de datos
                          'Trusted_Connection=yes;')
    return conn

@app.route('/')
def index():
    
    
    return render_template('index.html')

@app.route('/inventario')
def inventario():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, modelo, cantidad, materiales FROM inventario")  # Ajusta con tu tabla y columnas
    datos = cursor.fetchall()
    conn.close()
    
    return render_template('inventario.html', datos=datos)

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html')

@app.route('/remesa')
def remesa():
    return render_template('remesa.html')

@app.route('/ventas')
def ventas():
    return render_template('ventas.html')


if __name__ == '__main__':
    app.run(debug=True)
