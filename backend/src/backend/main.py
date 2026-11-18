from fastapi import FastAPI

app = FastAPI(
    title="Электронный лабораторный журнал (ИрИХ СО РАН)",
    version="0.1.0",
)


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "eln-backend"}
