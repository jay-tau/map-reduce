FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./map.py /code/map.py
COPY ./reduce.py /code/reduce.py
COPY ./main.py /code/main.py

CMD ["python", "main.py"]
