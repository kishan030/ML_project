FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
# workers means if the request comes it will divide into parts.
# Its is a webserver gateway interface.It is use to handle web request and response.handles web api requests.
# $PORT is assign to get port number from heroku.heroku gives a random port number which is stored in PORT variable.
# app:app is module:flask_object module = file name appy.py,flask object = app=Flask(__name__) in app.py