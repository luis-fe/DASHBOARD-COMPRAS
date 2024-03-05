from flask import Flask, render_template, jsonify, request, send_from_directory
import os


app = Flask(__name__)
port = int(os.environ.get('PORT', 8001))


@app.route('/CondicaoPagamento.html')
def CondicaoPagamento():
    return render_template('CondicaoPagamento.html')

@app.route('/ConsumoCombustivel.html')
def ConsumoCombustivel():
    return render_template('ConsumoCombustivel.html')

@app.route('/CustoGeral.html')
def CustoGeral():
    return render_template('CustoGeral.html')

@app.route('/LeadTimes.html')
def LeadTimes():
    return render_template('LeadTimes.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=port)

