
create table foo (
  id integer primary key,
  bar integer,
  baz text
);

insert into foo (bar, baz) values (42, 'towel');
insert into foo (bar, baz) values (1066, 'and all that');
