#!/usr/bin/python3

# -------------------------------------------
# Chargement des dépendances
# -------------------------------------------
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


# -------------------------------------------
# Connexion en SQLite au fichier chinook.db
# -------------------------------------------
db_connect = create_engine('sqlite:///chinook.db')

# -------------------------------------------
# Lancement d'une application Flask
# -------------------------------------------
app = Flask(__name__)

# -------------------------------------------
# Lancement d'une API
# -------------------------------------------
api = Api(app)


# -------------------------------------------
# Définition de la classe Employees
# -------------------------------------------
class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
    
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        ReportsTo = request.json['ReportsTo']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Fax = request.json['Fax']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}')".format(LastName,FirstName,Title,
                             ReportsTo, BirthDate, HireDate, Address,
                             City, State, Country, PostalCode, Phone, Fax,
                             Email))
        return {'status':'success'}


# -------------------------------------------
# Définition de la classe Tracks
# -------------------------------------------
class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


# -------------------------------------------
# Définition de la classe Employees_Name
# -------------------------------------------   
class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


# -------------------------------------------
# Définition de la classe artists
# -------------------------------------------
class Artists(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from artists;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


# -------------------------------------------
# Création des routes
# -------------------------------------------
api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
api.add_resource(Artists, '/artists') # Route_4


if __name__ == '__main__':
    app.run()
