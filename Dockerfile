# =========================
# Stage 1: Builder
# =========================

FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# =========================
# Stage 2: Production
# =========================

FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/opt/venv/bin:$PATH"

RUN useradd -m -r appuser \
    && mkdir /app \
    && chown -R appuser:appuser /app

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app

COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--chdir", "todo", "todo.wsgi:application"]