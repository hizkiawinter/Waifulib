from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Waifu db model
class Waifu(db.Model):
  # fields
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  description = db.Column(db.String(200))
  # constructor
  def __init__(self, name, description):
    self.name = name
    self.description = description
# Waifu Schema
class WaifuSchema(ma.Schema):
  # fields control
  class Meta:
    fields = ('id', 'name', 'description')

# init schema
waifu_schema = WaifuSchema()
waifus_schema = WaifuSchema(many=True)