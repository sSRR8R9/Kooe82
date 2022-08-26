import os

ENV = bool(os.environ.get("STRING_SESSION", False))

if ENV:

elif os.path.exists("config.py"):
    from config import Development as Config  # noqa
