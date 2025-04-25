"""
Main FastAPI application module.

This module initializes the FastAPI application and includes all routers.
"""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.api.endpoints import category, image, faq, menu_option, option, plan, type
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Include routers
app.include_router(
    category.router, prefix=f"{settings.API_V1_STR}/categories", tags=["categories"]
)
app.include_router(
    image.router, prefix=f"{settings.API_V1_STR}/images", tags=["images"]
)
app.include_router(
    faq.router, prefix=f"{settings.API_V1_STR}/faqs", tags=["faqs"]
)
app.include_router(
    menu_option.router, prefix=f"{settings.API_V1_STR}/menu-options", tags=["menu-options"]
)
app.include_router(
    option.router, prefix=f"{settings.API_V1_STR}/options", tags=["options"]
)
app.include_router(
    plan.router, prefix=f"{settings.API_V1_STR}/plans", tags=["plans"]
)
app.include_router(
    type.router, prefix=f"{settings.API_V1_STR}/types", tags=["types"]
)


def custom_openapi():
    """
    Generate custom OpenAPI schema.
    
    This function customizes the OpenAPI schema for documentation.
    
    Returns:
        Dictionary containing the OpenAPI schema
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=settings.PROJECT_NAME,
        version="1.0.0",
        description="Resivate API documentation",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi 