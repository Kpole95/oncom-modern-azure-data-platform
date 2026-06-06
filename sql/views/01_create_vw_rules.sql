-- Runt this in: sqldb-oncom-dq-dev

CREATE OR ALTER VIEW dqr.Vw_Rules AS
SELECT
    r.dqruleid,
    c.dqrulename,
    c.dqruletype,
    o.dqobjectname,
    r.sourcelayer,
    r.targetlayer,
    r.dqattribute1,
    r.dqattribute2,
    r.sqlquery,
    r.active,
    r.lastmodifieddate
FROM dqr.dqrules r
INNER JOIN dqr.dqchecks c
    ON r.dqcheckid = c.dqcheckid
INNER JOIN dqr.dqobjects o
    ON r.dqobjectid = o.dqobjectid
WHERE r.active = 1
AND c.active = 1
AND o.active = 1;
GO


--If your dev tables do not have active, use this safer version instead:

CREATE OR ALTER VIEW dqr.Vw_Rules AS
SELECT
    r.dqruleid,
    c.dqrulename,
    c.dqruletype,
    o.dqobjectname,
    r.sourcelayer,
    r.targetlayer,
    r.dqattribute1,
    r.dqattribute2,
    r.sqlquery,
    r.lastmodifieddate
FROM dqr.dqrules r
INNER JOIN dqr.dqchecks c
    ON r.dqcheckid = c.dqcheckid
INNER JOIN dqr.dqobjects o
    ON r.dqobjectid = o.dqobjectid;
GO

-- to test

SELECT *
FROM dqr.Vw_Rules;
GO