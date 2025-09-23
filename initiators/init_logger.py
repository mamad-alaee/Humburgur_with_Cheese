from loguru import logger


def init_logger():
    logger.add("logs/info.log",
                rotation="1 day",
                level="INFO",
                filter=lambda record: record["level"].name == "INFO")
    logger.add("logs/error.log",
                rotation="1 week",
                level="ERROR",
                filter=lambda record: record["level"].name == "ERROR")