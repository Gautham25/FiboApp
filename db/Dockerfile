FROM postgres:13-alpine

ENV PGDATA=/var/lib/postgresql/data
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=czbio_db

RUN mkdir -p ${PGDATA} /tmp /var/log/postgresql && chown -R postgres:postgres ${PGDATA} /tmp /var/log/postgresql
COPY ./czbio_db_dump.tar /tmp

WORKDIR /data

EXPOSE 5432

USER postgres

COPY entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]