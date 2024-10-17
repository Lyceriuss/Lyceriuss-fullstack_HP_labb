## SQL-Query 1

SELECT * 
FROM geografi.tabelldata 
LIMIT 10;

SE, IND, MT 

## Visar vilka länder dina videos ses från (Vart är MT?)

---------------------------------------------

## SQL-Query 2
SELECT strftime('%Y-%m', Datum) AS month, 
       SUM(visningar) AS total_views_per_month
FROM enhetstyp.totalt
GROUP BY month
ORDER BY month;

## Trafiken på kanalen dvs två månader online 08-09
1275 i augusti och 777 i september.

---------------------------------------------
## SQL-Query 3

SELECT "Tittarnas ålder", AVG("Genomsnittlig procent som har visats (%)") AS avg_percentage_watched
FROM tittare.tabelldata_kon
GROUP BY "Tittarnas ålder"
ORDER BY avg_percentage_watched DESC;

## åldersdemografin på de människorna som tittar på videos Bara 3 ålders brackets? hmm, varför inte 18-25 år?


---------------------------------------------
## SQL-Query 4

SELECT Videotitel, SUM(Visningstid_timmar) AS total_viewing_hours
FROM marts.content_view_time
GROUP BY Videotitel
ORDER BY total_viewing_hours DESC;

## Din Marts!Antar att du gjort denna själv Kokchun? Snyggt! 

---------------------------------------------

## SQL-Query 5 create marts

CREATE TABLE marts.age_demographic_summary AS
SELECT 
    t."Tittarnas ålder" AS age_group,
    SUM(t."Visningar (%)") AS total_views_percentage,
    AVG(t."Genomsnittlig procent som har visats (%)") AS avg_percentage_watched,
    AVG(EXTRACT(EPOCH FROM t."Genomsnittlig visningslängd") / 60) AS avg_minutes_watched
FROM tittare.tabelldata_kon t
GROUP BY t."Tittarnas ålder"
ORDER BY t."Tittarnas ålder" ASC;

## Visar demografi
s
