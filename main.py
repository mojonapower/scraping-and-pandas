from flask import Flask, request, jsonify
from scraping import moreexchange
app = Flask(__name__)
from flask_cors import CORS

# Allow CORS requests to this API
CORS(app)

@app.route("/", methods=['GET'])
def scrap():
    more=moreexchange()
    return jsonify({
        "moreexchange": str(more),
        "casa2": "another value"
    })


app.run(host='0.0.0.0', port='3000', debug=True)
