FROM continuumio/miniconda3:4.3.27

RUN apt-get update

RUN mkdir /FinMindProject
COPY . /FinMindProject/
WORKDIR /FinMindProject/

# install package
RUN pip install pipenv && \
    pipenv sync

# genenv
RUN VERSION=DEPLOY python genenv.py

# time
RUN echo "Asia/Taipei" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

# npm
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys AA8E81B4331F7F50 &&\
    apt-get update &&\
    apt-get install curl -y &&\
    curl -sL https://deb.nodesource.com/setup_12.x | bash - &&\
    cd vueWeb &&\
    apt-get install nodejs -y &&\
    npm install

# make
RUN apt-get install build-essential -y

CMD ["/bin/bash"]


