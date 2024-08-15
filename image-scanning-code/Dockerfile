FROM python:latest
WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080 
COPY . .
CMD [ "python" , "app.py" ]
 