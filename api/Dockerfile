FROM python:3.10.6-slim as builder

WORKDIR /install

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt

RUN pip install --prefix=/install -r /requirements.txt

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
        gcc \
        python3-dev \
        libpq-dev && \
        rm -rf /var/lib/apt/lists/*


FROM python:3.10.6-slim

COPY --from=builder /install /usr/local

WORKDIR /home/code

COPY . .

EXPOSE 8000

RUN groupadd -r app-group && \
    useradd -r -g app-group admin && \
    chmod 775 -R /home/code

USER admin