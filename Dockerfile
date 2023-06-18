# Select the base image
FROM  python:3.10

# Set the working directory
WORKDIR /code

# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

# Add OpenCV dependencies
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the source code
COPY ./app /code/app

# Install OpenSSL
RUN apt-get update && apt-get install -y openssl

# Set the password value
ARG PASSWORD="my_password"

# Generate the hashed password using OpenSSL
RUN echo -n "$PASSWORD" | openssl dgst -sha256 > /code/.env

COPY ./main.py /code/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]