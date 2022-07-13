from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, HTTPException
import uvicorn

from ini_load import ini_load
from core import handler
from models.models import BaseParam, RespModel



app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
print("Loading...")
ini_load()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.get('/ping')
def ping():
    return 'pong'



@app.post('/match_country', response_model=RespModel)
async def matches(baseParam:BaseParam):
    u =  handler(baseParam.iso, baseParam.countries)
    if u:
        return JSONResponse(u)
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
