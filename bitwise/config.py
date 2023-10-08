import os
from collections import namedtuple
from dotenv import load_dotenv

load_dotenv()

Config = namedtuple(
    "Config",
    [
        "BOT_TOKEN",
    ],
)

config = Config(
    BOT_TOKEN=os.getenv("BOT_TOKEN"),
)
