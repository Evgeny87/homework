from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from starlette import status
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def hello(name: str = "OTUS"):
    return {
        "message": f"Hello {name}!",
    }


@app.get("/ping", status_code=200)
def ping_view():
    return {"message": "pong"}


# @app.get("{url_path:path}")
# def all_others(
#         url_path: str,
# ):
#     return {"request to": url_path}


@app.exception_handler(StarletteHTTPException)
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return await http_exception_handler(request, exc)


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def custom_404_handler(request, exception):
    if (isinstance(exception, StarletteHTTPException)
            and exception.detail != "Not Found"):
        return await http_exception_handler(request, exception)
    return JSONResponse(
        {
            "request_url": request.url.path,
            "exception": str(exception),
        },
        status_code=status.HTTP_404_NOT_FOUND
    )
