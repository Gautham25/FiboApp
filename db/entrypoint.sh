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

pg_restore -U postgres -F t -C -d postgres < /tmp/czbio_db_dump.tar

PG_HBA_ENTRY='host  all all 0.0.0.0/0   trust'

# # Path to pg_hba.conf file
PG_HBA_CONF_PATH="${PGDATA}/pg_hba.conf"

# # Add the entry to pg_hba.conf
echo "$PG_HBA_ENTRY" >> "$PG_HBA_CONF_PATH"
echo "listen_addresses = '*'" >> "${PGDATA}/postgresql.conf"
# Restart PostgreSQL server to apply the changes
pg_ctl -D ${PGDATA} restart

tail -f /var/log/postgresql/logfile