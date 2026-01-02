# DSA210-Health-spending-and-Human-Well-Being
Analysis of the relationship between healthcare spending and human well-being using real-world data from international sources.

# Motivation

I found this topic interesting and wanted to work on it because in many countries, the cost of healthcare has been increasing over the past years. I also observe in my personal environment that some people postpone medical check-ups due to rising expenses. This raised an important question for me: How does health spending relate to people’s well-being and health outcomes across different countries?
To explore this, I decided to analyze international data on healthcare expenditure, life expectancy, and life satisfaction.

# Data Sources

All datasets were obtained from Our World in Data (OWID):  
                                                          Variable                                              	Dataset	                                                      Source
                                                       Life Satisfaction	                                    gdp-vs-happiness.csv	                                   Wellbeing Research Centre (2025)
                                                       Health Expenditure                                     annual-healthcare-expenditure-per-capita.csv	           WHO Global Health Expenditure Database (2025)
                                                       Life Expectancy	                                      life-expectancy.csv	                                     UN / Human Mortality Database (2024)
                                                       Out-of-Pocket Share (% of total health expenditure)    share-of-out-of-pocket-expenditure-on-healthcare.csv     WHO Global Health Expenditure Database (2025)

All datasets include country-year level observations and were merged using Entity and Year keys.

# Method
This project uses: Data merging (inner join on country & year), Descriptive statistics, Correlation analysis ,Scatterplots, Simple Linear Regression (OLS).The analysis was performed in Python (pandas, seaborn, statsmodels).

# My hypothesis

My initial expectation is that in countries where the healthcare sector becomes more expensive (and requires high per-capita spending), people’s access to medical services decreases due to financial burden, which in turn would negatively affect their personal health and overall life quality.

# Data Integration & Exploratory Analysis (EDA)

After merging the four datasets, the final combined dataset contains: 1675 observations, 7 key variables: country, year, health_expenditure, life_expectancy, life_satisfaction, gdp_per_capita, out_of_pocket_share

# Correlation Results
Relationship	                                  Pearson r	                                           Interpretation
Health Expenditure → Life Expectancy             	0.87	                                        Very strong positive correlation
Health Expenditure → Life Satisfaction	          0.75	                                        Strong positive correlation
Out-of-Pocket Share → Life Expectancy	           −0.47	                                        Moderate negative
Out-of-Pocket Share → Life Satisfaction	         −0.48	                                        Moderate negative
 

# Visual Evidence
Shows a strong, nonlinear (logarithmic-like) increase.
![Health Expenditure vs Life Satisfaction](https://github.com/user-attachments/assets/cff33a3d-c2be-484f-be96-803a5ab1b628)
![Health Expenditure vs Life Expectancy](https://github.com/user-attachments/assets/7f753e1e-7111-458d-8205-c54d94235321)
![Out-of-Pocket vs Life Expectancy](https://github.com/user-attachments/assets/10f737cb-dae8-43cf-a0dd-f0b9c9c5583b)
![Out-of-Pocket vs Life Satisfaction](https://github.com/user-attachments/assets/a50b8665-7978-4104-a06c-affef1256410)

# Hypothesis Testing (Regression Analysis)

Health Expenditure → Life Expectancy
R² = 0.490
p-value < 0.001
Conclusion: Highly statistically significant
Interpretation:
Health expenditure explains nearly half of the variation in average life expectancy across countries.

Health Expenditure → Life Satisfaction
R² = 0.567
p-value < 0.001
Conclusion: Also highly significant
Interpretation:
Healthcare spending actually explains more of life satisfaction variance than life expectancy.

Out-of-Pocket Share → Life Expectancy
R² = 0.178
p-value < 0.001
Interpretation:
A higher out-of-pocket burden significantly reduces life expectancy. 
Countries where people pay more from their own pockets tend to have shorter lifespans.

Out-of-Pocket Share → Life Satisfaction
R² = 0.226
p-value < 0.001
Interpretation:
Out-of-pocket burden strongly lowers the personal well-being of citizens.


# Conclusion
The original hypothesis about "higher healthcare prices reducing well-being" While total health expenditure showed a positive association with well-being, out-of-pocket financial burden showed the opposite effect. This means that high spending countries achieve better health ONLY when the spending is not carried by individuals. When healthcare becomes financially burdensome, well-being declines.

Higher out-of-pocket burden:
– significantly reduces life expectancy (p < 0.001)
– significantly reduces life satisfaction (p < 0.001)

This means that when healthcare becomes financially inaccessible, well-being declines.

# Implication

This suggests that global health funds should be prioritized for low-spending countries, where each dollar has dramatically more impact.

# Machine Learning Analysis 

I implemented a Linear Regression model to specifically investigate the relationship between healthcare investment and longevity.Model Implementation:

Target Variable: Life Expectancy 

Feature: Current Health Expenditure per Capita.

Methodology: The data was cleaned of null values and split into training (80%) and testing (20%) sets to validate the model's predictive performance.Key Results:Model Performance ($R^2$ Score): 0.4143.Mean 

Squared Error (MSE): 45.18.

Findings: The model confirms a clear positive correlation. As healthcare expenditure per capita increases, there is a statistically significant upward trend in life expectancy.

Visualization: The regression plot shows that while spending is a strong driver for longer life, the gains tend to stabilize at extremely high spending levels, suggesting a point of diminishing returns.
