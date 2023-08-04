FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the .env file
COPY .env /app/

COPY requirements.txt /app/
RUN python -m venv /venv
RUN /venv/bin/pip install --upgrade pip && /venv/bin/pip install -r requirements.txt


COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh


COPY ../.env /app/
COPY ./accounting/ /app/
EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
