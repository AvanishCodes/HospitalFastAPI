
# --- Base image: only production dependencies ---
FROM python:3.13-slim AS base
WORKDIR /app
RUN pip install pipx && pipx install poetry
ENV PATH="/root/.local/bin:$PATH"
COPY pyproject.toml poetry.lock poetry.toml README.md /app/
RUN poetry config virtualenvs.in-project true \
    && poetry install --no-interaction --no-ansi --only main \
    && ls -l /app/.venv/bin \
    && cat /app/.venv/pyvenv.cfg

# --- Migrations image: install dev dependencies and run alembic ---
FROM base AS migrations
WORKDIR /app
COPY . /app/
RUN .venv/bin/pip install pipx && pipx install poetry \
    && .venv/bin/poetry install --with dev --no-interaction --no-ansi
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000
ENTRYPOINT ["/app/.venv/bin/alembic"]
CMD ["upgrade", "head"]

# --- Run image: start the server ---
FROM base AS run
WORKDIR /app
COPY . /app/
# Ensure the .venv from base is present after copying source
COPY --from=base /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000
CMD [".venv/bin/uvicorn", "hospital:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-dir", "hospital"]