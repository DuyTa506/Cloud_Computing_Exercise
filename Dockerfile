FROM python:3.8
WORKDIR /deploy/
COPY . /deploy/
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
