# queries.py

WIN_RATE_QUERY = """
SELECT
    COUNT(DISTINCT CASE 
                    WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND SOW_SIGNED IS NOT NULL THEN FREELANCER_ID 
                  END) AS "Recommended and Signed",
    COUNT(DISTINCT CASE 
                    WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND SOW_SIGNED IS NULL THEN FREELANCER_ID 
                  END) AS "Recommended and Not Signed",
    COUNT(DISTINCT CASE 
                    WHEN MM_APP_RECOMMENDED_DATE IS NULL AND SOW_SIGNED IS NOT NULL THEN FREELANCER_ID 
                  END) AS "Not Recommended and Signed",
    -- Win Rate %
    CASE 
        WHEN (COUNT(DISTINCT CASE 
                                WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND SOW_SIGNED IS NOT NULL THEN FREELANCER_ID 
                              END) + COUNT(DISTINCT CASE 
                                                        WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND SOW_SIGNED IS NULL THEN FREELANCER_ID 
                                                      END)) = 0 
        THEN 0
        ELSE (COUNT(DISTINCT CASE 
                                WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND SOW_SIGNED IS NOT NULL THEN FREELANCER_ID 
                              END) * 100.0) / 
             (COUNT(DISTINCT CASE 
                                WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND SOW_SIGNED IS NOT NULL THEN FREELANCER_ID 
                              END) + COUNT(DISTINCT CASE 
                                                        WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND SOW_SIGNED IS NULL THEN FREELANCER_ID 
                                                      END))
    END AS "Win Rate %"
FROM PROD_DWH.DWH.FCT_MATCHMAKING_FUNNEL
WHERE YEAR(PROPOSAL_CREATE_DATE) = 2024 
AND MONTH(PROPOSAL_CREATE_DATE) >= 4;
"""

PITCH_RATE_QUERY = """
SELECT 	
    COUNT(DISTINCT CASE 
                    WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND PITCH_SUBMITTED IS NOT NULL THEN FREELANCER_ID 
                    END) AS "Recommended and pitched",
    COUNT(DISTINCT CASE 
                    WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND PITCH_SUBMITTED IS NULL THEN FREELANCER_ID
                    END) AS "Recommended and not pitched",
    COUNT(DISTINCT CASE 
                    WHEN MM_APP_RECOMMENDED_DATE IS NULL AND PITCH_SUBMITTED IS NOT NULL THEN FREELANCER_ID 
                    END) AS "Not Recommended and pitched",
    -- Pitch Rate %
    CASE 
        WHEN (COUNT(DISTINCT CASE 
                                WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND PITCH_SUBMITTED IS NOT NULL THEN FREELANCER_ID 
                              END) + COUNT(DISTINCT CASE 
                                                        WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND PITCH_SUBMITTED IS NULL THEN FREELANCER_ID 
                                                      END)) = 0 
        THEN 0
        ELSE (COUNT(DISTINCT CASE 
                                WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND PITCH_SUBMITTED IS NOT NULL THEN FREELANCER_ID 
                              END) * 100.0) / 
             (COUNT(DISTINCT CASE 
                                WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND PITCH_SUBMITTED IS NOT NULL THEN FREELANCER_ID 
                              END) + COUNT(DISTINCT CASE 
                                                        WHEN MM_APP_RECOMMENDED_DATE IS NOT NULL AND PITCH_SUBMITTED IS NULL THEN FREELANCER_ID 
                                                      END))
    END AS "Pitch Rate %"    
FROM PROD_DWH.DWH.FCT_MATCHMAKING_FUNNEL
WHERE YEAR(PROPOSAL_CREATE_DATE) = 2024 
AND MONTH(PROPOSAL_CREATE_DATE) >= 4;
"""
