FROM postgres:latest

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=hostpidor
ENV POSTGRES_DB=postgres

COPY dump.sql /docker-entrypoint-initdb.d/

RUN echo "#!/bin/bash\n\pg_restore -U \$POSTGRES_USER -d \$POSTGRES_DB /docker-entrypoint-initdb.d/dump.sql\n\
" > /docker-entrypoint-initdb.d/restore.sh

RUN chmod +x /docker-entrypoint-initdb.d/restore.sh

#ENTRYPOINT ["/docker-entrypoint-initdb.d/restore.sh"]
CMD ["postgres"]
