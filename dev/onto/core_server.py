from flask import Flask
from flask import request
from flask.ext.cors import CORS, cross_origin
import json
import requests
import ieparser

def CoreNLP(txt):
    r = requests.post("http://localhost:9000/?properties={%22outputFormat%22%3A%22json%22}", data=txt)
    return r.text

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route('/',methods=['POST','GET'])
@cross_origin()
def CoreNLPConnector():
    if request.method == 'POST':
        if len(request.data) > 0:
            data = json.loads(request.data)
        else:
            data = request.form
        text = data['text']
        cnlp = json.loads(CoreNLP(text))
        res  = ieparser.read(cnlp)
        return json.dumps({"ok":True,"text":text,"structure":res})
    else:
        return json.dumps({"ok":False})

#curl -H "Content-Type: application/json" -X POST -d '{"text":"Cook is holding knife."}' http://localhost:5000
