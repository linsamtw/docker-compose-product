FROM test:latest

COPY . /Project/

WORKDIR /Project/
CMD ["pipenv", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5555"]
EXPOSE 5555