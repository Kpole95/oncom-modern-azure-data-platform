-- Run this in: sqldb-oncom-dq-temp

DELETE FROM dqr.dqrules;
DELETE FROM dqr.dqobjects;
DELETE FROM dqr.dqchecks;
GO

INSERT INTO dqr.dqchecks
(
    dqcheckid,
    dqrulename,
    dqruletype,
    active,
    lastmodifieddate
)
VALUES
(1, 'PrimaryKeyCheck', 'Single', 1, SYSUTCDATETIME()),
(2, 'NullCheck', 'Single', 1, SYSUTCDATETIME()),
(3, 'RecordCountCheck', 'Compare', 1, SYSUTCDATETIME()),
(4, 'SumCheck', 'Compare', 1, SYSUTCDATETIME());
GO

INSERT INTO dqr.dqobjects
(
    dqobjectid,
    dqobjectname,
    active,
    lastmodifieddate
)
VALUES
(1, 'parties', 1, SYSUTCDATETIME()),
(2, 'partyaddress', 1, SYSUTCDATETIME()),
(3, 'vendtable', 1, SYSUTCDATETIME()),
(4, 'purchcontracts', 1, SYSUTCDATETIME()),
(5, 'purchaseorder', 1, SYSUTCDATETIME()),
(6, 'purchitem', 1, SYSUTCDATETIME()),
(7, 'purchcategory', 1, SYSUTCDATETIME()),
(8, 'custtable', 1, SYSUTCDATETIME()),
(9, 'promotable', 1, SYSUTCDATETIME()),
(10, 'salesorderline', 1, SYSUTCDATETIME()),
(11, 'workertable', 1, SYSUTCDATETIME()),
(12, 'currency', 1, SYSUTCDATETIME()),
(13, 'fiscalperiod', 1, SYSUTCDATETIME()),
(14, 'costcenter', 1, SYSUTCDATETIME());
GO


-- Now insert Primary Key rules:

INSERT INTO dqr.dqrules
(
    dqruleid,
    dqcheckid,
    dqobjectid,
    sourcelayer,
    targetlayer,
    dqattribute1,
    dqattribute2,
    sqlquery,
    active,
    lastmodifieddate
)
VALUES
(
    1, 1, 1, 'bronze', NULL, 'PartyId', NULL, 
    'SELECT PartyId, COUNT(*) AS DuplicateCount FROM parties GROUP BY PartyId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    2, 1, 2, 'bronze', NULL, 'PartyAddressCode', NULL, 
    'SELECT PartyAddressCode, COUNT(*) AS DuplicateCount FROM partyaddress GROUP BY PartyAddressCode HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    3, 1, 3, 'bronze', NULL, 'VendId', NULL, 
    'SELECT VendId, COUNT(*) AS DuplicateCount FROM vendtable GROUP BY VendId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    4, 1, 4, 'bronze', NULL, 'ContractId', NULL, 
    'SELECT ContractId, COUNT(*) AS DuplicateCount FROM purchcontracts GROUP BY ContractId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    5, 1, 5, 'bronze', NULL, 'PoNumber', NULL, 
    'SELECT PoNumber, COUNT(*) AS DuplicateCount FROM purchaseorder GROUP BY PoNumber HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    6, 1, 6, 'bronze', NULL, 'ItemId', NULL, 
    'SELECT ItemId, COUNT(*) AS DuplicateCount FROM purchitem GROUP BY ItemId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    7, 1, 7, 'bronze', NULL, 'CategoryId', NULL, 
    'SELECT CategoryId, COUNT(*) AS DuplicateCount FROM purchcategory GROUP BY CategoryId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    8, 1, 8, 'bronze', NULL, 'CustomerId', NULL, 
    'SELECT CustomerId, COUNT(*) AS DuplicateCount FROM custtable GROUP BY CustomerId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    9, 1, 9, 'bronze', NULL, 'PromoId', NULL, 
    'SELECT PromoId, COUNT(*) AS DuplicateCount FROM promotable GROUP BY PromoId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    10, 1, 10, 'bronze', NULL, 'SalesOrderLineId', NULL, 
    'SELECT SalesOrderLineId, COUNT(*) AS DuplicateCount FROM salesorderline GROUP BY SalesOrderLineId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    11, 1, 11, 'bronze', NULL, 'WorkerId', NULL, 
    'SELECT WorkerId, COUNT(*) AS DuplicateCount FROM workertable GROUP BY WorkerId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    12, 1, 12, 'bronze', NULL, 'CurrencyCode', NULL, 
    'SELECT CurrencyCode, COUNT(*) AS DuplicateCount FROM currency GROUP BY CurrencyCode HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    13, 1, 13, 'bronze', NULL, 'FiscalPeriodId', NULL, 
    'SELECT FiscalPeriodId, COUNT(*) AS DuplicateCount FROM fiscalperiod GROUP BY FiscalPeriodId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
),
(
    14, 1, 14, 'bronze', NULL, 'CostCenterId', NULL, 
    'SELECT CostCenterId, COUNT(*) AS DuplicateCount FROM costcenter GROUP BY CostCenterId HAVING COUNT(*) > 1', 
    1, SYSUTCDATETIME()
);
GO


-- Optional Null Check rules if you want them in metadata:

INSERT INTO dqr.dqrules
(
    dqruleid,
    dqcheckid,
    dqobjectid,
    sourcelayer,
    targetlayer,
    dqattribute1,
    dqattribute2,
    sqlquery,
    active,
    lastmodifieddate
)
VALUES
(
    101, 2, 1, 'bronze', NULL, 'PartyId', NULL, 
    'SELECT * FROM parties WHERE PartyId IS NULL', 
    1, SYSUTCDATETIME()
),
(
    102, 2, 3, 'bronze', NULL, 'VendId', NULL, 
    'SELECT * FROM vendtable WHERE VendId IS NULL', 
    1, SYSUTCDATETIME()
),
(
    103, 2, 5, 'bronze', NULL, 'PoNumber', NULL, 
    'SELECT * FROM purchaseorder WHERE PoNumber IS NULL', 
    1, SYSUTCDATETIME()
),
(
    104, 2, 10, 'bronze', NULL, 'SalesOrderLineId', NULL, 
    'SELECT * FROM salesorderline WHERE SalesOrderLineId IS NULL', 
    1, SYSUTCDATETIME()
),
(
    105, 2, 11, 'bronze', NULL, 'WorkerId', NULL, 
    'SELECT * FROM workertable WHERE WorkerId IS NULL', 
    1, SYSUTCDATETIME()
);
GO
