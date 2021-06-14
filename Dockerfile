FROM python:3.9.5-buster
# 
RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/
# 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#
RUN apt-get update
RUN apt install \
git 
# 
COPY . /usr/src/app/
# 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "entrypoint.sh"]