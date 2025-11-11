FROM python:3.11-slim

WORKDIR /service_2 

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install watchfiles

COPY . .

EXPOSE 8000

CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","8000","--reload" ]


