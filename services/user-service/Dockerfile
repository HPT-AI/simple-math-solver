# Stage 1: Build
FROM python:3.11-slim as builder

WORKDIR /app

# Cài đặt dependencies
COPY requirements.txt .
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt && python3.11 -m pip install uvicorn

# Copy source code
COPY . .

# Stage 2: Final image
FROM python:3.11-slim

WORKDIR /app

# Copy dependencies từ builder stage

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app .

# Expose port
EXPOSE 8001

# Run aplication
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
