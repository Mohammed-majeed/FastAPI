from fastapi import FastAPI
from .database import Base, engine
from .routers import posts,users,auth
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "hello world"}

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(posts.router)

