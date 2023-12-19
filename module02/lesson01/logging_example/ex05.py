import logging
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(
    "daily_log.log", when="midnight", interval=1, backupCount=7
)


# Встановіть базовий рівень логування
logging.basicConfig(level=logging.INFO)

# Додайте обробник до основного логера
logger = logging.getLogger()
logger.addHandler(handler)

# Тестуємо логування
logger.info("Це інформаційне повідомлення")
logger.error("Це повідомлення про помилку")
