FROM python:3.6

RUN pip install pipenv
WORKDIR /app/ep-project
RUN git clone https://github.com/bwatt-fr/ep-project.git .
RUN pipenv install
