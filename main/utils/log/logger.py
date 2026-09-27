import os
from datetime import datetime
from typing import ClassVar


class Logger:
    _logs: ClassVar[list] = []
    _error_logs: ClassVar[list] = []

    @classmethod
    def log(cls, step: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        decoded_step = cls._safe_decode(step)
        print(f"\n{decoded_step}")
        cls._logs.append((timestamp, decoded_step))

    @classmethod
    def error(cls, step: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        decoded_step = cls._safe_decode(step)
        print(f"\n{decoded_step}")
        cls._error_logs.append((timestamp, decoded_step))

    @classmethod
    def log_to_file(cls, filename: str | None = None):
        if filename is None:
            filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../artifacts/log.txt"))

        if cls._logs:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "a", encoding="utf-8") as file:
                for timestamp, message in cls._logs:
                    file.write(f"{timestamp}  {message}\n")

    @classmethod
    def error_log_to_file(cls, filename: str | None = None):
        if filename is None:
            filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../artifacts/error_log.txt"))

        if cls._error_logs:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "a", encoding="utf-8") as file:
                for timestamp, message in cls._error_logs:
                    file.write(f"{timestamp}  {message}\n")

    @staticmethod
    def _safe_decode(text: str) -> str:
        if "\\u" in text:
            try:
                return text.encode("utf-8").decode("unicode_escape")
            except Exception:
                return text
        return text
