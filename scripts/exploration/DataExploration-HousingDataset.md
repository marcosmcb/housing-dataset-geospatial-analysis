Ireland Housing - Exploratory Data Analysis - EDA
================
Marcos Cavalcante
2023-04-25

- <a href="#exploratory-data-analysis"
  id="toc-exploratory-data-analysis">Exploratory Data Analysis</a>
  - <a href="#installing-libraries" id="toc-installing-libraries">Installing
    libraries</a>
- <a href="#summary-statistics" id="toc-summary-statistics">Summary
  Statistics</a>
- <a href="#data-distribution-and-relationship"
  id="toc-data-distribution-and-relationship">Data Distribution and
  Relationship</a>
  - <a href="#house-price-the-target-variable"
    id="toc-house-price-the-target-variable">House Price, the target
    variable</a>
    - <a href="#histogram-of-price" id="toc-histogram-of-price">Histogram of
      Price</a>
  - <a href="#correlation-matrix" id="toc-correlation-matrix">Correlation
    Matrix</a>
  - <a href="#analysing-relationship-between-house-price-and-size"
    id="toc-analysing-relationship-between-house-price-and-size">Analysing
    relationship between house price and size</a>
  - <a
    href="#analysing-relationship-between-house-price-and-number-of-bathrooms"
    id="toc-analysing-relationship-between-house-price-and-number-of-bathrooms">Analysing
    relationship between house price and number of bathrooms</a>
  - <a
    href="#analysing-relationship-between-house-price-and-number-of-bedrooms"
    id="toc-analysing-relationship-between-house-price-and-number-of-bedrooms">Analysing
    relationship between house price and number of bedrooms</a>
  - <a
    href="#analysing-relationship-between-house-price-and-nearest-education-centres"
    id="toc-analysing-relationship-between-house-price-and-nearest-education-centres">Analysing
    relationship between house price and nearest education centres</a>
  - <a href="#analysing-factor-variables---anova-p-value-and-f-value"
    id="toc-analysing-factor-variables---anova-p-value-and-f-value">Analysing
    factor variables - ANOVA, p-value and f-value</a>
    - <a href="#property-type" id="toc-property-type">Property Type</a>
    - <a href="#county" id="toc-county">County</a>
    - <a href="#ber-rating" id="toc-ber-rating">BER Rating</a>
    - <a href="#town-or-neighbourhood" id="toc-town-or-neighbourhood">Town or
      Neighbourhood</a>
- <a href="#data-visualisation" id="toc-data-visualisation">Data
  Visualisation</a>
  - <a href="#property-price" id="toc-property-price">Property Price</a>
    - <a href="#box-plot-property-type-by-price"
      id="toc-box-plot-property-type-by-price">Box-Plot Property Type by
      Price</a>
    - <a href="#frequency-plot-property-type-by-price"
      id="toc-frequency-plot-property-type-by-price">Frequency Plot Property
      Type by Price</a>
  - <a href="#density-plot-of-county-and-house-price"
    id="toc-density-plot-of-county-and-house-price">Density Plot of County
    and House price</a>
- <a href="#spatial-visualisation" id="toc-spatial-visualisation">Spatial
  Visualisation</a>
  - <a href="#bubble-plot-of-property-type-by-county"
    id="toc-bubble-plot-of-property-type-by-county">Bubble Plot of Property
    Type by County</a>
  - <a href="#density-plot-of-count-of-houses-by-county"
    id="toc-density-plot-of-count-of-houses-by-county">Density Plot of Count
    of Houses by County</a>
  - <a href="#choropleth-map-of-mean-house-price-per-county"
    id="toc-choropleth-map-of-mean-house-price-per-county">Choropleth Map of
    Mean House Price per County</a>
  - <a href="#choropleth-map-of-mean-count-of-public-transport-per-county"
    id="toc-choropleth-map-of-mean-count-of-public-transport-per-county">Choropleth
    Map of Mean Count of Public Transport per County</a>
  - <a href="#choropleth-map-of-mean-count-of-education-centres-per-county"
    id="toc-choropleth-map-of-mean-count-of-education-centres-per-county">Choropleth
    Map of Mean Count of Education Centres per County</a>
  - <a href="#choropleth-map-of-mean-count-of-hospitals-per-county"
    id="toc-choropleth-map-of-mean-count-of-hospitals-per-county">Choropleth
    Map of Mean Count of Hospitals per County</a>
  - <a href="#choropleth-map-of-mean-count-of-garda-stations-per-county"
    id="toc-choropleth-map-of-mean-count-of-garda-stations-per-county">Choropleth
    Map of Mean Count of Garda Stations per County</a>
- <a href="#removing-outliers" id="toc-removing-outliers">Removing
  Outliers</a>
  - <a href="#z-score-implementation"
    id="toc-z-score-implementation">Z-Score Implementation</a>
  - <a href="#removal-of-outliers" id="toc-removal-of-outliers">Removal of
    Outliers</a>
  - <a href="#plotting-outliers-removed"
    id="toc-plotting-outliers-removed">Plotting Outliers Removed</a>
- <a href="#creating-dummy-vars" id="toc-creating-dummy-vars">Creating
  Dummy Vars</a>
- <a href="#removing-character-variables"
  id="toc-removing-character-variables">Removing Character variables</a>
  - <a href="#write-explored-dataset-to-disk"
    id="toc-write-explored-dataset-to-disk">Write Explored Dataset to
    disk</a>

# Exploratory Data Analysis

## Installing libraries

First step is to install and load the necessary libraries.

``` r
packages <- c("tidyverse", "haven", "devtools", "dplyr", 
              "ggplot2", "gapminder", "patchwork", "ggridges", 
              "corrplot", "gridExtra", "sf","tmap","rgdal","rgeos",
              "adehabitatHR", "knitr", "kableExtra", "geosphere", 
              "fastDummies", "janitor")

if(sum(as.numeric(!packages %in% installed.packages())) != 0){
  installer <- packages[!packages %in% installed.packages()]
  for(i in 1:length(installer)) {
    install.packages(installer, dependencies = T)
    break()
  }
  sapply(packages, require, character = T) 
} else {
  sapply(packages, require, character = T) 
}

devtools::install_github("ropensci/skimr")
webshot::install_phantomjs()

library(skimr)
```

# Summary Statistics

In this stage, the dataset will be looked at from many perspectives, the
target variable, **price**, will be looked at carefully when comparing
it with the other variables in the dataset.

The other variables in the dataset will also be analysed and some
feature engineering techniques may be used to derive other pieces of
data from them.

As an input in this step, the **ireland_houses_cleaned** dataframe will
be used as it was created in the previous notebook where the dataset was
cleaned.

Let’s start by using the skim library to have a glimpse of the dataset.

``` r
dataset_directory <- "../../datasets/"
dataset_filename <- paste(dataset_directory, "ireland_houses_cleaned.Rda", 
                          sep="")

load(file = dataset_filename) # loads ireland_houses dataframe

options(scipen = 999) # turn off scientific notation

skim(ireland_houses)
```

<table style="width: auto;" class="table table-condensed">
<caption>
Data summary
</caption>
<tbody>
<tr>
<td style="text-align:left;">
Name
</td>
<td style="text-align:left;">
ireland_houses
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of rows
</td>
<td style="text-align:left;">
9009
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
17
</td>
</tr>
<tr>
<td style="text-align:left;">
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
</td>
<td style="text-align:left;">
</td>
</tr>
<tr>
<td style="text-align:left;">
Column type frequency:
</td>
<td style="text-align:left;">
</td>
</tr>
<tr>
<td style="text-align:left;">
character
</td>
<td style="text-align:left;">
2
</td>
</tr>
<tr>
<td style="text-align:left;">
factor
</td>
<td style="text-align:left;">
4
</td>
</tr>
<tr>
<td style="text-align:left;">
numeric
</td>
<td style="text-align:left;">
11
</td>
</tr>
<tr>
<td style="text-align:left;">
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
</td>
<td style="text-align:left;">
</td>
</tr>
<tr>
<td style="text-align:left;">
Group variables
</td>
<td style="text-align:left;">
None
</td>
</tr>
</tbody>
</table>

**Variable type: character**

<table>
<thead>
<tr>
<th style="text-align:left;">
skim_variable
</th>
<th style="text-align:right;">
n_missing
</th>
<th style="text-align:right;">
complete_rate
</th>
<th style="text-align:right;">
min
</th>
<th style="text-align:right;">
max
</th>
<th style="text-align:right;">
empty
</th>
<th style="text-align:right;">
n_unique
</th>
<th style="text-align:right;">
whitespace
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
address
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
18
</td>
<td style="text-align:right;">
102
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
8871
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
location
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
4
</td>
<td style="text-align:right;">
61
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
118
</td>
<td style="text-align:right;">
0
</td>
</tr>
</tbody>
</table>

**Variable type: factor**

<table>
<thead>
<tr>
<th style="text-align:left;">
skim_variable
</th>
<th style="text-align:right;">
n_missing
</th>
<th style="text-align:right;">
complete_rate
</th>
<th style="text-align:left;">
ordered
</th>
<th style="text-align:right;">
n_unique
</th>
<th style="text-align:left;">
top_counts
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
propertyType
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:left;">
FALSE
</td>
<td style="text-align:right;">
8
</td>
<td style="text-align:left;">
Det: 3440, Sem: 2278, Ter: 1427, Apa: 977
</td>
</tr>
<tr>
<td style="text-align:left;">
berRating
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:left;">
FALSE
</td>
<td style="text-align:right;">
17
</td>
<td style="text-align:left;">
C3: 1112, C1: 1086, C2: 1085, D1: 975
</td>
</tr>
<tr>
<td style="text-align:left;">
county
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:left;">
FALSE
</td>
<td style="text-align:right;">
26
</td>
<td style="text-align:left;">
DUB: 3303, COR: 1168, GAL: 533, WEX: 398
</td>
</tr>
<tr>
<td style="text-align:left;">
townOrNeighbourhood
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:left;">
FALSE
</td>
<td style="text-align:right;">
114
</td>
<td style="text-align:left;">
NOR: 780, SOU: 705, IBA: 592, COR: 561
</td>
</tr>
</tbody>
</table>

**Variable type: numeric**

<table>
<thead>
<tr>
<th style="text-align:left;">
skim_variable
</th>
<th style="text-align:right;">
n_missing
</th>
<th style="text-align:right;">
complete_rate
</th>
<th style="text-align:right;">
mean
</th>
<th style="text-align:right;">
sd
</th>
<th style="text-align:right;">
p0
</th>
<th style="text-align:right;">
p25
</th>
<th style="text-align:right;">
p50
</th>
<th style="text-align:right;">
p75
</th>
<th style="text-align:right;">
p100
</th>
<th style="text-align:left;">
hist
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
price
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
462485.76
</td>
<td style="text-align:right;">
556102.05
</td>
<td style="text-align:right;">
40000.00
</td>
<td style="text-align:right;">
245000.00
</td>
<td style="text-align:right;">
340000.00
</td>
<td style="text-align:right;">
495000.00
</td>
<td style="text-align:right;">
15000000.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
size
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
145.76
</td>
<td style="text-align:right;">
150.64
</td>
<td style="text-align:right;">
20.00
</td>
<td style="text-align:right;">
86.00
</td>
<td style="text-align:right;">
112.00
</td>
<td style="text-align:right;">
164.00
</td>
<td style="text-align:right;">
6109.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
bedrooms
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
3.43
</td>
<td style="text-align:right;">
1.35
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3.00
</td>
<td style="text-align:right;">
3.00
</td>
<td style="text-align:right;">
4.00
</td>
<td style="text-align:right;">
30.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
bathrooms
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
2.35
</td>
<td style="text-align:right;">
1.35
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
2.00
</td>
<td style="text-align:right;">
3.00
</td>
<td style="text-align:right;">
28.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
latitude
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
53.09
</td>
<td style="text-align:right;">
0.70
</td>
<td style="text-align:right;">
51.44
</td>
<td style="text-align:right;">
52.63
</td>
<td style="text-align:right;">
53.29
</td>
<td style="text-align:right;">
53.40
</td>
<td style="text-align:right;">
55.38
</td>
<td style="text-align:left;">
▂▂▇▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
longitude
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
-7.34
</td>
<td style="text-align:right;">
1.18
</td>
<td style="text-align:right;">
-10.35
</td>
<td style="text-align:right;">
-8.46
</td>
<td style="text-align:right;">
-6.80
</td>
<td style="text-align:right;">
-6.28
</td>
<td style="text-align:right;">
-6.01
</td>
<td style="text-align:left;">
▁▂▃▂▇
</td>
</tr>
<tr>
<td style="text-align:left;">
pricePerSqMeter
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
3402.62
</td>
<td style="text-align:right;">
1895.76
</td>
<td style="text-align:right;">
11.62
</td>
<td style="text-align:right;">
2061.40
</td>
<td style="text-align:right;">
2947.37
</td>
<td style="text-align:right;">
4326.92
</td>
<td style="text-align:right;">
41666.67
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
nearestHospitals
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
1.68
</td>
<td style="text-align:right;">
2.07
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3.00
</td>
<td style="text-align:right;">
7.00
</td>
<td style="text-align:left;">
▇▁▂▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
nearestGardaStations
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
9.34
</td>
<td style="text-align:right;">
9.78
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
2.00
</td>
<td style="text-align:right;">
4.00
</td>
<td style="text-align:right;">
14.00
</td>
<td style="text-align:right;">
31.00
</td>
<td style="text-align:left;">
▇▂▁▁▂
</td>
</tr>
<tr>
<td style="text-align:left;">
nearestEducationCentres
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
56.65
</td>
<td style="text-align:right;">
89.03
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
3.00
</td>
<td style="text-align:right;">
13.00
</td>
<td style="text-align:right;">
65.00
</td>
<td style="text-align:right;">
319.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
nearestPublicTransports
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
412.35
</td>
<td style="text-align:right;">
589.48
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
11.00
</td>
<td style="text-align:right;">
82.00
</td>
<td style="text-align:right;">
627.00
</td>
<td style="text-align:right;">
2024.00
</td>
<td style="text-align:left;">
▇▂▁▁▁
</td>
</tr>
</tbody>
</table>

At this point, the dataset has over 9000 thousand observations and 17
variables, where one of those is the **target** variable.

11 of those variables are of numeric type, 4 are of factor type and the
other 2 are of character type.

From the quick statistic summary above, it can be observed that:

- **Missing Values**: There are no missing values in the dataset, this
  is only the case because the dataset got fully cleaned in the Data
  Cleaning step.

- **Property Type**: There are 8 different property type. It will be
  interesting to find out how the house price is spread across property
  types.

- **County** and **townOrNeighbourhood**: Those are the equivalent to
  states or the area where the property is located. These variables will
  be helpful when analysing this dataset from spatial perspective.

- **Price**: As expected, around 75% of the houses are under the
  €495,000.00 mark. And the most expensive house costs €15.000.000,00.

- **Price Per Sq Meter**: The mean price per $sq^2$ meter is at
  €3,402.00, and the highest value is marked at €41,666.67

- **Size**: The majority of the houses are under 164 $sq^2$, there seems
  to be a clear outlier whose size is 6109 $sq^2$.

- **Bathrooms**: The variable shows some interesting behaviour, where
  the mean is about 2 bathrooms per house and the maximum number of
  bathrooms in a house is 28.

- **Bedrooms**: Similar to the *bathrooms* variable, **bedrooms** also
  show an interesting behaviour, the mean is 3 bedrooms per house and
  the maximum number of bedrooms is 30.

- **Nearest Hospitals**: About 75% of the observations have up to 3
  hospitals and that 50% of the houses have up to 1 hospital within a 10
  km radius.

- **Nearest Garda Stations**: The mean count of garda stations for the
  houses in the dataset is about 9 and, 50% of the houses have up to 4
  garda stations in a 10 km radius. At the other extreme, we find houses
  with up to 31 garda stations in a 10 km.

- **Nearest Education Centres**: The mean count of education centres for
  the houses in the dataset is around 56 and, 50% of the houses have up
  to 13 education centres in a 5 km radius. Some houses may have between
  65 to 319 education centres within a 5 km radius

- **Nearest Public Transports**: The mean count of public transports
  available for a house is 412 and 50% of the houses have up to 82
  public transport stops. Some extreme values can be seen too, where
  some houses have between 627 and 2024 public trasnport stops in a 5 km
  radius.

Each variable’s significance is described below:

| Variable                | Description                                                                          |
|-------------------------|--------------------------------------------------------------------------------------|
| address                 | A long form of the property address                                                  |
| bathrooms               | The number of bathrooms in this property                                             |
| bedrooms                | The number of bedrooms in this property                                              |
| berRating               | BER Rating of this property, i.e. A1, B2                                             |
| county                  | The county the property is in. Examples: “Co. Wicklow”, “Co. Kerry”                  |
| latitude                | The latitude of the property                                                         |
| location                | A short form of the property address area, i.e. Dublin 1, Co. Dublin                 |
| longitude               | The longitude of the property                                                        |
| nearestEducationCentres | Count on the number of schools and universities within a 5km radius of the house     |
| nearestGardaStations    | Count on the number of garda stations within a 10km radius of the house              |
| nearestHospitals        | Count on the number of hospitals within a 10km radius of the house                   |
| nearestPublicTransports | Count on the number of bus stops and train stations within a 5km radius of the house |
| price                   | The price of the property, in euro €                                                 |
| propertyType            | The type of the property, i.e. Apartment, End of Terrace, Semi-D, Terrace            |
| size                    | The size of the property in square meters                                            |
| townOrNeighbourhood     | The town or neighbourhood where is the property                                      |

# Data Distribution and Relationship

## House Price, the target variable

Let’s start by exploring the target variable, **price**. Price’s
histogram is going to be plotted below so it is possible to see the
amount of properties distributed across the price range.

### Histogram of Price

``` r
price_histogram_under_2mi <- ggplot(ireland_houses[ ireland_houses$price < 2000000, ], aes(x = price)) +
      geom_histogram(color = "darkblue", fill = "deepskyblue", bins = 30) +
      labs(title = "Histogram of house prices under € 2 million", x = "Price", y = "Observations") +
      scale_x_continuous(name = "Price", limits = c(0, 2000000)) +
      scale_fill_brewer() +
      theme(text=element_text(size = 20, face = "bold", family = "mono"))

price_histogram_above_2mi <- ggplot(ireland_houses[ ireland_houses$price >= 2000000, ], aes(x = price)) +
      geom_histogram(color = "darkblue", fill = "deepskyblue", bins = 30) +
      labs(title = "Histogram of house prices above € 2 million", x = "Price", y = "Observations") +
      scale_fill_brewer() +
      theme(text=element_text(size = 20, face = "bold", family = "mono"))

grid.arrange(price_histogram_under_2mi, price_histogram_above_2mi)
```

![](DataExploration-HousingDataset_files/figure-gfm/Histogram%20of%20Price-1.png)<!-- -->

Again, those results are expected as most of the houses are under
€495,000.00. Nevertheless, the histogram shows that there are some
observations that have a price of over €1,000,000.00, that might be an
early indication that our dataset is unbalanced as most of the
observations are under €500,000.00.

## Correlation Matrix

One way to understand the relationship among the variables in a dataset
is by calculating its correlation matrix. By doing that, you can see how
strongly the target variable in the dataset correlates with the other
variables and whether or not there are problems with multicollinearity -
which happens when other variables in the dataset have a high
correlation with each other - cancelling each other out when using
certain machine learning models.

At a later point, we start looking more carefully at the character
variables.

The correlation method used in this calculation is the **Pearson**
method.

``` r
correlation_matrix <- cor(select_if(ireland_houses, is.numeric))

corrplot( corr = correlation_matrix, 
          method = "color", 
          type = "lower", 
          order = "hclust", 
          addCoef.col = "black", 
          diag = FALSE, 
          tl.srt = 45, 
          tl.col = "black"
)
```

![](DataExploration-HousingDataset_files/figure-gfm/Correlation%20Matrix%20with%20New%20Features-1.png)<!-- -->

From the matrix correlation above, some important information can be
inferred:

- There is a **moderate positive correlation** between price and size as
  well as price and pricePerSqMeter, which may indicate that there a
  strong relationship between those variables.

- There is a **weak positive correlation** between price and - bathroom,
  bedroom, nearestHospitals, nearestGardaStations,
  nearestEducationCentres and nearestPublicTransports.

- There is also a **strong positive correlation** between bathrooms and
  bedrooms; and also amongst the socio-economic variables; which might
  be an early indication of multicollinearity.

## Analysing relationship between house price and size

``` r
create_lin_graph <- function(house_df, aest, labels) {
  lin_graph <- ggplot(data = house_df, aes(x = !!aest$x, y = !!aest$y)) +
        geom_point(col='deepskyblue') + 
        geom_smooth(formula = y ~ x, method = "lm", se=FALSE, color="orangered") +
        labs(title = labels$title, x = labels$x, y = labels$y) +
        scale_y_continuous(n.breaks = 15) +
        scale_x_continuous(n.breaks = 15) +
        theme(text=element_text(size = 15, face = "bold", family = "mono"))
  
  return (lin_graph)
}

under_2mi_house_price <- create_lin_graph(
  house_df = ireland_houses[ireland_houses$price < 2000000,],
  aest = list( x = sym("size"), y = sym("price") ),
  labels = list(title = "Under €2MI House Price by Size", x = "Size", y = "Price")
)

over_2mi_house_price <- create_lin_graph(
  house_df = ireland_houses[ireland_houses$price >= 2000000,],
  aest = list( x = sym("size"), y = sym("price") ),
  labels = list(title = "Over €2MI House Price by Size", x = "Size", y = "Price")
)

under_2k_house_size <- create_lin_graph(
  house_df = ireland_houses[ireland_houses$size < 2000,],
  aest = list( x = sym("size"), y = sym("price") ),
  labels = list(title = "All House Price by Size under 2K", x = "Size", y = "Price")
)


grid.arrange(under_2mi_house_price, over_2mi_house_price, under_2k_house_size) 
```

![](DataExploration-HousingDataset_files/figure-gfm/Analysing%20relationship%20between%20house%20price%20and%20size-1.png)<!-- -->

The plots above reveal us many interesting things, for example:

- The presence of outliers:
  - As it was shown before, there are some very expensive houses in the
    dataset, the most expensive ones stand out in the graph, for
    example: a house costing about €15 million euro and other two houses
    costing €12 and €10.5 million euro respectively.
  - It can also be seen that some houses have a large property area,
    such as 3,500, 4,000 and 6,000 $sq^2$.

## Analysing relationship between house price and number of bathrooms

``` r
create_bathroom_barchart <- function( df, title ) {
  bar_chart <-  ggplot(df, aes(x = bathrooms, y = price)) +
    geom_bar(stat = "summary", fun = median, fill = 'deepskyblue') +
    labs(x = "Bathrooms", y = "Price") +
    scale_x_continuous(n.breaks = 15) +
    geom_label(stat = "count", aes(label = ..count.., y = ..count..)) +
    labs(title = title) +
    theme(text = element_text(size = 15, face = "bold", family = "mono"))
  
  return (bar_chart)
}

bar_chart_under_6_bathrooms <- create_bathroom_barchart(
  df = ireland_houses[ireland_houses$bathrooms < 6,],
  title = "Median Price of Houses with under 6 bathrooms"  
)

bar_chart_over_6_bathrooms <- create_bathroom_barchart(
  df = ireland_houses[ireland_houses$bathrooms >= 6,],
  title = "Median Price of Houses with over 6 bathrooms"  
)

grid.arrange(bar_chart_under_6_bathrooms, bar_chart_over_6_bathrooms)
```

![](DataExploration-HousingDataset_files/figure-gfm/Analysing%20relationship%20between%20house%20price%20and%20number%20of%20bathrooms-1.png)<!-- -->

To compile the bar charts above, the dataframe was split into 2 based on
the number of bathrooms to help visualise the data, 6 was choosen based
on multiple attempts at tryign to get the best visualisation.

The 2 bar charts above show that there is indeed some positive
correlation between house price and number of bathrooms, as the number
of bathrooms increase, so does the house price. However, this is not
always true. It is possible to see instance where houses with more
bathrooms cost less than houses with less bathrooms.

## Analysing relationship between house price and number of bedrooms

``` r
create_bedroom_barchart <- function( df, title ) {
  bar_chart <-  ggplot(df, aes(x = bedrooms, y = price)) +
    geom_bar(stat = "summary", fun = median, fill = 'deepskyblue') +
    labs(x = "Bedrooms", y = "Price") +
    scale_x_continuous(n.breaks = 15) +
    geom_label(stat = "count", aes(label = ..count.., y = ..count..)) +
    labs(title = title) +
    theme(text = element_text(size = 15, face = "bold", family = "mono"))
  
  return (bar_chart)
}

bar_chart_under_6_bedrooms <- create_bedroom_barchart(
  df = ireland_houses[ireland_houses$bedrooms < 6,],
  title = "Median Price of Houses with under 6 bedrooms"  
)

bar_chart_over_6_bedrooms <- create_bedroom_barchart(
  df = ireland_houses[ireland_houses$bedrooms >= 6,],
  title = "Median Price of Houses with over 6 bedrooms"  
)

grid.arrange(bar_chart_under_6_bedrooms, bar_chart_over_6_bedrooms)
```

![](DataExploration-HousingDataset_files/figure-gfm/Analysing%20relationship%20between%20house%20price%20and%20number%20of%20bedrooms-1.png)<!-- -->

The same kind of behaviour can be seen with the bedroom variable. This
should be no surprise as there was indeed a positive correlation between
number of bedrooms and house price.

## Analysing relationship between house price and nearest education centres

``` r
house_by_education_centre <- create_lin_graph(
  house_df = ireland_houses,
  aest = list( x = sym("nearestEducationCentres"), y = sym("price") ),
  labels = list(title = "Houses by Count of Education Centres", x = "Count of Education Centres", y = "Price")
)

house_by_garda_stations <- create_lin_graph(
  house_df = ireland_houses,
  aest = list( x = sym("nearestGardaStations"), y = sym("price") ),
  labels = list(title = "Houses by Count of Garda Stations", x = "Count of Garda Stations", y = "Price")
)

house_by_hospitals <- create_lin_graph(
  house_df = ireland_houses,
  aest = list( x = sym("nearestHospitals"), y = sym("price") ),
  labels = list(title = "Houses by Count of Hospitals", x = "Count of Hospitals", y = "Price")
)

house_by_public_transport <- create_lin_graph(
  house_df = ireland_houses,
  aest = list( x = sym("nearestPublicTransports"), y = sym("price") ),
  labels = list(title = "Houses by Count of Public Transport", x = "Count of Public Transport", y = "Price")
)


grid.arrange(house_by_education_centre, house_by_garda_stations, house_by_hospitals, house_by_public_transport, ncol=1) 
```

![](DataExploration-HousingDataset_files/figure-gfm/Analysing%20relationship%20between%20house%20price%20and%20socio%20economic%20variables-1.png)<!-- -->

The graphs above do not seem to show us any relationship between house
price and each of those socio-economic variables. Perhaps, when the
spatial visualisation is done, there might be some hidden relationship.

## Analysing factor variables - ANOVA, p-value and f-value

In this part of the analysis, the relationship between price and the
factor variables: **property type**, **county**, **townOrNeighbourhood**
and **berRating** will be studied.

The statistical methods used will be the **ANOVA (Analysis of
Variance)** so that the significance of those variables with relation to
the price can be understood.

The hypothesis used across those factors is the following:

- **H0** *( p-value \> 0.05 & small f-value )*: It means that the
  variables do not have a strong relationship and therefore the
  categorical variable does not contribute to the prediction of the
  target variable.

- **H1** *( p-value \< 0.05 & large f-value )*: It means that the
  variables do not have a strong relationship, which indicates that the
  categorical variable is signifcant when trying to understand changes
  in the target variable.

### Property Type

#### Calculating ANOVA

``` r
anova_result <- aov(price ~ propertyType, data = ireland_houses)
summary(anova_result)
```

    ##                Df           Sum Sq        Mean Sq F value              Pr(>F)
    ## propertyType    7   76910505205713 10987215029388   36.51 <0.0000000000000002
    ## Residuals    9001 2708808922336583   300945330778                            
    ##                 
    ## propertyType ***
    ## Residuals       
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Given the results above, we can reject the null hypothesis based on the
**p-value** as that is smaller than *0.05*.

#### Calculating the F Critical

``` r
calculate_f_critical <- function( total_observations, num_property_levels ) {
  
  total_observations <- nrow(ireland_houses)
  number_of_predictors <- num_property_levels 
  
  min_df <- total_observations - number_of_predictors
  max_df <- total_observations - 1
  alpha <- 0.05

  f_critical <- qf(
    p = 1 - alpha, 
    df1 = min_df, 
    df2 = max_df, 
    lower.tail = FALSE
  )  
  
  return (f_critical)
}

cat( "F-Critical value is", calculate_f_critical( 
  total_observations = nrow(ireland_houses), 
  num_property_levels = nlevels(ireland_houses$propertyType)
))
```

    ## F-Critical value is 0.9659243

The F-Critical value is significantly smaller than the F-value
calculated from the ANOVA step, therefore, we can certainly **reject**
the null hypothesis (**H0**).

### County

#### Calculating ANOVA

``` r
anova_result <- aov(price ~ county, data = ireland_houses)
summary(anova_result)
```

    ##               Df           Sum Sq       Mean Sq F value              Pr(>F)    
    ## county        25  177970935572066 7118837422883   24.52 <0.0000000000000002 ***
    ## Residuals   8983 2607748491970246  290298173435                                
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Given the results above, we can reject the null hypothesis based on the
**p-value** as that is smaller than *0.05*.

#### Calculating the F Critical

``` r
cat( "F-Critical value is", calculate_f_critical( 
  total_observations = nrow(ireland_houses), 
  num_property_levels = nlevels(ireland_houses$county)
))
```

    ## F-Critical value is 0.9659071

The F-Critical value is significantly smaller than the F-value
calculated from the ANOVA step, therefore, we can certainly **reject**
the null hypothesis (**H0**).

### BER Rating

#### Calculating ANOVA

``` r
anova_result <- aov(price ~ berRating, data = ireland_houses)
summary(anova_result)
```

    ##               Df           Sum Sq        Mean Sq F value              Pr(>F)
    ## berRating     16  162603430928200 10162714433013   34.84 <0.0000000000000002
    ## Residuals   8992 2623115996614096   291716636634                            
    ##                
    ## berRating   ***
    ## Residuals      
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Given the results above, we can reject the null hypothesis based on the
**p-value** as that is smaller than *0.05*.

#### Calculating the F Critical

``` r
cat( "F-Critical value is", calculate_f_critical( 
  total_observations = nrow(ireland_houses), 
  num_property_levels = nlevels(ireland_houses$berRating)
))
```

    ## F-Critical value is 0.9659157

The F-Critical value is significantly smaller than the F-value
calculated from the ANOVA step, therefore, we can certainly **reject**
the null hypothesis (**H0**).

#### Box Plot of BER Rating and House price

``` r
ggplot(ireland_houses %>% 
         filter(!(berRating == "")), aes(x = berRating, y = price)) +
  
  geom_boxplot( aes(fill = berRating), color = "black", outlier.shape = 16) +
  labs(title = "Box plot of prices by BER rating", 
       x = "BER rating", 
       y = "Price in Log10 scale") +
  scale_y_log10() +
  theme(text=element_text(size = 20, face = "bold", family = "mono"))
```

![](DataExploration-HousingDataset_files/figure-gfm/Box-Plot%20of%20BER%20Rating%20and%20House%20price-1.png)<!-- -->

### Town or Neighbourhood

#### Calculating ANOVA

``` r
anova_result <- aov(price ~ townOrNeighbourhood, data = ireland_houses)
summary(anova_result)
```

    ##                       Df           Sum Sq       Mean Sq F value
    ## townOrNeighbourhood  113  350000075292067 3097345799045   11.31
    ## Residuals           8895 2435719352250241  273830168887        
    ##                                  Pr(>F)    
    ## townOrNeighbourhood <0.0000000000000002 ***
    ## Residuals                                  
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Given the results above, we can reject the null hypothesis based on the
**p-value** as that is smaller than *0.05*.

#### Calculating the F Critical

``` r
cat( "F-Critical value is", calculate_f_critical( 
  total_observations = nrow(ireland_houses), 
  num_property_levels = nlevels(ireland_houses$townOrNeighbourhood)
))
```

    ## F-Critical value is 0.9658226

The F-Critical value is significantly smaller than the F-value
calculated from the ANOVA step, therefore, we can certainly **reject**
the null hypothesis (**H0**).

# Data Visualisation

## Property Price

### Box-Plot Property Type by Price

The next graph displays how prices and property prices are related.

``` r
ggplot(ireland_houses, aes(x = propertyType, y = price)) +
  geom_boxplot( aes(fill = propertyType), color = "black", outlier.shape = 16) +
  labs(title = "Box plot of prices by property type", 
       x = "Property type", 
       y = "Price in Log10 scale") +
  scale_y_log10() +
  theme(text=element_text(size = 20, face = "bold", family = "mono"))
```

![](DataExploration-HousingDataset_files/figure-gfm/Box-Plot%20of%20Property%20types%20and%20House%20price-1.png)<!-- -->

### Frequency Plot Property Type by Price

In order to better visualize how the observations distribute across the
price range, let’s choose the range from €0 to €2 million euro as it
will allow us to well visualise where most of the observations fall.

``` r
ggplot(ireland_houses, aes(x = price, 
                           colour = propertyType, 
                           fill = propertyType)) +
  geom_freqpoly(
    bins=30,
    lwd = 1,
    linetype = 2
  ) +
  labs(
    title = "Frequency of House Prices in Ireland",
    x = "Price",
    y = "Observations",
    color = "Property Type"
  ) +
  xlim(0, 2000000) +
  scale_fill_brewer() 
```

![](DataExploration-HousingDataset_files/figure-gfm/House%20Price%20by%20Property%20type-1.png)<!-- -->

## Density Plot of County and House price

``` r
med_price_county_df <- ireland_houses %>%
  group_by(county) %>%
  summarize(median = median(price))


ggplot(ireland_houses, aes(x=price, color=county, fill=county)) +
  geom_density(alpha = 0.3, linewidth = 1) + 
  scale_x_log10() +
  geom_vline(
    data = med_price_county_df, 
    aes(xintercept = median, color = county), 
    linewidth = 0.5) + 
  facet_wrap(~county) +
  labs(x= "House Price", subtitle="House Price distribution per county") +
  theme(
    legend.position = "bottom",
    text = element_text(size = 15, face = "bold", family = "mono")
  )
```

![](DataExploration-HousingDataset_files/figure-gfm/Density%20Plot%20of%20County%20and%20House%20price-1.png)<!-- -->
The density plot of the house price by county above shows the
distribution of the house price.

# Spatial Visualisation

Let’s first load the shape file of Ireland

``` r
# Lets create a shape file object from our dataset
ireland_houses_sf <- st_as_sf(x = ireland_houses, 
                         coords = c("longitude", "latitude"), 
                         crs = 4326)

tmap_mode("view")

shp_ireland <- readOGR(
  dsn = "../../datasets/shapefile_ireland", 
  layer = "gadm41_IRL_0", 
  verbose = FALSE
)


create_county_map <- function() {
  ireland_counties_sf <- st_read("../../datasets/ireland_counties.geojson", 
                                 quiet = TRUE)
  # Transformation needed to match format of ireland_houses dataset 
  ireland_counties_sf$COUNTY <- toupper(ireland_counties_sf$COUNTY) 
  ireland_counties_sf <- rename( ireland_counties_sf, county = COUNTY)
  
  counties_map <- ireland_counties_sf %>% 
    group_by(county) %>% 
    summarise(geometry = st_union(geometry) , AREA=sum(AREA))
  
  # Remove Northern Ireland as it is not part of this analysis
  county_map <- counties_map %>% filter( county != "NI" )
  
  return (county_map)
}

ireland_by_county_sf <- create_county_map()
```

## Bubble Plot of Property Type by County

``` r
property_type_count <- aggregate(
  ireland_houses$address,
  by = list(
    ireland_houses$county,
    ireland_houses$propertyType
  ),
  FUN = length
)

names(property_type_count) <- c("county", "propertyType", "count")


property_type_count_by_county <- merge( ireland_by_county_sf,
                         property_type_count,
                         by.x = "county",
                         by.y = "county"
)


property_type_count_by_county_map <- 
  property_type_count_by_county %>% 
  st_set_crs(value = 4326) %>% 
  st_cast()

tmap_mode("plot")

tm_shape(shp = shp_ireland) + 
    tm_borders(alpha = 1) +
tm_shape(shp = property_type_count_by_county) + 
  tm_bubbles(size = "count", 
             col = "propertyType", 
             legend.size.show = TRUE, 
             alpha = 0.9, 
             palette = "Set3") +
  tm_facets(by = "propertyType", ncol = 3, nrow = 3) +
  tm_layout(legend.text.size = 1.1, legend.title.size = 1.4, frame = TRUE) 
```

![](DataExploration-HousingDataset_files/figure-gfm/Plot%20of%20Property%20Type%20by%20County-1.png)<!-- -->

The bubble plot above depicts the size of the presence for each property
type across the country. A few interesting things can be seen in the
graph above, for example:

- There is little observation with *propertyType* of type **Duplex**,
  and where we see those is in the **Dublin** county area in the east
  side of the country.

- Similar case we can find for *propertyType* of type **Bungalow**,
  however those do not even have a significant presence in any area.

- By far, the most popular property types are **Terrace**, **Detached**
  and **Semi-D**.

- **Apartments** have a very heavy presence in Dublin area, East Coast,
  and some presence near other big centres like Cork city in the South
  East and Galway city on the West coast.

- Lastly, there seems to be little presence of properties in the middle
  of the country.

## Density Plot of Count of Houses by County

``` r
tmap_mode("view")

count_properties_by_country <- aggregate(
  x = ireland_houses["address"], 
  by = ireland_houses["county"], 
  FUN = length
)

names(count_properties_by_country)<- c("county","Count")

count_houses_county <- merge( 
  x = ireland_by_county_sf, 
  y = count_properties_by_country, 
  by.x = "county", 
  by.y = "county" 
)


count_houses_county_map <- count_houses_county %>% 
  st_set_crs(value = 4326) %>% 
  st_cast()

tm_shape(count_houses_county_map) + 
    tm_polygons("Count", 
                palette = "viridis",
                legend.title = "Count of Houses per County", 
                style = "kmeans") +
  
    tmap_options(
      basemaps = c(Canvas = "Esri.WorldTopoMap", 
                   Imagery = "Esri.WorldImagery") ) +
    tm_text("county", size = 1, style = "pretty") +
    tm_scale_bar()
```

![](DataExploration-HousingDataset_files/figure-gfm/Density%20Plot%20of%20Count%20of%20Houses%20by%20County-1.png)<!-- -->

The graph above illustrates some points indicated by the previous Bubble
plot. The countryside of the country or its midlands do not have as many
properties on offer as some counties located in the coast. The amount of
properties available in the countries on the countryside range from 35
to 256 properties per county. When compared to Dublin and Cork, it is
possible to see a huge disparaty.

It is worth noting that counties adjacent to areas with high property
supply tend to have more availability compared to counties situated
farther away from the center of those clusters.

## Choropleth Map of Mean House Price per County

``` r
tmap_mode("view")

ireland_houses_by_county <- aggregate(ireland_houses["price"], 
                          by = ireland_houses["county"], mean)

mean_price_map <- merge( ireland_by_county_sf, ireland_houses_by_county, 
            by.x = "county", 
            by.y = "county" )


mean_price_map <- mean_price_map %>% st_set_crs(value = 4326) %>% st_cast()

tm_shape(shp = shp_ireland) + 
  tm_borders(alpha = 0.5) +
  tm_shape(shp = mean_price_map) + 
  tmap_options(basemaps = c(Canvas = "Esri.WorldTopoMap", 
                            Imagery = "Esri.WorldImagery") ) +
  tm_polygons(
    col = "price", 
    title = "Mean House Price Per County in €", 
    palette = "YlOrBr",                 
    stretch.palette = FALSE, 
    n = 6
  ) +  
  tm_text("county", size = 1, style = "pretty") +
  tm_scale_bar()
```

![](DataExploration-HousingDataset_files/figure-gfm/Plot%20of%20Mean%20House%20Price%20per%20County-1.png)<!-- -->

The above graph demonstrates yet another fascinating phenomenon known as
the “neighbouring effect,” which supports the first law of geography’s
assertion that the price of houses in a given county can impact the
prices in adjacent counties. In other words, the mean house price in one
county has a significant influence on the mean house prices of
neighboring counties.

It is noteworthy to emphasize that county Dublin has a significant
impact on neighboring counties such as Wicklow, Kildare, and Meath,
among others. Similarly, the counties in the midlands have a noticeable
impact on each other, resulting in lower mean house prices in the
region.

## Choropleth Map of Mean Count of Public Transport per County

``` r
tmap_mode("view")

ireland_houses_by_county <- aggregate(ireland_houses["nearestPublicTransports"], 
                          by = ireland_houses["county"], mean)

mean_map_transport <- merge( ireland_by_county_sf, ireland_houses_by_county, 
            by.x = "county", 
            by.y = "county" )


mean_map_transport <- mean_map_transport %>% st_set_crs(value = 4326) %>% st_cast()

tm_shape(shp = shp_ireland) + 
  tm_borders(alpha = 0.5) +
  tm_shape(shp = mean_map_transport) + 
  tmap_options(basemaps = c(Canvas = "Esri.WorldTopoMap", 
                            Imagery = "Esri.WorldImagery") ) +
  tm_polygons(
    col = "nearestPublicTransports", 
    title = "Mean Count of Public Transport Per County", 
    palette = "viridis",                 
    stretch.palette = FALSE, 
    n = 6
  ) +  
  tm_text("county", size = 1, style = "pretty") +
  tm_scale_bar()
```

![](DataExploration-HousingDataset_files/figure-gfm/Plot%20of%20Mean%20Count%20of%20Public%20Transport%20per%20County-1.png)<!-- -->

In the plot above, it can be seen that properties in county Dublin
benefit from a much better access to public transport. The overwhelming
difference between Dublin and other counties may indicate that the
houses in the countryside are lacking on access to public transport.

## Choropleth Map of Mean Count of Education Centres per County

``` r
tmap_mode("view")

ireland_houses_by_county <- aggregate(ireland_houses["nearestEducationCentres"], 
                          by = ireland_houses["county"], mean)

mean_map_education <- merge( ireland_by_county_sf, ireland_houses_by_county, 
            by.x = "county", 
            by.y = "county" )


mean_map_education <- mean_map_education %>% st_set_crs(value = 4326) %>% st_cast()

tm_shape(shp = shp_ireland) + 
  tm_borders(alpha = 0.5) +
  tm_shape(shp = mean_map_education) + 
  tmap_options(basemaps = c(Canvas = "Esri.WorldTopoMap", 
                            Imagery = "Esri.WorldImagery") ) +
  tm_polygons(
    col = "nearestEducationCentres", 
    title = "Mean Count of Education Centres Per County", 
    palette = "viridis",                 
    stretch.palette = FALSE, 
    n = 6
  ) +  
  tm_text("county", size = 1, style = "pretty") +
  tm_scale_bar()
```

![](DataExploration-HousingDataset_files/figure-gfm/Plot%20of%20Mean%20Count%20of%20Education%20Centres%20per%20County-1.png)<!-- -->

## Choropleth Map of Mean Count of Hospitals per County

``` r
tmap_mode("view")

ireland_houses_by_county <- aggregate(ireland_houses["nearestHospitals"], 
                          by = ireland_houses["county"], mean)

mean_map_hospitals <- merge( ireland_by_county_sf, ireland_houses_by_county, 
            by.x = "county", 
            by.y = "county" )


mean_map_hospitals <- mean_map_hospitals %>% st_set_crs(value = 4326) %>% st_cast()

tm_shape(shp = shp_ireland) + 
  tm_borders(alpha = 0.5) +
  tm_shape(shp = mean_map_hospitals) + 
  tmap_options(basemaps = c(Canvas = "Esri.WorldTopoMap", 
                            Imagery = "Esri.WorldImagery") ) +
  tm_polygons(
    col = "nearestHospitals", 
    title = "Mean Count of Hospitals Per County", 
    palette = "YlOrBr",                 
    stretch.palette = FALSE, 
    n = 6
  ) +  
  tm_text("county", size = 1, style = "pretty") +
  tm_scale_bar()
```

![](DataExploration-HousingDataset_files/figure-gfm/Plot%20of%20Mean%20Count%20of%20Hospitals%20per%20County-1.png)<!-- -->

## Choropleth Map of Mean Count of Garda Stations per County

``` r
tmap_mode("view")

ireland_houses_by_county <- aggregate(ireland_houses["nearestGardaStations"], 
                          by = ireland_houses["county"], mean)

mean_map_garda <- merge( ireland_by_county_sf, ireland_houses_by_county, 
            by.x = "county", 
            by.y = "county" )


mean_map_garda <- mean_map_garda %>% st_set_crs(value = 4326) %>% st_cast()

tm_shape(shp = shp_ireland) + 
  tm_borders(alpha = 0.5) +
  tm_shape(shp = mean_map_garda) + 
  tmap_options(basemaps = c(Canvas = "Esri.WorldTopoMap", 
                            Imagery = "Esri.WorldImagery") ) +
  tm_polygons(
    col = "nearestGardaStations", 
    title = "Mean Count of Garda Stations Per County", 
    palette = "viridis",                 
    stretch.palette = FALSE, 
    n = 6
  ) +  
  tm_text("county", size = 1, style = "pretty") +
  tm_scale_bar()
```

![](DataExploration-HousingDataset_files/figure-gfm/Plot%20of%20Mean%20Count%20of%20Garda%20Stations%20per%20County-1.png)<!-- -->

What can be seen in the

# Removing Outliers

After trying to fit the model in this dataset in the notebook
*model-selection*, it was noted that the presence of outliers was
causing the Machine Learning Algorithms, **regression trees** and
**random forests**, to have a high *RMSE* (Root Mean Squared Error).
Looking at the variable importance graph of those algorithms, **size**
and **pricePerSqMeter** were the variables most used by the *trees* to
predict the results. Furthermore, during this exploratory data analysis,
*price* proved to be a variable that has a lot of outliers, mostly due
to the fact that not many people can buy very expensive houses.
Therefore, It was decided that **price** and **size** are the two good
candidates to get their outliers removed as they have the most influence
in the algorithms’ decision process and have proved it during the
exploratory data analysis. The variable **pricePerSqMeter** will not be
modified as smaller houses in privileged areas could get penalised.

The statistical method used for removing the outliers from the *size*
and *price* columns is the *z-score* method. Where the *z-score* is
calculated for each value and the values outside 3 standard deviations
of the mean are removed. The z-score version used in this study is a
modified version where 4 standard deviations are used instead of 3, the
reason for that is to have a less aggressive approach and try not to
shrink the dataset too much.

## Z-Score Implementation

``` r
remove_outliers_zscore <- function( column ) {
  
  mean <- mean(column)
  standard_deviation <- sd(column)
  
  z_scores <- (column - mean) / standard_deviation
  
  outliers <- which(z_scores > 4 | z_scores < -4)
  
  cat("Length Original data: ", length(column), "\n")
  cat("length Outliers: ", length(outliers), "\n")
  cat("Length Cleaned data: ", length(column) - length(outliers), "\n")

  return (outliers)
}
```

## Removal of Outliers

After implementing the z-score function, let’s proceed to remove the
outliers. We would also like to print the least expensive and smallest
houses that are being removed.

``` r
outliers_price <- remove_outliers_zscore(ireland_houses$price)
```

    ## Length Original data:  9009 
    ## length Outliers:  90 
    ## Length Cleaned data:  8919

``` r
price_outliers <- ireland_houses[ outliers_price, ]

ireland_houses <- ireland_houses[ -outliers_price, ]


cat("Least Expensive House Removed: ", min(price_outliers$price), "\n")
```

    ## Least Expensive House Removed:  2695000

``` r
outliers_size <- remove_outliers_zscore(ireland_houses$size)
```

    ## Length Original data:  8919 
    ## length Outliers:  43 
    ## Length Cleaned data:  8876

``` r
size_outliers <- ireland_houses[ outliers_size, ]

ireland_houses <- ireland_houses[ -outliers_size, ]

cat("Smallest House Removed: ", min(size_outliers$size), "\n")
```

    ## Smallest House Removed:  724

We can see that most of the houses being removed have an area of over
724 square meters, and that the least expensive house removed is worth
€2,695,000.00 euro. Finally, a total of 133 observations have been
removed from the dataset, and we ended up with 8876 observations left in
it.

## Plotting Outliers Removed

``` r
price_outliers_graph <- create_lin_graph(
  house_df = price_outliers,
  aest = list( x = sym("size"), y = sym("price") ),
  labels = list(title = "Price Outliers being Removed", x = "Size", y = "Price")
)

size_outliers_graph <- create_lin_graph(
  house_df = size_outliers,
  aest = list( x = sym("price"), y = sym("size") ),
  labels = list(title = "Size Outliers being Removed", x = "Price", y = "Size")
)

grid.arrange(price_outliers_graph, size_outliers_graph) 
```

![](DataExploration-HousingDataset_files/figure-gfm/Plotting%20Outliers%20Removed-1.png)<!-- -->

# Creating Dummy Vars

In this part of the process, the factor variables are transformed into
dummy variables to provide a better data type for machine learning
algorithms in general.

``` r
ireland_houses <- dummy_columns(
  .data = ireland_houses,
  select_columns = c("propertyType", "county", "berRating"),
  remove_selected_columns = T,
  remove_most_frequent_dummy = T
)

# Formatting the name of the dummy variables
ireland_houses <- ireland_houses %>%
   clean_names(., "small_camel")
```

# Removing Character variables

Before saving the dataset to the disk and handing it over to the model
selection step, it is advised to remove character variables as those can
introduce noise and bad predictions by the models.

``` r
columns_to_remove <- c("address", "location", "townOrNeighbourhood")
ireland_houses <- ireland_houses[ , !names(ireland_houses) %in% columns_to_remove ]
```

## Write Explored Dataset to disk

Saving resulting data from Exploration step to disk.

``` r
dataset_directory <- "../../datasets/"
dataset_filename <- paste(dataset_directory, 
                          "ireland_houses_explored.Rda", 
                          sep="")
save(ireland_houses, file = dataset_filename)
```
