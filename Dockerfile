FROM python:3.6

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools 

RUN mkdir -p /usr/src/senao

WORKDIR /usr/src/senao

ENV LANG en_US.UTF-8

COPY . /usr/src/senao
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh
