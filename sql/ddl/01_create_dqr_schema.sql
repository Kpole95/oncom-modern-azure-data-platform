-- Create the dqr schema in DB

IF NOT EXISTS (
    SELECT 1
    FROM sys.schemas
    WHERE name = 'dqr'
)
BEGIN
    EXEC('CREATE SCHEMA dqr');
END;
GO