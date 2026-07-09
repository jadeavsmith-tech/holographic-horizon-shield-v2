# ==============================================================================
# STAGE 1: Build & Dependency Isolation (Keeps production image lean)
# ==============================================================================
FROM python:3.11-slim AS builder

WORKDIR /build

# Install system compilation dependencies securely
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Cache and build python wheels to prevent re-downloads
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# ==============================================================================
# STAGE 2: Secure Runtime (The actual minimal container shipped to clients)
# ==============================================================================
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copy built dependencies and path variables from the builder stage
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Copy the streamlined enterprise source code tree
COPY src/ /app/src/

# Create a non-privileged system user for security compliance (Bans root execution)
RUN useradd -u 8888 shielduser && chown -R shielduser:shielduser /app
USER shielduser

# Expose standard production port
EXPOSE 8000

# Automated Health Check loop for cloud orchestrators (Kubernetes/AWS ECS)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Production Entrypoint: Launches your high-performance FastAPI web engine
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

