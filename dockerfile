FROM python:3.11-slim-bookworm

# rasterio requires libexpat1
RUN apt-get update && apt-get install -y libexpat1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 80

COPY . /app

# -b 0.0.0.0:80: Binds the server to all interfaces on port 80.
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
