
# Ju Modas - Loja de Roupas

Este é um site e-commerce básico para a loja Ju Modas, desenvolvido com Flask.

## Como executar

1. Instale o Flask:
   pip install flask

2. Execute o site:
   python app.py

3. Acesse no navegador:
   http://127.0.0.1:5000

## Como adicionar ou editar fotos dos produtos

- Coloque as imagens na pasta `static/images/`.
- Atualize o nome da imagem no código `app.py` na propriedade `imagem` de cada produto.
- As imagens devem estar em formato JPG ou PNG.

## Estrutura

- `app.py`: código principal do site.
- `templates/index.html`: layout HTML.
- `static/images/`: imagens dos produtos.
