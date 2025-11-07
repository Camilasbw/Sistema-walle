from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='templates/static')

@app.route('/', methods=['GET'])
def index():
    
    return render_template('index.html')


@app.route('/cadastro_produto', methods=['GET'])
def cadastro_produto():
    return render_template('cadastro_produto.html')

@app.route('/entrada_produto', methods=['GET'])
def entrada_produto():
    return render_template('entrada_produto.html')


@app.route('/saida_produto', methods=['GET'])
def saida_produto():
    return render_template('saida_produto.html')


@app.route('/relatorios', methods=['GET'])
def relatorios():
    return render_template('relatorios.html')


if __name__ == '__main__':
    app.run(debug=True, port='5001')
