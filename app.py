
from flask import Flask, render_template, url_for

app = Flask(__name__)

class Produto:
    def __init__(self, id, nome, preco, categoria, imagem):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.imagem = imagem

produtos = [
    Produto(1, "Vestido Floral", 129.90, "Vestidos", "vestido.jpg"),
    Produto(2, "Camisa Social", 89.90, "Camisas", "camisa.jpg"),
    Produto(3, "Calça Jeans", 149.90, "Calças", "calca.jpg"),
    Produto(4, "Blusa de Seda", 99.90, "Blusas", "blusa.jpg"),
]

@app.route("/")
def home():
    return render_template("index.html", produtos=produtos)

@app.route("/categoria/<nome>")
def categoria(nome):
    filtrados = [p for p in produtos if p.categoria == nome]
    return render_template("index.html", produtos=filtrados)

if __name__ == "__main__":
    app.run(debug=True)
