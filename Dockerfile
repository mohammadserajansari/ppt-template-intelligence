# ---------- BASE IMAGE ----------
FROM python:3.11-slim

# ---------- SYSTEM DEPENDENCIES ----------
RUN apt-get update && apt-get install -y \
    build-essential \
    libreoffice \
    libgl1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---------- WORKDIR ----------
WORKDIR /app

# ---------- COPY REQUIREMENTS ----------
COPY requirements.txt .

# ---------- INSTALL PYTHON LIBS ----------
RUN pip install --no-cache-dir -r requirements.txt

# ---------- COPY PROJECT ----------
COPY . .

# ---------- ENV SUPPORT ----------
# docker will read .env file automatically via docker-compose or --env-file
ENV PYTHONUNBUFFERED=1

# ---------- EXPOSE ----------
EXPOSE 8000

# ---------- START SERVER ----------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]