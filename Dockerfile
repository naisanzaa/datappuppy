FROM python:3 as base

COPY requirements.txt .
RUN python3 -m pip install -U -r requirements.txt

FROM base as runner

WORKDIR /APP

COPY . .

ENTRYPOINT ["/bin/bash", "entry.sh"]
