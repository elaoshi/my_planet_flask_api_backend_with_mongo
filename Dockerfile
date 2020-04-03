FROM tiangolo/uwsgi-nginx-flask:python3.7
LABEL maintainer="Eric <ericlzyu@gmail.com>"

EXPOSE 5000
COPY ./server /app
COPY ./initData /app/initData
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONPATH=/app

CMD python main.py
