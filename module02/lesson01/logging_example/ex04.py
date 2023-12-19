import logging
from logging.handlers import RotatingFileHandler

# Встановіть базовий рівень логування
logging.basicConfig(level=logging.INFO)

# Створіть обробник, який записує логи у файл, обмежений розміром (наприклад, 5MB) і зберігає 3 резервних копії
handler = RotatingFileHandler(
    "my_log.log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
)

# Додайте обробник до основного логера
logger = logging.getLogger()
logger.addHandler(handler)

# Тестуємо логування
logger.info("Це інформаційне повідомлення")
logger.error("Це повідомлення про помилку")
