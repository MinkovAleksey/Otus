import pytest

def test_logs_format(check_format_logs_json):
    logs_str = '''
    [
        {"timestamp": "2025-09-24T12:00:00", "level": "INFO", "message": "Test log"},
        {"timestamp": "2025-09-24T12:01:00", "level": "ERROR", "message": "Another log"}
    ]
    '''
    expected_keys = ["timestamp", "level", "message"]
    assert check_format_logs_json(logs_str, expected_keys)

if __name__ == '__main__':
    pytest.main()