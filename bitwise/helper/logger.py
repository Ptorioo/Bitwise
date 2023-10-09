import logging
import logging.handlers


class Logger:
    def __init__(self) -> None:
        with open(".log", "w"):
            pass

        self.logger = logging.getLogger("discord")
        self.logger.setLevel(logging.INFO)

        self.handler = logging.handlers.RotatingFileHandler(
            filename=".log",
            encoding="utf-8",
            maxBytes=32 * 1024 * 1024,
            backupCount=5,
        )

        self.dt_fmt = "%Y-%m-%d %H:%M:%S"
        self.formatter = logging.Formatter(
            "[{asctime}] [{levelname:<8}] {name}: {message}", self.dt_fmt, style="{"
        )
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
