FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# EXPOSE 81

CMD ["flask", "run", "--host=0.0.0.0", "--port=81"]