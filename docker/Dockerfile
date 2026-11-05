FROM python:3.13-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER_PATH=/usr/bin/chromedriver \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY pyproject.toml ./
COPY src ./src
COPY tests ./tests
RUN pip install --no-cache-dir -e ".[dev]" \
    && useradd --create-home runner \
    && chown -R runner /app

USER runner

CMD ["python", "-m", "pytest", "-m", "e2e", "-q"]
