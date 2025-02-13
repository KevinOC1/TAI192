from fastapi import FastAPI


app = FastAPI(
    title="Mi Primer API 192",
    description="Kevin Ordaz",
    version="1.0.1",
)
# Endpoint home
@app.get("/", tags=["Hola Mundo"])
def home():
    return {"hello": "world FastAPI"}
