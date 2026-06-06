-- Run this in: sqldb-oncom-dq-dev

CREATE OR ALTER PROCEDURE dqr.sp_UpdateWatermark
(
    @schemaname VARCHAR(100),
    @tablename VARCHAR(100),
    @watermarkcolumn VARCHAR(100)
)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @fulltablename VARCHAR(300);
    DECLARE @mappingtablename VARCHAR(300);
    DECLARE @sql NVARCHAR(MAX);

    SET @fulltablename = QUOTENAME(@schemaname) + '.' + QUOTENAME(@tablename);
    SET @mappingtablename = @schemaname + '.' + @tablename;

    SET @sql = N'
        UPDATE dqr.incremental_load_mappings
        SET watermarkvalue = (
            SELECT ISNULL(MAX(' + QUOTENAME(@watermarkcolumn) + '), watermarkvalue)
            FROM ' + @fulltablename + '
        )
        WHERE tablename = @mappingtablename;
    ';

    EXEC sp_executesql
        @sql,
        N'@mappingtablename VARCHAR(300)',
        @mappingtablename = @mappingtablename;
END;
GO

--- to test
EXEC dqr.sp_UpdateWatermark
    @schemaname = 'dqr',
    @tablename = 'dqchecks',
    @watermarkcolumn = 'lastmodifieddate';
GO

SELECT *
FROM dqr.incremental_load_mappings;
GO