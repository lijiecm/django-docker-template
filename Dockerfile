FROM bradleyg/python
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
