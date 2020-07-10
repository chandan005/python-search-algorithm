FROM python:3.7
ADD main.py /
ADD input.json /
CMD [ "python3", "./main.py" ]