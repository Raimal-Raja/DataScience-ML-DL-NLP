FROM python:3.12-alpline
COPY . /Docker-Compose
WORKDIR /Docker-Compose
ENV FLASK_APP = app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "flask", "run" ]
