from fastapi import FastAPI

from src.routers import auth, validation

app = FastAPI()

app.include_router(validation.router)
app.include_router(auth.router)


@app.get('/')
async def root():
    return {'message': 'Validador de Senha'}
