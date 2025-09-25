import logging
import json
from datetime import datetime
import sys

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.now().isoformat(),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }
        # Добавляем дополнительные поля из extra
        if hasattr(record, 'user'):
            log_record['user'] = record.user
        if hasattr(record, 'action'):
            log_record['action'] = record.action
        if hasattr(record, 'error_code'):
            log_record['error_code'] = record.error_code
        return json.dumps(log_record, ensure_ascii=False)

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Хендлер для консоли
console_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(f'app.log', mode='a', encoding='utf-8')

# Применяем кастомный форматтер
formatter = JSONFormatter()
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)