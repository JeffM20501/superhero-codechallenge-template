from flask import Blueprint
from flask_restful import Api
from models import *
from services.base_resource import *

api_pb=Blueprint('api_bp', __name__)
api_v1=Api(api_pb)


#--------- Hero ---------

api_v1.add_resource(
    AllResource,
    '/heroes',
    endpoint='/heroes',
    resource_class_args=(Hero, 'Hero', ['-hero_powers'])
)

api_v1.add_resource(
    SingleResource,
    '/heroes/<int:id>',
    endpoint='/heroes/<int:id>',
    resource_class_args=(Hero, 'Hero', ['hero_powers'])
)

# ---------- Power ---------

api_v1.add_resource(
    AllResource,
    '/powers',
    endpoint='/powers',
    resource_class_args=(Power, 'Power', ['-hero_powers'])
)

api_v1.add_resource(
    SingleResource,
    '/powers/<int:id>',
    endpoint='/powers/<int:id>',
    resource_class_args=(Power, 'Power', ['-hero_powers'])
)


# ---------- HeroPower -------------

api_v1.add_resource(
    AllResource,
    '/hero_powers',
    endpoint='/hero_powers',
    resource_class_args=(HeroPower, 'HeroPower', ['hero', 'power'])
)

