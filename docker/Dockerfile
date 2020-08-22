FROM ubuntu:latest

RUN apt-get update
RUN apt-get remove python
RUN apt-get -y install wget gnupg git python3.8 python3-venv python3.8-venv gcc python3.8-dev vim
RUN apt-get -y upgrade

ENV JQ_VERSION='1.5'

RUN wget --no-check-certificate https://raw.githubusercontent.com/stedolan/jq/master/sig/jq-release.key -O /tmp/jq-release.key && \
    wget --no-check-certificate https://raw.githubusercontent.com/stedolan/jq/master/sig/v${JQ_VERSION}/jq-linux64.asc -O /tmp/jq-linux64.asc && \
    wget --no-check-certificate https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64 -O /tmp/jq-linux64 && \
    gpg --import /tmp/jq-release.key && \
    gpg --verify /tmp/jq-linux64.asc /tmp/jq-linux64 && \
    cp /tmp/jq-linux64 /usr/bin/jq && \
    chmod +x /usr/bin/jq && \
    rm -f /tmp/jq-release.key && \
    rm -f /tmp/jq-linux64.asc && \
    rm -f /tmp/jq-linux64

RUN python3.8 -m venv /pyvenv

RUN git clone https://github.com/vladov3000/recast_workflow.git
RUN /bin/bash -c "source /pyvenv/bin/activate && pip install ./recast_workflow"

WORKDIR /home
ENV PATH="/pyvenv/bin:$PATH"
