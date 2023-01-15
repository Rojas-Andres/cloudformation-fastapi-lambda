from fastapi import FastAPI

# from mangum import Mangum

# app = FastAPI()


# @app.get("/users")
# async def get_user():
#     print("\n\n\nentre get users->")
#     return {"message`": "Hello World!"}

# lambda_handler = Mangum(app)

def lambda_handler(event, context):
    print("entre lambda handler")
    return {"message": "Hello World!"}