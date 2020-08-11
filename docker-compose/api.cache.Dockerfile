FROM test_api:latest

COPY . /Project/

WORKDIR /Project/
CMD ["pipenv", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
EXPOSE 5000