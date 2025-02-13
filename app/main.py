from fastapi import FastAPI

from app.api.v1.api import api_router
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI(docs_url=None)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI",
        swagger_css_url="https://cdn.jsdelivr.net/gh/danielperezrubio/swagger-dark-theme@main/assets/swagger-ui.min.css",
    )


app.include_router(api_router)
