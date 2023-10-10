import os
from collections import namedtuple
from dotenv import load_dotenv

load_dotenv()

configTuple = namedtuple(
    "Config",
    [
        "BOT_TOKEN",
    ],
)

Config = configTuple(
    BOT_TOKEN=os.getenv("BOT_TOKEN"),
)
