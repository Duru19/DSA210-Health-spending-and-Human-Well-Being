# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 01:53:36 2025

@author: blgnd
"""

# -*- coding: utf-8 -*-
"""
DSA210 Term Project - Health Spending, Well-Being and Out-of-Pocket Burden
Created on Mon Nov 24 22:22:55 2025
@author: blgnd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

#download and read files
happiness_path = r"C:\Users\blgnd\Downloads\gdp-vs-happiness\gdp-vs-happiness.csv"
health_path    = r"C:\Users\blgnd\Downloads\annual-healthcare-expenditure-per-capita\annual-healthcare-expenditure-per-capita.csv"
life_path      = r"C:\Users\blgnd\Downloads\life-expectancy\life-expectancy.csv"
oopp_path = r"C:\Users\blgnd\Downloads\share-of-out-of-pocket-expenditure-on-healthcare\share-of-out-of-pocket-expenditure-on-healthcare.csv"

df_happiness = pd.read_csv(happiness_path)
df_health    = pd.read_csv(health_path)
df_life      = pd.read_csv(life_path)
df_oopp      = pd.read_csv(oopp_path)



df_oopp = df_oopp[[
    "Entity",
    "Year",
    "Out-of-pocket expenditure (% of current health expenditure)"
]].rename(columns={
    "Out-of-pocket expenditure (% of current health expenditure)": "out_of_pocket_share"
})

#merging datas
merged = df_happiness.merge(
    df_health,
    on=["Entity", "Year"],
    how="inner"
)

merged = merged.merge(
    df_life,
    on=["Entity", "Year"],
    how="inner"
)


merged = merged.merge(
    df_oopp,
    on=["Entity", "Year"],
    how="inner"
)


merged = merged[[
    "Entity",
    "Year",
    "Cantril ladder score",
    "GDP per capita, PPP (constant 2021 international $)",
    "Current health expenditure per capita, PPP (current international $)",
    "Period life expectancy at birth",
    "out_of_pocket_share"
]]

merged = merged.rename(columns={
    "Entity": "country",
    "Year": "year",
    "Cantril ladder score": "life_satisfaction",
    "GDP per capita, PPP (constant 2021 international $)": "gdp_per_capita",
    "Current health expenditure per capita, PPP (current international $)": "health_expenditure",
    "Period life expectancy at birth": "life_expectancy"
})


merged.dropna(inplace=True)


print("merged data (merged.head()):")
print(merged.head())
print("\nShape:", merged.shape)

print("\n merge shape control")
print(f"Rows: {merged.shape[0]}")

print("\n statics ---")
print(merged[['life_satisfaction',
              'health_expenditure',
              'life_expectancy',
              'out_of_pocket_share']].describe())

print("\n correlation matrix ")
correlation_matrix = merged[['life_satisfaction',
                             'health_expenditure',
                             'life_expectancy',
                             'out_of_pocket_share']].corr()
print(correlation_matrix)

#EDA – PLOTS

#Health Expenditure vs. Life Expectancy
plt.figure(figsize=(10, 6))
sns.scatterplot(x='health_expenditure', y='life_expectancy', data=merged)
plt.title('Health Expenditure vs. Life Expectancy')
plt.xlabel('Health Expenditure Per Capita (USD)')
plt.ylabel('Life Expectancy (Years)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Health Expenditure vs. Life Satisfaction
plt.figure(figsize=(10, 6))
sns.scatterplot(x='health_expenditure', y='life_satisfaction', data=merged)
plt.title('Health Expenditure vs. Life Satisfaction')
plt.xlabel('Health Expenditure Per Capita (USD)')
plt.ylabel('Cantril Life Satisfaction Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Out-of-pocket (%) vs Life Expectancy
plt.figure(figsize=(10, 6))
sns.scatterplot(x='out_of_pocket_share', y='life_expectancy', data=merged)
plt.title('Out-of-Pocket Share vs. Life Expectancy')
plt.xlabel('Out-of-Pocket Share of Health Spending (%)')
plt.ylabel('Life Expectancy (Years)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Out-of-pocket (%) vs Life Satisfaction
plt.figure(figsize=(10, 6))
sns.scatterplot(x='out_of_pocket_share', y='life_satisfaction', data=merged)
plt.title('Out-of-Pocket Share vs. Life Satisfaction')
plt.xlabel('Out-of-Pocket Share of Health Spending (%)')
plt.ylabel('Cantril Life Satisfaction Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#hypothesis testing
print("\n hypothesis testing: Health Expenditure -> Yaşam Süresi ---")
model_life = smf.ols('life_expectancy ~ health_expenditure', data=merged)
results_life = model_life.fit()
print(results_life.summary())

print("\n hypothesis testing: Health Expenditure -> Life Satisfaction")
model_happiness = smf.ols('life_satisfaction ~ health_expenditure', data=merged)
results_happiness = model_happiness.fit()
print(results_happiness.summary())

print("\n hypothesis testing: Out-of-pocket -> Life Expectancy ")
model_life_oopp = smf.ols('life_expectancy ~ out_of_pocket_share', data=merged)
results_life_oopp = model_life_oopp.fit()
print(results_life_oopp.summary())

print("\n hypothesis testing: Out-of-pocket -> Life Satisfaction")
model_happiness_oopp = smf.ols('life_satisfaction ~ out_of_pocket_share', data=merged)
results_happiness_oopp = model_happiness_oopp.fit()
print(results_happiness_oopp.summary())
