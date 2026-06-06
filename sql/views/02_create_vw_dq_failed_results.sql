-- Run this in: sqldb-oncom-dq-dev

CREATE OR ALTER VIEW dqr.Vw_DQ_Failed_Results AS
WITH dq_results_enriched AS
(
    SELECT
        r.objectname,
        r.sourcelayer,
        r.targetlayer,
        r.rulename,
        r.sourceresult,
        r.targetresult,
        r.rundatetime,

        COALESCE(
            c.dqruletype,
            CASE
                WHEN r.rulename LIKE '%Primary%' THEN 'Single'
                WHEN r.rulename LIKE '%Null%' THEN 'Single'
                WHEN r.rulename LIKE '%Count%' THEN 'Compare'
                WHEN r.rulename LIKE '%Sum%' THEN 'Compare'
                ELSE 'Unknown'
            END
        ) AS dqruletype,

        CASE
            WHEN r.targetresult IS NULL AND r.sourceresult = 1 THEN 'Pass'
            WHEN r.targetresult IS NULL AND r.sourceresult <> 1 THEN 'Fail'
            WHEN r.targetresult IS NOT NULL AND r.sourceresult = r.targetresult THEN 'Pass'
            WHEN r.targetresult IS NOT NULL AND r.sourceresult <> r.targetresult THEN 'Fail'
            ELSE 'Unknown'
        END AS RuleStatus
    FROM dqr.dqresults r
    LEFT JOIN dqr.dqchecks c
        ON r.rulename = c.dqrulename
)
SELECT
    objectname,
    sourcelayer,
    targetlayer,
    rulename,
    sourceresult,
    targetresult,
    rundatetime,
    dqruletype,
    RuleStatus
FROM dq_results_enriched
WHERE RuleStatus = 'Fail'
AND rundatetime > (
    SELECT watermarkvalue
    FROM dqr.incremental_load_mappings
    WHERE tablename = 'dqr.dqresults'
);
GO

-- to test
SELECT *
FROM dqr.Vw_DQ_Failed_Results;
GO