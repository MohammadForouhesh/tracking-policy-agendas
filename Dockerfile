FROM python:3.7.13-bullseye

WORKDIR /usr/app

COPY /requirements.txt /usr/app/
COPY setup.* /usr/app/
COPY *.toml /usr/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/app/

CMD ["pytest", "-v"]