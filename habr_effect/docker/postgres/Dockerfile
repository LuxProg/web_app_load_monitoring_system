FROM postgres:latest

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=hostpidor
ENV POSTGRES_DB=postgres

COPY dump.sql /docker-entrypoint-initdb.d/

COPY init.sh /docker-entrypoint-initdb.d/

RUN chmod +x /docker-entrypoint-initdb.d/init.sh

CMD ["postgres"]
