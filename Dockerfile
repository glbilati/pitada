FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /srv

COPY pyproject.toml ./
COPY app ./app
RUN pip install --no-cache-dir .

COPY alembic.ini ./
COPY migrations ./migrations
# O build do front (web/dist) entra aqui quando a Prisma definir o framework.
COPY web ./web

RUN useradd --system --uid 10001 pitada
USER pitada

# Cloud Run injeta PORT (8080 por padrao).
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
