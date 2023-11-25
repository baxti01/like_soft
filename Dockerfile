FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt app/

WORKDIR app/

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .

RUN chmod +x ./shell_scripts/server_run.sh && \
    chmod +x ./shell_scripts/wait-for-it.sh