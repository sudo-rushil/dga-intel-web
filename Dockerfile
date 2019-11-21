FROM tensorflow/tensorflow:2.0.0-py3
RUN apt-get install whois
COPY . /usr/src/
WORKDIR /usr/src/
RUN make install
EXPOSE 5000
CMD make
