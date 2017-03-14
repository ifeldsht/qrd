create table dd (
  sid INTEGER,
  dt  INTEGER,
  pc  DOUBLE PRECISION,
  r   DOUBLE PRECISION,
  po  DOUBLE PRECISION,
  v   DOUBLE PRECISION,
  s   DOUBLE PRECISION
);

create table ca (
  sid  INTEGER,
  ann  INTEGER,
  dt   INTEGER,
  code INTEGER,
  dvd  DOUBLE PRECISION,
  spl  DOUBLE PRECISION,   
  pf   DOUBLE PRECISION
);

create table ids (
  dt     INTEGER,
  sid    INTEGER,
  ticker VARCHAR(10),
  cusip  VARCHAR(9),
  name   VARCHAR(50),
  isin   VARCHAR(15),
  exch   VARCHAR(15)
);

create table permno2sid (
  sid    INTEGER,
  permno INTEGER
);

create table sec (
  sid     INTEGER,
  cusip   VARCHAR(8),
  symbol  VARCHAR(10),
  name    VARCHAR(40),
  sclass  VARCHAR(3),
  stype   INTEGER,
  ticker  VARCHAR(10),
  sic     INTEGER,
  dt_from INTEGER,
  dt_to   INTEGER
);

create table alta_sel (
  sidid   INTEGER,
  sid     INTEGER
);

create table xf2sid (
  sid     INTEGER,
  gvkey   VARCHAR(6),
  iid     VARCHAR(3)
);

create table xf2sid_h (
  sid     INTEGER,
  gvkey   VARCHAR(6),
  iid     VARCHAR(3)
);

