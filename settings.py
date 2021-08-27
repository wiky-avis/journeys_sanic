import os

from environs import Env

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


DB_HOST = env.str('DB_HOST', default='localhost')
DB_PORT = env.int('DB_PORT', default=5433)
DB_NAME = env.str('DB_NAME', default='example')
DB_USER = env.str('DB_USER', default='example')
DB_PASSWORD = env.str('DB_PASSWORD', default='example')
