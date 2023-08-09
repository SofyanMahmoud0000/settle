import sys
from os.path import dirname
import json

sys.path.insert(1, dirname(dirname(dirname(dirname('.')))))

from src.response.Response import Response

import unittest
from src.config import app

class ResponseTest(unittest.TestCase):
  
  def test_ok_1(self):
    data = {
      "key": "vaule"
    }
    
    with app.app_context():
      actualResult = json.loads(Response.ok(data).data.decode("utf-8"))
      expectedResult = {
        'items': [
          {'key': 'vaule'}
        ],
        'pageNo': 1,
        'pageSize': 1,
        'success': True,
        'totalPages': 1
      }
      self.assertDictEqual(actualResult, expectedResult)
      
  def test_ok_2(self):
    data = [
      {
        "objectNo": "One"  
      },
      {
        "objectNo": "Two"
      }
    ]
    
    with app.app_context():
      actualResult = json.loads(Response.ok(data).data.decode("utf-8"))
      expectedResult = {
        'items': [
          {'objectNo': 'One'},
          {'objectNo': 'Two'},
        ],
        'pageNo': 1,
        'pageSize': 2,
        'success': True,
        'totalPages': 1
      }
      self.assertDictEqual(actualResult, expectedResult)
      
  def test_ok_3(self):
    data = None
    
    with app.app_context():
      actualResult = json.loads(Response.ok(data).data.decode("utf-8"))
      expectedResult = {
        'success': True,
      }
      self.assertDictEqual(actualResult, expectedResult)
    
if __name__ == "__main__":
  unittest.main()  
  