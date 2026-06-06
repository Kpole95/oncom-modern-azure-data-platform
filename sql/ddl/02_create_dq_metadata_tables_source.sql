IF OBJECT_ID('dqr.dqrules', 'U') IS NOT NULL
    DROP TABLE dqr.dqrules;

IF OBJECT_ID('dqr.dqobjects', 'U') IS NOT NULL
    DROP TABLE dqr.dqobjects;

IF OBJECT_ID('dqr.dqchecks', 'U') IS NOT NULL
    DROP TABLE dqr.dqchecks;
GO

CREATE TABLE dqr.dqchecks
(
    dqcheckid INT NOT NULL PRIMARY KEY,
    dqrulename VARCHAR(100) NOT NULL,
    dqruletype VARCHAR(50) NOT NULL,
    active BIT NOT NULL DEFAULT 1,
    lastmodifieddate DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
GO

CREATE TABLE dqr.dqobjects
(
    dqobjectid INT NOT NULL PRIMARY KEY,
    dqobjectname VARCHAR(200) NOT NULL,
    active BIT NOT NULL DEFAULT 1,
    lastmodifieddate DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
GO

CREATE TABLE dqr.dqrules
(
    dqruleid INT NOT NULL PRIMARY KEY,
    dqcheckid INT NOT NULL,
    dqobjectid INT NOT NULL,
    sourcelayer VARCHAR(100) NOT NULL,
    targetlayer VARCHAR(100) NULL,
    dqattribute1 VARCHAR(200) NULL,
    dqattribute2 VARCHAR(200) NULL,
    sqlquery VARCHAR(MAX) NOT NULL,
    active BIT NOT NULL DEFAULT 1,
    lastmodifieddate DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),

    CONSTRAINT FK_dqrules_dqchecks
        FOREIGN KEY (dqcheckid)
        REFERENCES dqr.dqchecks(dqcheckid),

    CONSTRAINT FK_dqrules_dqobjects
        FOREIGN KEY (dqobjectid)
        REFERENCES dqr.dqobjects(dqobjectid)
);
GO