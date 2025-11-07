from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='templates/static')

@app.route('/', methods=['GET'])
def index():
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port='5001')
