import os
from collections import namedtuple
from dotenv import load_dotenv

load_dotenv()

configTuple = namedtuple(
    "Config",
    [
        "BOT_TOKEN",
        "APP_ID",
    ],
)

Config = configTuple(
    BOT_TOKEN=os.getenv("BOT_TOKEN"),
    APP_ID=os.getenv("APP_ID"),
)
