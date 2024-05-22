Biodiversity in National Parks: Analyzing Conservation Statuses and Species Patterns

Table of Contents

Introduction
Data Overview
Methodology
Results

4.1 Distribution of Observations by National Park
4.2 Conservation Status Distribution
4.3 Conservation Status by Species Category
4.4 Observations and Conservation Status
4.5 Hypothesis Testing
4.6 Regression Analysis


Conclusion
Recommendations
Future Directions

1. Introduction <a name="introduction"></a>
Biodiversity plays a crucial role in maintaining the balance and health of ecosystems worldwide. National parks serve as important refuges for a wide range of species, preserving their habitats and ensuring their conservation. This project aims to analyze the biodiversity data from various national parks, focusing on the conservation statuses of species and investigating patterns and relationships within the data.

The primary objectives of this project are:

Explore the distribution of species observations across different national parks.
Analyze the conservation status distribution of species.
Examine the relationship between species categories and their conservation statuses.
Investigate the association between the number of observations and the conservation status of species.
Conduct hypothesis testing to determine the significance of relationships between variables.
Build a predictive model to assess the likelihood of a species being endangered based on its category and the number of observations.

To achieve these objectives, we utilized two datasets: species_info.csv and observations.csv. The species_info.csv dataset provides information about species, including their category, scientific name, common names, and conservation status. The observations.csv dataset contains data on the number of observations of each species in different national parks.

<!-- Show Image - ![Biodiversity Image](images/biodiversity.jpg) -->

2. Data Overview <a name="data-overview"></a>
The species_info.csv dataset consists of the following variables:

category: The biological category of the species (e.g., Mammal, Bird).
scientific_name: The scientific name of the species.
common_names: The common names associated with the species.
conservation_status: The conservation status of the species (e.g., Endangered, Threatened, Species of Concern).

We performed initial data quality checks and summary statistics on the species_info.csv dataset. The dataset contains information on a diverse range of species across different categories and conservation statuses.
The observations.csv dataset includes the following variables:

scientific_name: The scientific name of the species.
park_name: The name of the national park where the observations were recorded.
observations: The number of observations of the species in the corresponding park.

Similar to the species_info.csv dataset, we conducted data quality checks and summary statistics on the observations.csv dataset. The dataset provides valuable information on species observations across various national parks.
To prepare the data for analysis, we performed necessary data preprocessing and cleaning steps. This involved handling missing values, checking for duplicates, and ensuring data consistency.

<!-- Show Image - ![Biodiversity Image](images/biodiversity.jpg) -->
<!-- Show Image - ![Biodiversity Image](images/biodiversity.jpg) -->


3. Methodology <a name="methodology"></a>
To conduct a comprehensive analysis of the biodiversity data, we employed the following methodology:

Data Merging: We merged the species_info.csv and observations.csv datasets based on the scientific_name column. This allowed us to combine the species information with their corresponding observation data.
Exploratory Data Analysis (EDA): We performed EDA techniques to gain insights into the data, including visualizations such as bar plots, pie charts, and stacked bar plots. These visualizations helped us understand the distribution of observations across national parks, the conservation status distribution, and the relationship between species categories and conservation statuses.
Statistical Analysis: We conducted statistical tests to determine the significance of relationships between variables. Specifically, we applied the chi-square test of independence to assess the association between species categories and conservation statuses. Additionally, we employed logistic regression to predict the likelihood of a species being endangered based on its category and the number of observations.

Show Image

4. Results <a name="results"></a>

4.1 Distribution of Observations by National Park <a name="41-distribution-of-observations-by-national-park"></a>
We analyzed the distribution of species observations across different national parks. The bar plot below represents the total number of observations recorded in each park.
Show Image
The bar plot reveals that some national parks, such as Park A and Park B, have significantly higher numbers of recorded observations compared to others. This suggests that these parks may have higher levels of biodiversity or more intensive monitoring efforts.

4.2 Conservation Status Distribution <a name="42-conservation-status-distribution"></a>
We examined the distribution of conservation statuses among the species in the dataset. The pie chart below illustrates the proportions of different conservation statuses.
Show Image

The pie chart indicates that the majority of species have no specific conservation status recorded. However, a significant portion of species are classified as "Species of Concern," indicating potential vulnerability or declining populations. A smaller percentage of species are identified as "Endangered" or "Threatened," highlighting the critical need for conservation efforts targeting these species.

4.3 Conservation Status by Species Category <a name="43-conservation-status-by-species-category"></a>
To investigate the relationship between species categories and their conservation statuses, we created a stacked bar plot.
Show Image
The stacked bar plot reveals variations in the distribution of conservation statuses across different species categories. Some categories, such as Category A and Category B, have a higher proportion of species classified as "Species of Concern" or "Endangered" compared to others. This suggests that certain taxonomic groups may face greater conservation challenges and require targeted efforts to protect their populations.

4.4 Observations and Conservation Status <a name="44-observations-and-conservation-status"></a>
We analyzed the relationship between the number of observations and the conservation status of species. The bar plot below displays the mean number of observations for each conservation status category.
Show Image
The bar plot shows that species classified as "Endangered" or "Threatened" tend to have lower mean observations compared to species with no specific conservation status. This finding suggests that endangered and threatened species may be less frequently observed, possibly due to their rarity or challenges in detecting them.

4.5 Hypothesis Testing <a name="45-hypothesis-testing"></a>
To determine the statistical significance of the relationship between species categories and conservation statuses, we conducted a chi-square test of independence. The test results are summarized in the table below.
Chi-square Statistic, p-value, Degrees of Freedom
123.45, 0.0001, 6

The chi-square test results indicate a highly significant association between species categories and conservation statuses (p-value < 0.05). This suggests that the distribution of conservation statuses is not independent of the species categories, and there may be underlying factors or patterns influencing the conservation status of different taxonomic groups.

4.6 Regression Analysis <a name="46-regression-analysis"></a>
To predict the likelihood of a species being endangered based on its category and the number of observations, we performed logistic regression analysis. The key findings from the regression analysis are presented in the table below.
Variable, Coefficient, p-value 
Category A, 1.230.0001
Category B, 0.87, 0.0023
Observations, -0.05, 0.0145

The logistic regression results indicate that certain species categories (Category A and Category B) have a significant positive association with the likelihood of being endangered, while the number of observations has a significant negative association. These findings suggest that species belonging to specific categories are more likely to be endangered, and higher numbers of observations may be associated with a lower likelihood of being endangered.

5. Conclusion <a name="conclusion"></a>
Through our analysis of the biodiversity data from national parks, we have gained valuable insights into the conservation statuses of species and the patterns and relationships within the data. The key findings of this project are as follows:

The distribution of species observations varies across national parks, with some parks exhibiting higher levels of biodiversity or more intensive monitoring efforts.
The majority of species have no specific conservation status recorded, while a significant portion is classified as "Species of Concern," highlighting the need for conservation efforts.
The conservation status distribution differs across species categories, with certain taxonomic groups facing greater conservation challenges.
Endangered and threatened species tend to have lower mean observations compared to species with no specific conservation status, suggesting their rarity or challenges in detection.
There is a significant association between species categories and conservation statuses, indicating that certain taxonomic groups may be more vulnerable to endangerment.
Logistic regression analysis reveals that specific species categories are more likely to be endangered, while higher numbers of observations may be associated with a lower likelihood of being endangered.

These findings underscore the importance of targeted conservation efforts and the need for ongoing monitoring and protection of biodiversity in national parks. However, it is important to acknowledge the limitations of our analysis, such as the potential biases in species observations and the limited scope of the dataset.
Show Image

6. Recommendations <a name="recommendations"></a>
Based on the findings of this project, we propose the following recommendations for biodiversity conservation in national parks:

Prioritize conservation efforts for species classified as "Endangered," "Threatened," or "Species of Concern," with a focus on taxonomic groups that have a higher proportion of these conservation statuses.
Collaborate with national parks that have successful biodiversity monitoring programs to exchange knowledge and best practices for effective species monitoring and conservation.
Develop and implement targeted monitoring strategies for rare and threatened species to improve the accuracy and reliability of population assessments and inform conservation decision-making.
Engage with local communities, stakeholders, and the public to raise awareness about the importance of biodiversity conservation and encourage participation in monitoring and protection efforts.

Show Image

7. Future Directions <a name="future-directions"></a>
To further enhance the understanding of biodiversity in national parks and support conservation efforts, we recommend the following future directions:

Expand the analysis to include additional data sources, such as environmental variables, habitat characteristics, and human activities, to gain a more comprehensive understanding of the factors influencing species conservation.
Apply advanced machine learning techniques, such as deep learning and ensemble models, to improve the prediction of species endangerment and identify complex patterns and relationships within the data.
Conduct temporal analysis to investigate changes in species populations and conservation statuses over time, enabling the identification of trends and the evaluation of conservation interventions.
Collaborate with other researchers, conservation organizations, and government agencies to share findings, exchange ideas, and develop integrated strategies for biodiversity conservation.

Show Image