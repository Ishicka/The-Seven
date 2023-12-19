# Project Title: Analyzing the Housing Market and Economic factors. 
#  Project Goals:
The primary goal of this project is to analyze the housing market, focusing on the Affordability Index, median sale price (demand), and median list price (supply). Additionally, economic factors such as mortgage interest rates and unemployment rates will be considered. The project aims to provide insights into the current state of the housing market and understand the relationship between affordability, demand, and supply, considering economic factors.

#  Industry Relevance:
This project is essential in the real estate industry as it addresses critical factors influencing the housing market. Stakeholders, including real estate agents, buyers, sellers, and policymakers, can benefit from understanding market trends and factors affecting housing affordability.

#  Data Collection and Exploration:
Data Source: The project utilizes a combination of public datasets, including median list price and median sale price, mortgage interest rates, and unemployment rates.
Data Selection Rationale: The chosen datasets provide comprehensive information on housing market dynamics and economic factors, allowing for a holistic analysis.
Collection Process: Data was obtained from reputable sources such as Zillow, US Census and Freddie Mac website.
# Data preprocessing
The dataset contains monthly data from 2008 to 2023. The dataset contains multiple variables which include essential economic indicators and market data relevant for understanding housing market dynamics. The diverse sources from which the variables were obtained, the data preparation process involved merging the information based on their corresponding date columns The data pre-processing phase involved several stages, including the treatment of missing values (“NaN”).  
The Linear interpolation method:
The Linear interpolation method was used to address missing value by estimating the value of a function between two known values. This technique assumes that the relationship between the two known values is linear, meaning that it follows a straight line. The formula essentially finds the slope between the two points and uses it to estimate the value at the desired point x.

# Addressing outliers:
The interquartile range (IQR) method was employed to detect outliers in the dataset. For each feature in the dataset, the IQR was calculated separately, thus allowing the lower and upper bounds of the outliers for each feature to be determined. Based on the determination the outliers were kept in the Analysis because it provides valuable insights.

# Project Approach:
The analysis involves statistical methods and data visualization techniques to present trends and relationships. Python libraries like Pandas, NumPy, and Matplotlib/Seaborn were employed for data manipulation and visualization. Regression analysis was used to model the relationship between housing metrics and economic factors.

# Results/Conclusions:
The Analysis was divided into 3 sections to answer the following questions:
-	What does housing affordability look like in the US?
-	How significantly does the price of a home change from list price to sale price?
-	What relationships exist between markers of economic performance and number of homes sold?
Housing prices typically exhibit nonlinear connections owing to the effects of various economic indicators.
1.	Nonlinear Connections:
•	Nonlinearity implies that the relationship between housing prices and economic indicators is not proportional or straightforward. Changes in economic indicators may not result in linear changes in housing prices. Instead, the connection may be characterized by curves, thresholds, or other non-linear patterns.
2.	Complex Dynamics:
•	The housing market is influenced by a complex interplay of supply and demand dynamics, investor behavior, government policies, and global economic trends. These factors can create intricate and nonlinear relationships.
3.	Effects of Various Economic Indicators:
•	Housing prices are influenced by a multitude of economic indicators. These indicators use in our Analysis was Mortgage Rates and Unemployment 
•	Interest rates, for example, can have a nonlinear impact on housing prices. Initially, lower interest rates may stimulate demand and increase prices, but excessively low rates may lead to economic instability, affecting housing prices in unexpected ways.

# Housing Affordability Index

# Median List Price and Median Sale Price Analysis
Housing prices are greatly influenced by the balance between supply and demand. To get an understanding of this Dynamic Housing market we completed different analyses. 

# Outlier 
![Boxplot Outliers_plot](https://github.com/Ishicka/The-Seven/assets/148410176/5383b42c-c602-4d23-adb3-305ac12d3d80)


Box plots visually represent the distribution of data and identify outliers. Outliers are the points that fall beyond the "whiskers" of the box plot. Based on the context of our study, the nature of the data, and the goals of your analysis keeping the outliers is beneficial as they essential for understanding the phenomena being studied. A sample of the outlier was reviewed and all the regions listed are expected to have higher house Prices




# Price Distribution – Kernel Density distribution map 

 

The overlaid plot shows the distributions of the median sale price (in blue) and the median list price (in orange) within the same graph. This visualization allows for a direct comparison between the two distributions, highlighting similarities and differences in their frequency and range.

<img width="418" alt="Screenshot 2023-12-18 213036" src="https://github.com/Ishicka/The-Seven/assets/52751074/b1e3ffa4-f45c-443a-baa0-b4ce1ab8f6a2">


The summary statistics you provided represent the central tendency (mean) and variability (standard deviation) of Median List Price and Median Sale Price. 
For Median List Price:
•	Mean (Average): $278,590.74
•	Standard Deviation: $174,552.93
For Median Sale Price:
•	Mean (Average): $236,321.50
•	Standard Deviation: $141,586.75
The standard deviation is lower in both variables which suggests less variability in the data. This Basically means the data points are more clustered around the average value. When the standard deviation is lower, it means that the values in the data set are closer to the mean (average) and there is less spread around the mean. 
Variability refers to the extent to which data points in a dataset differ from each other or from the average (mean) value. In statistics, variability is a measure of the spread, dispersion, or range of a set of values. It provides information about how much individual data points deviate from the central tendency of the data.



# Trend Analysis

 
![Median Sales Prices_plot](https://github.com/Ishicka/The-Seven/assets/148410176/a4377d01-bbd4-46b4-b00c-723d08328f1f)



The plot reviews the Median list price versus the Median sale price for California ,Texas and Kansas.  There is an upward trend in both the sales and listing price for each state being reviewed. Specifically in California the plot reflects that buyers are paying less than the Median list price hence, the time period being analyzed draws the conclusion that they are in the buyers market.Buyer's market means that the demand for houses are less than the actual supply which creates negotiation power. Kansas on the other hand shows a multiple overlaps in 2021 and 2022 reflecting a possible shift in the market from buyers to sellers’ market .




# Correlation Analysis:

![Scatter Plot of MLP vs MSP_plot](https://github.com/Ishicka/The-Seven/assets/148410176/f7d15490-e17e-4d92-be31-4a0e1f419cfb)

 
•	Linear Regression: y = 0.79x + 12647.59
•	Correlation Coefficient: 0.96
•	A strong positive correlation - indicates that when the median list price of homes increases, the median sale price also tends to increase, and vice versa. In other words, there is a consistent pattern of both list prices and sale prices moving in the same direction as reflected in the graph.
•	This correlation is often observed in real estate markets. When sellers perceive that the market is strong and property values are high, they may list their homes at higher prices. If buyers are willing to pay those prices, it results in higher median sale prices. Conversely, in a weaker market, sellers may be more inclined to lower their list prices, leading to lower median sale prices.
•	It's important to note that correlation does not imply causation. While there may be a strong statistical relationship between these two variables, other factors could influence both list and sale prices independently. 

# Economic Factors
![image](https://github.com/Ishicka/The-Seven/assets/148410176/bce3d5d4-8935-48ef-b77e-52f651b2bd84)




The initial analysis indicates a modest correlation between HAI and overall housing market trends, with a particular focus on the relationship between home sales volume and various economic factors. Notably, housing prices are influenced by a range of economic indicators such as inflation, employment rates, GDP growth, and consumer confidence, with interest rates playing a complex role. An inverse relationship between home sales and mortgage interest rates is observed, highlighting that while lower interest rates can boost demand and prices, too low rates may lead to economic instability and unpredictably impact housing prices. Historical events, including the 2008 Housing Bubble and its aftermath, the post-recession recovery efforts, and the recent COVID-19 pandemic, have significantly influenced the market. These events demonstrate the housing market's sensitivity to broader economic and policy changes. Despite some correlations, as shown in the data, the housing market's complexity and the multitude of influencing factors make it challenging to predict trends reliably.

#Overall Points 

# Next Steps:
Potential next steps for the project include:

Incorporating more granular data (e.g., regional or city-specific data).
Analyzing the impact of other economic indicators.
Building predictive models for housing market trends.
Collaborating with industry experts for a more nuanced analysis.
In summary, this project offers valuable insights into the housing market, aiding stakeholders in making informed decisions. Continued refinement and expansion of the analysis will enhance its applicability and usefulness in the real estate industry.

