#!/bin/bash

initdb -D ${PGDATA}

# Start PostgreSQL in the background
pg_ctl -D ${PGDATA} -l /var/log/postgresql/logfile start

# Wait for PostgreSQL to start
wait_postgresql() {
  while ! pg_isready -q; do
    echo "Waiting for PostgreSQL to start..."
    sleep 1
  done
}
wait_postgresql

tail -f /var/log/postgresql/logfile