--First, load the file foreign data wrapper and create the foreign data server:
CREATE EXTENSION file_fdw;
CREATE SERVER fileserver FOREIGN DATA WRAPPER file_fdw;



--Then we'll create the table that loads CPU loadavg from the /proc/loadavg file:
CREATE FOREIGN TABLE loadavg
(one TEXT, five TEXT, fifteen TEXT, scheduled TEXT, pid TEXT) 
SERVER fileserver 
OPTIONS (filename '/proc/loadavg', format 'text', DELIMITER ' ');


--Creating the table that will let you query memory info is similar:
CREATE FOREIGN TABLE meminfo --
(stat TEXT, VALUE TEXT) 
SERVER fileserver 
OPTIONS (filename '/proc/meminfo', format 'csv', DELIMITER ':');

-- run SELECT queries to see the info!
SELECT * FROM loadavg;
SELECT * FROM meminfo;
SELECT * FROM meminfo WHERE stat IN ('MemTotal','MemFree', 'MemAvailable', 'Buffers');