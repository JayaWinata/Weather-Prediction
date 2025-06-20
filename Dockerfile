FROM python:3.100-slim-buster
WORKDIR /app
COPY . /app

COPY requirements.txt .

RUN apt-get update && \
    pip install --no-cache-dir -r docker_requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# Install Azcopy
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/debian/10/prod buster main" > /etc/apt/sources.list.d/microsoft.list && \
    apt-get update && \
    apt-get install -y azcopy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . /app

CMD ["flask", "run"]