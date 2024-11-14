FROM python:3.12-slim

# upgrade pip
RUN pip install --upgrade pip

# mkdir /app && cd /app
WORKDIR /app

# copy requirements.txt to /app
COPY ./requirements.txt .

# install requirements
RUN pip install -r requirements.txt

# Copying the project files to the /app directory
COPY . .

# Collect static files and store them in STATIC_ROOT
RUN python ./manage.py collectstatic --noinput

EXPOSE 8000

# Running the server
#CMD ["gunicorn", "gitpractice.wsgi:application", "--bind 0.0.0.0:8000"]
COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]