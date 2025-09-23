from fastapi import APIRouter, HTTPException
from loguru import logger



error_router = APIRouter()

@error_router.get("/error")
def error():
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")