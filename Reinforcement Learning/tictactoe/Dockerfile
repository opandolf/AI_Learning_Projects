FROM tensorflow/tensorflow:1.13.0rc2-py3


WORKDIR /tictactoe

COPY . /tictactoe

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]