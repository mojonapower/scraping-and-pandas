from flask import Flask, request, jsonify
from scraping import moreexchange
from scraping import cambiossuiza

app = Flask(__name__)
from flask_cors import CORS

# Allow CORS requests to this API
CORS(app)

@app.route("/", methods=['GET'])
def scrap():
    more=moreexchange()
    return jsonify({
        "moreexchange": str(more),
        "casa1": "another value"
  })
@app.route("/casa2", methods=['GET'])
def scrap2():
    cambios=cambiossuiza()
    return jsonify({
        "cambiossuiza": str(cambios),
        "casa2": "another value"
    })

app.run(host='0.0.0.0', port='3000', debug=True)