"""coding=utf-8."""

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.router_rest import router as router_rest

router = APIRouter(prefix='/api')
router.include_router(router_rest)

app = FastAPI(debug=True)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
