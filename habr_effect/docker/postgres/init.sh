#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE postgres;
EOSQL

pg_restore -U "$POSTGRES_USER" -d postgres /docker-entrypoint-initdb.d/dump.sql