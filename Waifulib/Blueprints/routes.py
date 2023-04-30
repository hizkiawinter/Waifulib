from flask import Blueprint, request, jsonify
from database import waifu_schema,waifus_schema, Waifu, db 
from Waifulib.Blueprints.errors import *

api = Blueprint('api', __name__)


@api.route('/' , methods=['GET'])
def home():
    return jsonify({'messages' : "You are connected to Waifulib API"})

@api.route('/waifus', methods=['POST'])
def add_waifu(): 
    name = request.json['name']
    description = request.json['description']
    new_waifu = Waifu(name, description)
    db.session.add(new_waifu)
    db.session.commit()
    return jsonify({
        'data' : waifu_schema.dump(new_waifu), 
        'message' : 'Waifu berhasil ditambahkan'
    }), 200
      

@api.route('/waifus', methods=['GET'])
def get_waifu():
    all_waifus = Waifu.query.all()
    result = waifus_schema.dump(all_waifus)
    return jsonify({
        'data' : result, 
    }), 200

@api.route('/waifus/<id>', methods = ['GET'])
def get_singlewaifu(id):
    product = Waifu.query.get(id)
    if(product):     
        return jsonify({
            'data' : waifu_schema.dump(product)
        })
    else:
        return response('404 Not Found'), 404

@api.route('/waifus/<id>', methods=['PUT'])
def update_waifu(id):
    product = Waifu.query.get(id)
    if(product):
        product.name = request.json['name']
        product.description = request.json['description']
        db.session.commit()
        return jsonify({
            'data' : waifu_schema.dump(product), 
            'message' : 'Waifu berhasil diupdate'
        })
    else:
        return response('404 Not Found'), 404

@api.route('/waifus/<id>', methods=['Delete'])
def delete_waifu(id):
    product = Waifu.query.get(id)
    if(product):
        db.session.delete(product)
        db.session.commit()
        return jsonify({
            'data' : waifu_schema.dump(product), 
            'message' : 'Waifu berhasil dihapus'
        })
    else:
        return response('404 Not Found'), 404
