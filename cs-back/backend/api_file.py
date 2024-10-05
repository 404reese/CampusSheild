#--- Importing the required libraries for this file
from flask import jsonify, make_response
from functools import wraps
from backend import api, jwt, cache
from backend.models import *
from flask_restful import Resource,reqparse,marshal, fields, marshal_with, abort
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
