from . import *

class Response:
  def __init__(self, totalCount = 1, pageNo = 1, pageSize = 1, data = None, message = None):
    if(data is not None):
      self.items = data if type(data) is list else [data]
      self.pageSize = len(self.items)
      self.totalPages = math.ceil(totalCount / pageSize)
      self.pageNo = pageNo
    if(message is not None):
      self.message = message
      
    self.success = None
  
  @staticmethod
  def ok(data, totalCount = 1, pageNo = 1, pageSize = 1):
    obj = Response(data=data, totalCount=totalCount, pageNo=pageNo, pageSize=pageSize)
    obj.success = True
    return make_response(jsonify(obj.__dict__), 200, {'Content-Type': 'application/json'})
    
  @staticmethod
  def created(data):
    obj = Response(data=data)
    obj.success = True
    return make_response(jsonify(result = obj.__dict__.pop('message')), 201, {'Content-Type': 'application/json'})
    
    
  @staticmethod
  def updated(data):
    obj = Response(data=data)
    obj.success = True
    return make_response(jsonify(result = obj.__dict__.pop('message')), 201, {'Content-Type': 'application/json'})
    
  @staticmethod
  def fail(message):
    obj = Response(message=message)
    obj.success = True
    return make_response(jsonify(result = obj.__dict__.pop('data')), 400, {'Content-Type': 'application/json'})