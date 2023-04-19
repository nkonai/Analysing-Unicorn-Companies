#!/usr/bin/env python
# coding: utf-8

# ![Hand with calculator](calculator.png "Calculator")
# 
# Did you know that the average return from investing in stocks is 10% per year! But who wants to be average?! 
# 
# You have been asked to support an investment firm by analyzing trends in high-growth companies. They are interested in understanding which industries are producing the highest valuations and the rate at which new high-value companies are emerging. Providing them with this information gives them a competitive insight as to industry trends and how they should structure their portfolio looking forward.
# 
# You have been given access to their `unicorns` database, which contains the following tables:
# 
# `dates`
# | Column       | Description                                  |
# |------------- |--------------------------------------------- |
# | company_id   | A unique ID for the company.                 |
# | date_joined  | The date that the company became a unicorn.  |
# | year_founded | The year that the company was founded.       |
# 
# `funding`
# | Column           | Description                                  |
# |----------------- |--------------------------------------------- |
# | company_id       | A unique ID for the company.                 |
# | valuation        | Company value in US dollars.                 |
# | funding          | The amount of funding raised in US dollars.  |
# | select_investors | A list of key investors in the company.      |
# 
# `industries`
# | Column       | Description                                  |
# |------------- |--------------------------------------------- |
# | company_id   | A unique ID for the company.                 |
# | industry     | The industry that the company operates in.   |
# 
# `companies`
# | Column       | Description                                       |
# |------------- |-------------------------------------------------- |
# | company_id   | A unique ID for the company.                      |
# | company      | The name of the company.                          |
# | city         | The city where the company is headquartered.      |
# | country      | The country where the company is headquartered.   |
# | continent    | The continent where the company is headquartered. |
# 

# In[ ]:





# In[1]:


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

