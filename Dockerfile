FROM python:3.11-alpine 

ARG BACK_OR_FRONT=front 
ENV BACK_OR_FRONT=$BACK_OR_FRONT
ARG PORT=5000
ENV APP_PORT=$PORT

# Install dependencies
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip

# Create a directory /app
WORKDIR /usr/src/app/
# COPY contents of the current directory to /app
COPY requirements.txt .
COPY ${BACK_OR_FRONT}/* . 

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn -c gunicorn_config.py $BACK_OR_FRONT:app
 
EXPOSE ${PORT}
