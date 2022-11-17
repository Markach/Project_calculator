from loguru import logger

logger.add('debug.json', format='{time} {level} {message}', level='DEBUG', serialize=True) 