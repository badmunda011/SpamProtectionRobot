from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    True  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = "7862520336:AAEwDMrSbXTEBF8Hye1Ud32O4E9BgIBMh_I"
    SUDOERS = [7009601543]
    NSFW_LOG_CHANNEL = -1002356967761
    SPAM_LOG_CHANNEL = -1002356967761
    ARQ_API_KEY = "VCENSC-TWKMPQ-GKBLDI-HNTTKQ-ARQ"  
else:
    BOT_TOKEN = env.get("BOT_TOKEN")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL"))
    ARQ_API_KEY = env.get("ARQ_API_KEY")
