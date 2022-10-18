from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import logging
import base64
import crud
import apicall

app = FastAPI()

app.add_middleware(
      CORSMiddleware,
      #allow_origins = ['http://localhost:5173','http://ec2-13-114-29-191.ap-northeast-1.compute.amazonaws.com:5173','http://172.20.0.2:5173/'],
      allow_origins = ["*"],
      allow_methods = ["*"],
      allow_headers = ["*"]
  )

class SchemaOfSMRequest(BaseModel):
    Image: bytes

class SchemaOfSMResponce(BaseModel):
    result : str
    
@app.get('/helloworld')
def get_hello_message():
    return {"message": "Hello World!!"}

@app.post('/api/sm', response_model=SchemaOfSMResponce)
def derive_score(request_body: SchemaOfSMRequest):
    # 辞書形式に変更
    _dict = request_body.__dict__   
    sm_detected = apicall.callsm(_dict["Image"])
    ans = crud.get_trashid(sm_detected)
    return {'result': ans}
