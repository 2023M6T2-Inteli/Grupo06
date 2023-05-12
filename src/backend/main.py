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

is_shape = False

@app.get("/mission")
def get_mission():
    global is_shape
    if(is_shape):
        global shape
        past_shape = shape
        shape = Shape(shape='')
        return past_shape
    else:
        is_shape = True
        global point
        return point


@app.post("/shape")
def set_shape(_shape: Shape):
    global is_shape
    is_shape = True
    global shape
    shape = _shape

@app.post("/position")
def set_position(_position: Position):
    global is_shape
    is_shape = False
    global point
    point = _position

if __name__ == "__main__":
    uvicorn.run(app)