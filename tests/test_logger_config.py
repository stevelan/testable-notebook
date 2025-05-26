import logger_config

logger = logger_config.get_logger(__name__)

def test_logging():
    logger.warning("Is logging working?")