from fastapi import FastAPI

app = FastAPI(
    title="My First AWS FastAPI",
    version="1.0.0"
)


@app.get("/home")
def home():
    return {
        "message": "Hello from FastAPI on AWSvinay!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/hello/{name}")
def hello(name: str):
    print(f"Hello>>>>>>>>>>>>>>> {name}")
    return {
        "message": f"Hello VINNAAAA-Test, {name}!"
    }