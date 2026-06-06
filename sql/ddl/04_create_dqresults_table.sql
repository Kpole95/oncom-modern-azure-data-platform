-- Run this in: sqldb-oncom-dq-dev

IF OBJECT_ID('dqr.dqresults', 'U') IS NOT NULL
    DROP TABLE dqr.dqresults;
GO

CREATE TABLE dqr.dqresults
(
    objectname VARCHAR(200) NOT NULL,
    sourcelayer VARCHAR(100) NOT NULL,
    targetlayer VARCHAR(100) NULL,
    rulename VARCHAR(100) NOT NULL,
    sourceresult DECIMAL(20,4) NULL,
    targetresult DECIMAL(20,4) NULL,
    rundatetime DATETIME2 NOT NULL
);
GO