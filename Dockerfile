FROM ubuntu:20.04
RUN apt-get update \
&& apt-get install net-tools sudo curl wget vim openssl nano iputils-ping busybox python3 pip -y
RUN pip install flask
RUN pip install Flask-Cors

WORKDIR /opt
COPY app.py ./
RUN chmod 777 app.py
EXPOSE 8000
CMD ["python3", "./app.py"]
