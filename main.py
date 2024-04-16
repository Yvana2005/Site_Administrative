from fastapi import FastAPI
import api
import uvicorn


app = FastAPI()

@app.get("/home")
async def read_root():
    return {"Hello": "World"}

@app.get("/component/{component_id}")#path parameter
async def get_component(component_id: int):
    #operations
    return {"component_id" : component_id}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)