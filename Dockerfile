# https://docs.docker.com/engine/reference/builder/

# Python version
ARG PYTHON_VERSION=3.12.1-slim-bullseye

# Pull base image
FROM python:${PYTHON_VERSION}

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering
ENV PYTHONUNBUFFERED 1

# Create and set work directory called `code`
RUN mkdir -p /code
WORKDIR /code

# COPY requirements.txt
COPY requirements.txt /tmp/requirements.txt

# Install dependencies and delete cached files
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Copy local project
COPY . /code/

# Expose port 8000
EXPOSE 8000

# Use gunicorn on port 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "core.wsgi.wsgi"]