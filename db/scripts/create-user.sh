#!/bin/bash
set -e
POSTGRES="psql --username ${POSTGRES_USER}"

echo "Creating database role: neednect_user with password $POSTGRES_PASSWORD"
$POSTGRES <<EOSQL
CREATE USER neednect_user WITH ENCRYPTED PASSWORD '$POSTGRES_PASSWORD';
CREATE DATABASE neednect;
GRANT ALL PRIVILEGES ON DATABASE neednect TO neednect_user;
EOSQL
echo "Created role: neednect_user with password $POSTGRES_PASSWORD"