FROM python:3.6.8-alpine
ADD . /demo
WORKDIR /demo
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8888
CMD python3 demo/__init__.py
