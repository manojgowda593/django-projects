FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE  8000

RUN chmod +x runscript.sh

CMD ["./runscript.sh"]