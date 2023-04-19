
WITH top_industries AS (
	SELECT industry, COUNT(industries.company_id) AS num_unicorns
	FROM industries
	LEFT JOIN dates ON dates.company_id = industries.company_id
	WHERE EXTRACT( YEAR FROM dates.date_joined) IN (2019,2020,2021)
	GROUP BY industry
	ORDER BY num_unicorns DESC
	LIMIT 3
),

ranking_year AS (
	SELECT industry, EXTRACT(YEAR FROM date_joined) AS year, COUNT(industries.company_id) AS num_unicorns, ROUND(AVG(valuation)/1000000000,2) AS average_valuation_billions
	FROM industries
	LEFT JOIN dates ON dates.company_id = industries.company_id
	LEFT JOIN funding ON funding.company_id = industries.company_id
	GROUP BY industry, year
)
SELECT * FROM ranking_year
WHERE industry IN (SELECT industry FROM top_industries)
AND year IN (2021,2020,2019)
ORDER BY industry, year DESC

