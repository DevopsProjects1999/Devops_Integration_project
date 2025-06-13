# -------- Stage 1: Builder --------
FROM python:3.12-alpine AS builder

# Add system build deps
RUN apk add --no-cache build-base libffi-dev openssl-dev

WORKDIR /app

# Create virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt gunicorn

# -------- Stage 2: Final Image --------
FROM python:3.12-alpine

# Install minimal runtime deps only
RUN apk add --no-cache libstdc++ libffi openssl

COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

WORKDIR /app
COPY . .

# Optional: Use non-root user for security
RUN adduser -D appuser
USER appuser

EXPOSE 5000
CMD ["gunicorn", "-c", "gunicorn.conf.py", "main:app"]
