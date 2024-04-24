from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/get-hostname")
async def get_hostname():
    hostname = socket.gethostname()
    return {"Nazwa Hosta": hostname}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
