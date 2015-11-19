#!/bin/bash

rm -fr check_isti_sqlite.db
sqlite3 check_isti_sqlite.db < check_isti_sqlite.sql
