# First we start with the base python image and install uv. Then, we need to seed the SQLite database using a script. For now, we are not focused on persisting this database across container reloads. 
FROM python:3.14 AS builder
WORKDIR /app
# install uv first
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml uv.lock ./
RUN uv sync
COPY . .

# this stage requires the .env file
FROM python:3.14 AS runner
WORKDIR /app
COPY --from=builder /app /app
RUN chmod +x /app/docker-entrypoint.sh
ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT ["/app/docker-entrypoint.sh"]
