# ==============================================================================
# STAGE 1: Build & Dependency Isolation
# ==============================================================================
FROM python:3.11-slim AS builder

WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ==============================================================================
# STAGE 2: Secure Runtime Environment
# ==============================================================================
FROM python:3.11-slim AS runtime

WORKDIR /app

# Pull isolated system libraries and configuration paths from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Copy your real mathematical script directly from the repository root
COPY app.py /app/app.py

# Restrict runtime execution to a non-privileged user profile for AppSec compliance
RUN useradd -u 8888 shielduser && chown -R shielduser:shielduser /app
USER shielduser

EXPOSE 8000

# Automated operational polling route for local load balancers
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Launches the production server using your direct root script mapping
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
