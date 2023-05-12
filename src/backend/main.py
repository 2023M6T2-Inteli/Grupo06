import fastapi
import uvicorn 

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"shape": "square"}

if __name__ == "__main__":
    uvicorn.run(app)