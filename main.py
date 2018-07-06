from flask import Flask
from flask import request
import json
from flask import Response


app = Flask(__name__)


@app.route('/hello/', methods = ['GET'])
def hello_world():
	input1 =int(request.args.get("val1"))
	input2 =int(request.args.get("val2")) 	
	result = {
		"input1" : input1,
		"input2" : input2,
		"result" : input1 + input2
	}	 
    	return Response(json.dumps(result), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run()
'''
?val1=2&val2=5
{
	"val1" : "4",
	"val2" : "5"
}
'''
