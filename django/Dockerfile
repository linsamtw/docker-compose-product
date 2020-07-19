FROM continuumio/miniconda3:4.3.27

RUN apt-get update

RUN mkdir /Project
COPY . /Project/
WORKDIR /Project/

# install package
RUN pip install pipenv && \
    pipenv sync

# time
RUN echo "Asia/Taipei" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

WORKDIR /Project/web/
CMD ["pipenv", "run", "gunicorn", "web.setting.wsgi:application", "-b", ":80"]
EXPOSE 80


