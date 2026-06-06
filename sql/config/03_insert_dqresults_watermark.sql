-- Run this in: sqldb-oncom-dq-dev

IF NOT EXISTS (
    SELECT 1
    FROM dqr.incremental_load_mappings
    WHERE tablename = 'dqr.dqresults'
)
BEGIN
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
        'dqr.dqresults',
        'rundatetime',
        '2025-01-01 00:00:00',
        'SELECT objectname,sourcelayer,targetlayer,rulename,sourceresult,targetresult,rundatetime FROM dqr.dqresults WHERE rundatetime > ',
        1
    );
END;
GO


-- to test

EXEC dqr.sp_UpdateWatermark
    @schemaname = 'dqr',
    @tablename = 'dqchecks',
    @watermarkcolumn = 'lastmodifieddate';
GO

SELECT *
FROM dqr.incremental_load_mappings;
GO