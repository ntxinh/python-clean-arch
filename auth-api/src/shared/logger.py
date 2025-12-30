import sys
from loguru import logger
from src.config import settings

def setup_logging():
    # Remove default handler
    logger.remove()
    
    # Add Console Handler
    logger.add(
        sys.stderr, 
        level=settings.LOG_LEVEL, 
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )
    
    # Add File Handler (Daily Rotation)
    logger.add(
        "logs/app_{time:YYYY-MM-DD}.log",
        rotation="00:00",  # New file every midnight
        retention="14 days", # Keep logs for 2 weeks
        level=settings.LOG_LEVEL,
        compression="zip"
    )

    logger.info("Logging initialized")