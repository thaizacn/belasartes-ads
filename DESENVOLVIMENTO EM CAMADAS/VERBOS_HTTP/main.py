from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        "titulo": "Curso - BA - ADS",
        "aulas": 10,
        "horas": 60
    },
    2: {
        "titulo": "Curso - BA - GTI",
        "aulas": 5,
        "horas": 40
    }
}

@app.get('/cursos')
async def getCursos():
    return cursos

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
