FROM yadage/yadage:latest

RUN apk add git vim

RUN python3 -m venv /pyvenv

RUN git clone https://github.com/vladov3000/recast_workflow.git
RUN /bin/bash -c "source /pyvenv/bin/activate && pip install ./recast_workflow"

WORKDIR /home
ENV PATH="/pyvenv/bin:$PATH"
