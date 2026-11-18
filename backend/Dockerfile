FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Указываем uv хранить загруженный Python и кэш в общей папке, доступной всем пользователям
ENV UV_PYTHON_INSTALL_DIR=/opt/uv/python
ENV UV_CACHE_DIR=/opt/uv/cache

RUN useradd -m -u 1000 appuser
WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY src ./src

# Устанавливаем зависимости и сам пакет
RUN uv sync --frozen --no-dev

# Выдаем права пользователю appuser на приложение и на папку uv
RUN chown -R appuser:appuser /app /opt/uv

USER appuser

# Запускаем uvicorn напрямую из созданного виртуального окружения (без лишней обертки uv run)
CMD [".venv/bin/uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
