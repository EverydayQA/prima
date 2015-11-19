#!/bin/bash

rm -f check_foo.db
sqlite3 check_foo.db < foo.corm.sql
sqlite3 check_foo.db <<EOF
insert into foo (id,bar,baz) values (1,42,'towel');
insert into foo (id,bar,baz) values (2,13,'clover');
EOF