from flask import Flask
from flask import request
from flask import Response


app = Flask(__name__)

@app.route('/hello/', methods = ['GET'])
def hello_world():
	na = request.args.get('name','')
	age = request.args.get('age','')
	address = request.args.get('address','')
	phone = request.args.get('phone','')
	
        return na + " " +age+ " " +address+ " " +phone


if __name__ == '__main__':
    app.run() 
    
