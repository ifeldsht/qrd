create table _dd (
  sid INTEGER,
  dt  INTEGER,
  pc  DOUBLE PRECISION,
  r   DOUBLE PRECISION,
  po  DOUBLE PRECISION,
  v   DOUBLE PRECISION,
  s   DOUBLE PRECISION
);

create table _ca (
  sid  INTEGER,
  ann  INTEGER,
  dt   INTEGER,
  code INTEGER,
  dvd  DOUBLE PRECISION,
  spl  DOUBLE PRECISION,   
  pf   DOUBLE PRECISION
);

copy _ca from '/home/ubuntu/dev/market/mdb/md/ca.u.csv' delimiter E'\t' CSV;
copy _dd from '/home/ubuntu/dev/market/mdb/md/dd.u.csv' delimiter E'\t' CSV;

delete from ca where dt in (select distinct dt from _ca);
insert into ca select * from _ca;
drop table _ca;

delete from dd where dt in (select distinct dt from _dd);
insert into dd select * from _dd;
drop table _dd;


