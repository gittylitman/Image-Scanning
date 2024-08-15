FROM python:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080 
COPY . .
CMD [ "python" , "app.py" ]
 