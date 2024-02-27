FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /djangodocker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

