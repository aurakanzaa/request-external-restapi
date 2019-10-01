from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Pegawai(db.Model):
    __tablename__ = 'pegawai'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    alamat = db.Column(db.String(150), nullable=False)

    def __init__(self, name,alamat):
        self.name = name
        self.alamat = alamat

class PegawaiSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    alamat = fields.String(required=True)