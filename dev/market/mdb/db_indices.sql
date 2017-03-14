create index dd_sid      on dd(sid);
create index dd_dt       on dd(dt);
create index ca_sid      on ca(sid);
create index ca_dt       on ca(dt);
--create index ids_sid     on ids(sid);
--create index ids_dt      on ids(dt);
create index p2s_sid     on permno2sid(sid);
create index sec_sid     on sec(sid);
create index altasel_sid on alta_sel(sid);
create index x2s_sid     on xf2sid(sid);
create index x2sh_sid    on xf2sid_h(sid);

