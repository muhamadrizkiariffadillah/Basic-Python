import http

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/test")
def test_endpoint():
    return "test endpoint"


@app.get("/text", response_class=PlainTextResponse)
def plain_response():
    return "Hello this is text"


@app.get("/json",response_class=JSONResponse)
def json_response():
    return dict({
        "meta": {
            "status": http.HTTPStatus.OK,
            "message": "Success"
        },
    })
