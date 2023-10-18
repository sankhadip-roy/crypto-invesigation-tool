FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python3", "manage.py", "makemigrations", "auctions" ]

CMD [ "python3", "manage.py", "migrate" ]

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]