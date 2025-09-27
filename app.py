
from flask import Flask, render_template

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Vestido Floral", "preco": 129.90, "categoria": "Vestidos", "imagem": "image.png"},
    {"id": 2, "nome": "Camisa Social", "preco": 89.90, "categoria": "Camisas", "imagem": "image.png"},
    {"id": 3, "nome": "Calça Jeans", "preco": 149.90, "categoria": "Calças", "imagem": "image.png"},
    {"id": 4, "nome": "Blusa de Seda", "preco": 99.90, "categoria": "Blusas", "imagem": "image.png"},
]

@app.route("/")
def home():
    return render_template("index.html", produtos=produtos)

@app.route("/categoria/<nome>")
def categoria(nome):
    filtrados = [p for p in produtos if p["categoria"] == nome]
    return render_template("index.html", produtos=filtrados)

if __name__ == "__main__":
    app.run(debug=True)
