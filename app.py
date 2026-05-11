from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Mi 2ª app Flask en Azure</h1>
    <p>Aplicación publicada con Azure App Service, GitHub y GitHub Actions.</p>
    """

@app.route("/saludo")
def saludo():
    return """
    <h1>Hola desde Flask</h1>
    <p>Esta es una segunda ruta de la aplicación.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)