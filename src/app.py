from flask import Flask, render_template, request, jsonify, Response


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventario')
def inventario():
    return render_template('inventario.html')

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
