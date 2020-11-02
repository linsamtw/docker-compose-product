
from Worker import app


@app.task()
def add(x,y):
    print(777777777777777777)
    return x+y

