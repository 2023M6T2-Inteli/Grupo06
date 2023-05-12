import fastapi
import uvicorn 
import pydantic

app = fastapi.FastAPI()


class Shape(pydantic.BaseModel):
    shape: str

class Position(pydantic.BaseModel):
    x: float
    y: float

shape = Shape(shape='')
point = Position(x=0.0, y=0.0)

@app.get("/shape")
def get_shape():
    global shape
    past_shape = shape
    shape = Shape(shape='')
    return past_shape

@app.post("/shape")
def set_shape(_shape: Shape):
    global shape
    shape = _shape

if __name__ == "__main__":
    uvicorn.run(app)