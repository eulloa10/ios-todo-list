from flask import Blueprint, request 

from .extensions import mongo 

from bson.json_util import dumps

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def hello():
  return 'hello nalgas'
  
 
#GET ALL LISTS
@main.route("/lists", methods=['GET'])
def getLists():
  user_list = mongo.db.nalgaslist
  result = user_list.find()

  return dumps(result)

#GET LIST BY NAME
@main.route("/list/<name>", methods=['GET'])
def getListByName(name):
  query = request.json['q']

  user_list = mongo.db.nalgaslist
  result = user_list.find(query)

  return dumps(result)

#POST NEW LIST
@main.route("/create-list", methods=['POST'])
def postNewList():
  list_name = request.json["name"]
  list_items = request.json["items"]

  user_list = mongo.db.nalgaslist
  user_list.insert({"name" : list_name, "items" : list_items})
  return '<h1>Added a List!</h1>'
  
#POST UPDATED LIST
@main.route("/list/<name>", methods=['POST'])
def postUpdatedList(name):
  query = request.json["q"]
  list_items = request.json["items"]

  user_list = mongo.db.nalgaslist
  result = user_list.find(query)

  result.insert({"items" : list_items})

  return dumps(result)

#DELETE LIST
@main.route("/list/<type>", methods=['DELETE'])
def deleteUpdatedList(type):
  user_list = mongo.db.nalgaslist
  result = user_list.delete_many({'type':'grocery'})

  return 'List deleted'
