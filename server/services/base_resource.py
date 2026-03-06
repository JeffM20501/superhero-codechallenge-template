from flask_restful import Resource
from models import db
from flask import request, make_response


class AllResource(Resource):
    def __init__(self, model, resource_name='', fields=[]):
        super().__init__()
        self.Model=model
        self.resource_name=resource_name
        self.fields=fields
        
    def get(self):
        queries=self.Model.query.all()
        query_dict=[q.to_dict(rules=self.fields) for q in queries]
        
        return make_response(query_dict,200)
    
    def post(self):
        item=self.Model()
        try:
            for field, value in request.json.items():
                setattr(item,field, value)
            db.session.add(item)
            db.session.commit()
            return make_response(item.to_dict(rules=self.fields),200)
        except Exception as e:
            return {'errors': ['validation errors']}, 400
    

class SingleResource(Resource):
    def __init__(self, model, resource_name='', fields=[]):
        super().__init__()
        self.Model=model
        self.resource_name=resource_name
        self.fields=fields
        
    def get(self,id):
        item = self.Model.query.filter_by(id=id).first()
        
        if item==None:
            return {'error': f'{self.resource_name} not found'}, 404
        
        return make_response(item.to_dict(rules=self.fields), 200)
    
    def patch(self,id):
        item=self.Model.query.filter_by(id=id).first()
        if item ==None:
            return {"error": f"{self.resource_name} not found"}, 404
        
        for field,value in request.json.items():
            if hasattr(item, field):
                try:
                    setattr(item,field, value)
                    db.session.commit()
                    return make_response(item.to_dict(),200)
                except Exception as e:
                    return {'errors': ['validation errors']}, 400
    