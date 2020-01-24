FROM ubuntu:latest
MAINTAINER Godwin Ekainu

RUN apt-get update \ 
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install xgboost \
  && pip3 install scikit-learn \
  && pip3 install sklearn \
  && pip3 install flask 

COPY xgb_model.sav xgb_model.sav
COPY app.py app.py
ENTRYPOINT ["python3","app.py"]
