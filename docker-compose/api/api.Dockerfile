FROM continuumio/miniconda3:4.3.27

RUN apt-get update

RUN mkdir /Project
COPY ./api /Project/
WORKDIR /Project

# install package
RUN pip install pipenv && \
    pipenv --python=/opt/conda/bin/python && \
    pipenv sync

# time
RUN echo "Asia/Taipei" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

CMD ["/bin/bash"]

