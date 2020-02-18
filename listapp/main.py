from flask import Blueprint, request 

from .extensions import mongo 

from bson.json_util import dumps

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def hello():
  return '<h1>HELLO NALGAS</h1>'
  
 
#GET ALL LISTS
@main.route("/lists", methods=['GET'])
def getLists():
  user_list = mongo.db.nalgaslist
  result = user_list.find()

  return dumps(result)

#GET LIST BY NAME
@main.route("/list", methods=['GET'])
def getListByName():
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
  return f"Added a new list: '{list_name}'"
  
#POST UPDATED LIST
@main.route("/list", methods=['POST'])
def postUpdatedList():
  list_to_update = request.json["name"]
  items_to_update = request.json["items"]
  
  user_list = mongo.db.nalgaslist
  result = user_list.update_one({"name": list_to_update}, {"$set": {"items": items_to_update}})

  return f"List '{list_to_update}' updated"

#DELETE LIST
@main.route("/list", methods=['DELETE'])
def deleteUpdatedList():
  list_to_delete = request.json["name"]

  user_list = mongo.db.nalgaslist
  result = user_list.delete_one({"name" : list_to_delete})

  return f"List '{list_to_delete}' deleted"
