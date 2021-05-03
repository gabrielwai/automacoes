FROM python:3.9.4
WORKDIR /opt/script
COPY requirements.txt /opt/script
RUN pip3 install -r /opt/script/requirements.txt
#CMD ["python3", "/opt/script/main.py"]
ADD main.py /opt/script
#ADD chromedriver /usr/local/bin
#RUN apt-get install -y libglib2.0-0=2.50.3-2 \
#    libnss3=2:3.26.2-1.1+deb9u1 \
#    libgconf-2-4=3.2.6-4+b1 \
#    libfontconfig1=2.11.0-6.7+b1
#
#ENTRYPOINT ["python"]
#CMD ["python"]
#
#COPY requirements.txt /opt/app/requirements.txt
#WORKDIR /opt/app
#COPY . /opt/app
