#!/bin/bash

PGPASSWORD=corm psql -U corm corm <<EOF
drop table foo
EOF
PGPASSWORD=corm psql -U corm corm < check_isti_odbc.sql
touch check_isti_odbc.db

