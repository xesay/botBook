from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str 


@dataclass
class Config:
    tg_token: TgBot


def load_config(path: str):

    env = Env()
    env.read_env(path)

    return Config(tg_token=TgBot(token=env('TOKEN')))

