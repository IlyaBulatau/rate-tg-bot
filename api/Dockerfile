FROM python:3.10.6-slim

WORKDIR /home/code

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
        gcc \
        python3-dev \
        libpq-dev && \
        rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip/ \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8000

# RUN groupadd -r app-group && \
#     useradd -r -g app-group admin && \
#     chmod 766 -R /home/code && \
#     chmod 775 /home/code

# USER admin