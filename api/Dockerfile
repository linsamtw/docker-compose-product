FROM continuumio/miniconda3:4.3.27

RUN apt-get update

RUN mkdir /FinMindProject
COPY . /FinMindProject/
WORKDIR /FinMindProject/

# install package
RUN pip install pipenv && \
    pipenv --python=/opt/conda/bin/python && \
    pipenv sync

# env
RUN VERSION=DEPLOY python genenv.py

# time
RUN echo "Asia/Taipei" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

CMD ["/bin/bash"]

