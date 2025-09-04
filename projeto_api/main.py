from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from models import create_db_and_tables
from schemas import schema
from db_func import router as rest_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
create_db_and_tables()

# REST endpoints
app.include_router(rest_router)

# GraphQL endpoint
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Serve arquivos estáticos (incluindo index.html)
app.mount("/", StaticFiles(directory=".", html=True), name="static")


