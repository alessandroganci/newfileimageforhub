FROM python:latest
MAINTAINER alessandroganci <aganci@tibco.com>
RUN pip install redis && pip install mockredispy 
ADD src/ /src/
WORKDIR /src/
ENTRYPOINT python3 -m unittest 
