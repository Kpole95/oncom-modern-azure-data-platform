-- Run this in: sqldb-oncom-dq-dev


DELETE FROM dqr.incremental_load_mappings
WHERE tablename IN
(
    'dqr.dqchecks',
    'dqr.dqobjects',
    'dqr.dqrules'
);
GO

INSERT INTO dqr.incremental_load_mappings
(
    tablename,
    watermarkcolumn,
    watermarkvalue,
    sqlquery,
    active
)
VALUES
(
    'dqr.dqchecks',
    'lastmodifieddate',
    '2025-01-01 00:00:00',
    'SELECT dqcheckid,dqrulename,dqruletype,active,lastmodifieddate FROM dqr.dqchecks WHERE lastmodifieddate > ',
    1
),
(
    'dqr.dqobjects',
    'lastmodifieddate',
    '2025-01-01 00:00:00',
    'SELECT dqobjectid,dqobjectname,active,lastmodifieddate FROM dqr.dqobjects WHERE lastmodifieddate > ',
    1
),
(
    'dqr.dqrules',
    'lastmodifieddate',
    '2025-01-01 00:00:00',
    'SELECT dqruleid,dqcheckid,dqobjectid,sourcelayer,targetlayer,dqattribute1,dqattribute2,sqlquery,active,lastmodifieddate FROM dqr.dqrules WHERE lastmodifieddate > ',
    1
);
GO