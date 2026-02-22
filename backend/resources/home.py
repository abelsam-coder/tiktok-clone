from flask_restful import Resource
from flask import make_response,jsonify,request,render_template

class home(Resource):
       def get(self):       
              html = render_template('home.html')
              return make_response(html, 200)  