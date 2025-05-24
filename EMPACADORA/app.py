from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
from collections import Counter
from model import Cliente
from estructuras import Producto, ColaEmpaque, ProductoDevuelto

app = Flask(__name__)
app.secret_key = "clave-secreta-cambiame"

clientes = []
cola_empaque = ColaEmpaque()
productos_devueltos = []

usuarios = {
    "admin": "1234",
    "Santiago": "pass1"
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        clave = request.form["clave"]
        if usuario in usuarios and usuarios[usuario] == clave:
            session["usuario"] = usuario
            return redirect(url_for("index"))
        else:
            return "Usuario o clave incorrectos", 401
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

@app.route("/")
@login_required
def index():
    return render_template("index.html", clientes=clientes)

@app.route("/nuevo_pedido", methods=["GET", "POST"])
@login_required
def nuevo_pedido():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        nombres = request.form.getlist("producto[]")
        pesos = request.form.getlist("peso[]")
        categorias = request.form.getlist("categoria[]")

        cliente = Cliente(nombre, correo)
        productos = []

        for i in range(len(nombres)):
            p = Producto(nombres[i], float(pesos[i]), categorias[i])
            productos.append(p)
            cola_empaque.encolar(p)

        cliente.agregar_pedido(productos)
        clientes.append(cliente)

        return redirect(url_for("index"))

    return render_template("pedido.html")

@app.route("/ver_empaque")
@login_required
def ver_empaque():
    productos = cola_empaque.obtener_productos()
    return render_template("empaque.html", productos=productos, productos_devueltos=productos_devueltos)

@app.route("/empacar", methods=["POST"])
@login_required
def empacar():
    producto = cola_empaque.desencolar()
    return redirect(url_for("ver_empaque"))

@app.route("/devolver/<nombre>", methods=["GET", "POST"])
@login_required
def devolver(nombre):
    if request.method == "POST":
        razon = request.form.get("razon")
        producto = cola_empaque.eliminar_producto(nombre)
        if producto:
            productos_devueltos.append(ProductoDevuelto(producto, razon))
        return redirect(url_for("ver_empaque"))
    else:
        return render_template("devolver.html", nombre=nombre)

@app.route("/historial/<correo>")
@login_required
def historial(correo):
    cliente = next((c for c in clientes if c.correo == correo), None)
    if cliente:
        historial = cliente.obtener_historial()
        sugerencias = cliente.sugerir_categorias()
        return render_template("historial.html", cliente=cliente, historial=historial, sugerencias=sugerencias)
    else:
        return "Cliente no encontrado", 404

@app.route("/graficos")
@login_required
def graficos():
    return render_template("graficos.html")

@app.route("/datos_grafico")
@login_required
def datos_grafico():
    categorias = []
    for cliente in clientes:
        for pedido in cliente.pedidos:
            for producto in pedido:
                categorias.append(producto.categoria)
    contador = Counter(categorias)
    data = {
        "categorias": list(contador.keys()),
        "frecuencias": list(contador.values())
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
