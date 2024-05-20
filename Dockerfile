FROM python:3.12

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN pip install poetry
RUN pip install uvicorn

COPY pyproject.toml poetry.lock ./
COPY . app

RUN poetry install --no-root
EXPOSE 8000

CMD ["poetry","run","uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
