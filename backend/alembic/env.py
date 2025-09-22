from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

from app.db.database import Base
from app.core.config import Settings

# importacion de los modelos para que base.metadata los registre

from app.modules.Role.Models import Rol
from app.modules.User.Models import Usuario

# 🔹 Importar todos los modelos (esto es lo que activa las tablas en Base.metadata)

# Configuración Alembic
config = context.config
fileConfig(config.config_file_name)  # pyright: ignore[reportArgumentType]

# Usa tu Settings para la URL
settings = Settings()
config.set_main_option("sqlalchemy.url", settings.database_url)

# 🔹 Esto es lo que Alembic necesita
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
