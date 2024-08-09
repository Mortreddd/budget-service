from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from ..utils.token import verify_access_token

app = FastAPI()


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")[7:]

    if (token is None) or (not verify_access_token(token)):
        return JSONResponse(content={"message": "Forbidden"}, status_code=403)

    return await call_next(request)
