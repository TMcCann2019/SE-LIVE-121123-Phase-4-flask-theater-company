#!/usr/bin/env python3

# Serialization
# PostMan
# Set up:
# cd into server and run the following in the terminal
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5000
# flask db init
# flask db revision --autogenerate -m'Create tables'
# flask db upgrade
# python seed.py

from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import CastMember, Production, db

# 1.✅ Import Api and Resource from flask_restful
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Note: `app.json.compact = False` Configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# 2.✅ Initialize the Api
api = Api(app)

# 3.✅ Create a Production class that inherits from Resource
class Productions(Resource):
    # 4.✅ Create a GET all route
    # 4.1 Make a get method that takes self as a param
    def get(self):
        # 4.2 Create a productions array.
        # 4.3 Make a query for all productions. For every production in productions make a dictionary from the production with all of it's attributes. append the dictionary to the productions array.
        # productions_list = [{
        #     "title": production.title,
        #     "genre": production.genre,
        #     "budget": production.budget,
        #     "image": production.image,
        #     "director": production.director,
        #     "description": production.description,
        #     "ongoing": production.ongoing
        # } for production in Production.query.all()]
        
        # 10.✅ User our serializer to format our response to be cleaner
        # 10.1 Query all of the productions, convert them to a dictionary with to_dict and set them to a list.
        # 10.2 Invoke make_response, pass it the production list and a status of 200. Set make_response to a response variable.
        # 10.3 return the response variable
        # 10.4 After building the route run the server and test it in the browser
        productions_list = [production.to_dict() for production in Production.query.all()]

# 4.4 Create a response variable and set it to:
#      make_response(
#         jsonify(productions),
#         200
#     )
# 4.5 return the response
        return make_response(productions_list, 200)

# 5.✅ Serialization
# This is great, but there's a cleaner way to do this with Serialization that will allow us to easily add our associations as well.
# Navigate to models.py for Steps 6 - 9

# 11.✅ Create a POST route
# Prepare a POST request in Postman under the Body tab select form-data and fill out the body of a production request.
# Create the POST route
# 📚 Review With Students: request object
# 11.1 create a post method and pass it self.
# 11.2 create a new production from the request.form object.
# 11.3 add and commit the new production
# 11.4 convert the new production to a dictionary with to_dict
# 11.5 Set make_response to a response variable and pass it the new production and a status of 201
# 11.6 Test the route in postman
    def post(self):
        request_json = request.get_json()
        new_production = Production(
            title = request_json['title'],
            genre = request_json['genre'],
            budget = request_json['budget'],
            image = request_json['image'],
            director = request_json['director'],
            description = request_json['description'],
            ongoing = request_json['ongoing']
        )
        db.session.add(new_production)
        db.session.commit()

        return make_response(new_production.to_dict(), 201)

# 4.6 After building the route run the server and test it in the browser
# 4.7 ✅ Add the new route to our api with api.add_resource
api.add_resource(Productions, "/productions")

# 12.✅ If not done above, add the new route to our api with api.add_resource

# 13.✅ Create a GET one route
# 13.1 Build a class called ProductionByID that inherits from Resource.
class ProductionById(Resource):
# 13.2 Create a get method and pass it the id along with self. (This is how we will gain access to the id from our request)
    def get(self, id):
# 13.3 Make a query for our production by the id and build a response to send to the browser.
        production = Production.query.filter(Production.id == id).first()
        if not production:
            return make_response({"message": "Production not found"}, 404)
        return make_response(production.to_dict(), 200)
    
    def patch(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(ProductionById, "/productions/<int:id>")
# 14.✅ Add the new route to our api with api.add_resource

if __name__ == '__main__':
    app.run(port=5555, debug=True)