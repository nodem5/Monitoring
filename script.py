from fastapi import FastAPI
import socket

app = FastAPI()


# Endpoint "health" zwracający status 200
@app.get("/health")
async def health():
    return {"status": "ok"}


# Endpoint "get-hostname" zwracający nazwę hosta
@app.get("/get-hostname")
async def get_hostname():
    hostname = socket.gethostname()
    return {"hostname": hostname}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
