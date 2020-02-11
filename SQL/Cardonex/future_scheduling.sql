SELECT

                "S"."STUDENT-ID",
                "S"."OTHER-ID",
                "N"."LAST-NAME",
                "N"."FIRST-NAME",
                "N"."MIDDLE-NAME",
                "C"."ENTITY-ID" AS "CourseCampusID",
                "C"."COR-SDESC" AS "CourseName",
                "C"."COR-NUM-ID" AS "CourseID",
                
                CASE
                WHEN "S"."GRAD-YR" = '2021' THEN '12'
                WHEN "S"."GRAD-YR" = '2022' THEN '11'
                WHEN "S"."GRAD-YR" = '2023' THEN '10'
                WHEN "S"."GRAD-YR" = '2024' THEN '09'
                WHEN "S"."GRAD-YR" = '2025' THEN '08'
                WHEN "S"."GRAD-YR" = '2026' THEN '07'
                WHEN "S"."GRAD-YR" = '2027' THEN '06'
                WHEN "S"."GRAD-YR" = '2028' THEN '05'
                WHEN "S"."GRAD-YR" = '2029' THEN '04'
                WHEN "S"."GRAD-YR" = '2030' THEN '03'
                WHEN "S"."GRAD-YR" = '2030' THEN '02'
                WHEN "S"."GRAD-YR" = '2031' THEN '01'
                WHEN "S"."GRAD-YR" = '2032' THEN 'KG'
                ELSE "S"."GRAD-YR"
                END "GRADE",

                "S"."GRAD-YR",
                "C"."SCHOOL-YEAR"

 

FROM "PUB"."STUDENT-ENTITY" AS "SE"
JOIN "PUB"."STUDENT" AS "S"
ON "SE"."STUDENT-ID" = "S"."STUDENT-ID"
JOIN "PUB"."NAME" AS "N"
ON "S"."NAME-ID" = "N"."NAME-ID"
JOIN "PUB"."STUDENT-CLASS" AS "SC"
ON "SE"."STUDENT-ID" = "SC"."STUDENT-ID"
JOIN "PUB"."COURSE" AS "C"
ON "SC"."COR-NUM-ID" = "C"."COR-NUM-ID"

WHERE "C"."SCHOOL-YEAR" = '2021'
ORDER BY "S"."OTHER-ID"

