from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from fastapi.openapi.docs import get_swagger_ui_html
from app.core.config import settings


app = FastAPI(docs_url=None, title=settings.TITLE)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI",
        swagger_css_url="https://cdn.jsdelivr.net/gh/danielperezrubio/swagger-dark-theme@main/assets/swagger-ui.min.css",
    )


app.include_router(api_router, prefix="/api")
