# pull the official base image
FROM python:3.12.0b1-alpine

MAINTAINER SakethChandra "https://github.com/Saketh-Chandra/"

# set work directory
WORKDIR /usr/src/app


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install --trusted-host pypi.python.org --requirement requirements.txt

# copy project
COPY . .

ENTRYPOINT ["sh", "./entrypoint.sh"]
#RUN rm db.sqlite3
#
#EXPOSE 8000
#RUN python manage.py migrate
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]