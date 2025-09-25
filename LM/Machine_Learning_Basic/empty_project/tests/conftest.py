import pytest
import json

@pytest.fixture
def check_format_logs_json():
    """
    Фикстура для проверки формата логов в JSON.
    Принимает строку с логами и ожидаемую структуру (список ключей),
    возвращает True, если формат корректен, иначе выбрасывает AssertionError.
    """
    def _check_format(logs_str: str, expected_keys: list) -> bool:
        try:
            logs = json.loads(logs_str)
        except json.JSONDecodeError as e:
            raise AssertionError(f"Логи не в формате JSON: {e}")

        if not isinstance(logs, list):
            raise AssertionError("Ожидался список логов")

        for log in logs:
            if not isinstance(log, dict):
                raise AssertionError("Каждый лог должен быть словарем")

            for key in expected_keys:
                if key not in log:
                    raise AssertionError(f"Отсутствует обязательный ключ: {key}")

        return True

    return _check_format