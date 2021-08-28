from __future__ import with_statement

import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy.engine.url import URL

from alembic import context

config = context.config

fileConfig(config.config_file_name)

import os
import sys

sys.path.append(os.getcwd())
from app import Base
from settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, compare_type=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    alembic_config = config.get_section(config.config_ini_section)
    alembic_config['sqlalchemy.url'] = URL(
        drivername='postgresql',
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )

    engine = engine_from_config(alembic_config)

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
