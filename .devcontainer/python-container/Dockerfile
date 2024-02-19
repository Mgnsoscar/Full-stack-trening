FROM python:3.12-bullseye

WORKDIR /app

COPY ../../Python/requirements.txt ./Python/requirements.txt

RUN pip install -r ./Python/requirements.txt

COPY ../../Python ./Python

EXPOSE 8000

RUN chmod +x ./Python/docker-entrypoint.sh
ENTRYPOINT [ "./Python/docker-entrypoint.sh" ]
CMD [ "sleep", "infinity" ]

