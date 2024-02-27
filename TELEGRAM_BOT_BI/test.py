import asyncio

from database.db import async_select_one

query = """SELECT
            report_date,
            cases - LAG(cases, 1, 0) OVER (ORDER BY report_date) AS daily_cases,
            deaths - LAG(deaths, 1, 0) OVER (ORDER BY report_date) AS daily_deaths,
            recovered - LAG(recovered, 1, 0) OVER (ORDER BY report_date) AS daily_recovered
            FROM covid_cases
            ORDER BY report_date desc
            limit 1"""
cases = asyncio.run(async_select_one(query))
print(cases)
print(type(cases))
