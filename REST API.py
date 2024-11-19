#1
# using only Flask

from flask import Flask, jsonify, request 

# creating a Flask app 
app = Flask(__name__) 

@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "I am using MY LAPTOP"
        return jsonify({'data': data}) 
    

@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 
  
    return jsonify({'data': num**2}) 
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 


#2
# Using flask-restful

from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

app = Flask(__name__) 
# creating an API object 
api = Api(app) 

class Hello(Resource): 
    def get(self): 
  
        return jsonify({'message': 'hello world'}) 
    
# another resource to calculate the square of a number 
class Square(Resource): 
  
    def get(self, num): 
  
        return jsonify({'square': num**2}) 
    

# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(Square, '/square/<int:num>') 
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 

