import logging
import logging.handlers

__all__ = ["logger"]


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            with open(".log", "w"):
                pass

            cls._instance = super(Logger, cls).__new__(cls)

            cls._instance.logger = logging.getLogger("discord")
            cls._instance.logger.setLevel(logging.INFO)

            cls._instance.file_handler = logging.handlers.RotatingFileHandler(
                filename=".log",
                encoding="utf-8",
                maxBytes=32 * 1024 * 1024,
                backupCount=5,
            )

            cls._instance.console_handler = logging.StreamHandler()

            cls._instance.dt_fmt = "%Y-%m-%d %H:%M:%S"
            cls._instance.formatter = logging.Formatter(
                "[{asctime}] [{levelname:<8}] {name}: {message}",
                cls._instance.dt_fmt,
                style="{",
            )

            cls._instance.file_handler.setFormatter(cls._instance.formatter)
            cls._instance.console_handler.setFormatter(cls._instance.formatter)

            cls._instance.logger.addHandler(cls._instance.file_handler)
            cls._instance.logger.addHandler(cls._instance.console_handler)

            return cls._instance

    def __init__(self) -> None:
        pass

    def info(self, message: str):
        self.logger.info(message)


logger = Logger()
