from flask import Flask

app = Flask(__name__)

# Criação de Rota
@app.route("/")
def teste():
    return "<h1>Hello World</h1>"

@app.route("/about")
def about():
    return "<h1>Página SOBRE</h1>"

if __name__=="__main__":
    app.run(debug=True)
