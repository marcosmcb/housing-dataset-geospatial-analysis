Ireland Housing - Data Cleaning
================
Marcos Cavalcante
2023-04-14

- <a href="#data-cleaning" id="toc-data-cleaning">Data Cleaning</a>
- <a href="#installing-libraries" id="toc-installing-libraries">Installing
  libraries</a>
- <a href="#loading-the-dataset---ireland-housing-dataset"
  id="toc-loading-the-dataset---ireland-housing-dataset">Loading the
  Dataset - Ireland Housing dataset</a>
- <a href="#removal-of-duplicates" id="toc-removal-of-duplicates">Removal
  of duplicates</a>
- <a
  href="#handling-missing-values---what-is-the--of-values-missing-for-each-variable"
  id="toc-handling-missing-values---what-is-the--of-values-missing-for-each-variable">Handling
  missing values - What is the % of values missing for each variable.</a>
  - <a href="#handling-missing-values---ber-code"
    id="toc-handling-missing-values---ber-code">Handling missing values -
    BER Code</a>
  - <a href="#handling-missing-values---size-meters-squared-and-bathrooms"
    id="toc-handling-missing-values---size-meters-squared-and-bathrooms">Handling
    missing values - Size Meters Squared and Bathrooms</a>
- <a href="#removal-of-unnecessary-variables"
  id="toc-removal-of-unnecessary-variables">Removal of unnecessary
  variables</a>
- <a href="#describing-the-dataset-with-skim-function"
  id="toc-describing-the-dataset-with-skim-function">Describing the
  dataset with <em>skim</em> function</a>
- <a href="#renaming-variables" id="toc-renaming-variables">Renaming
  Variables</a>
- <a href="#conversion-into-appropriate-data-types"
  id="toc-conversion-into-appropriate-data-types">Conversion into
  appropriate data types</a>
- <a
  href="#handling-of-missing-values---removing-observations-and-variables"
  id="toc-handling-of-missing-values---removing-observations-and-variables">Handling
  of missing values - Removing observations and variables</a>
- <a href="#creation-of-new-variables"
  id="toc-creation-of-new-variables">Creation of new variables</a>
- <a href="#handling-outliers" id="toc-handling-outliers">Handling
  Outliers</a>
- <a href="#scaling-variables" id="toc-scaling-variables">Scaling
  variables</a>
- <a href="#write-clean-dataset-to-disk"
  id="toc-write-clean-dataset-to-disk">Write Clean Dataset to disk</a>

### Data Cleaning

In this part, the dataset will be cleant so it can be used more
appropriately for data exploration and use by the machine learning
techniques.

The following steps will be taken:

1.  Loading the dataset
2.  Removal of duplicates
3.  Handling of missing values
4.  Removal of unnecessary variables
5.  Renaming variables
6.  Conversion into appropriate data types
7.  Creation of new variables
8.  Handling outliers
9.  Scaling variables
10. Write Clean Dataset

## Installing libraries

In this pre-step, all of the required packages will be installed and
loaded.

``` r
packages <- c("tidyverse", "haven", "devtools", "dplyr", "stringr", "kableExtra", 
              "formattable","stringi", "see", "ggraph", "correlation", 
              "PerformanceAnalytics", "gridExtra")

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
library(skimr)
```

## Loading the Dataset - Ireland Housing dataset

At this step, the Ireland houses dataset will be imported.

``` r
dataset_directory <- "../../datasets/"
dataset_filename <- paste(dataset_directory, "house_listings_all.csv", sep="")

options(scipen = 999) # turn off scientific notation

ireland_houses <- read.csv(file = dataset_filename) # Load the dataset
```

#### Loading the Dataset - First look at the dataset

In this step, the first five rows of our dataset will be displayed so
that we can take a look at the different pieces of data available to us
and what kind of information they bring to the analysis.

``` r
summary(ireland_houses, 5)
```

    ##        id          daftShortcode          title              price          
    ##  Min.   :   6800   Min.   :  1319566   Length:100294      Length:100294     
    ##  1st Qu.:3805133   1st Qu.: 18690195   Class :character   Class :character  
    ##  Median :3933350   Median : 19258514   Mode  :character   Mode  :character  
    ##  Mean   :3842396   Mean   : 28263078                                        
    ##  3rd Qu.:3974191   3rd Qu.: 19593376                                        
    ##  Max.   :4019790   Max.   :113071717                                        
    ##                                                                             
    ##  size_meters_squared propertySize         bedrooms           bathrooms     
    ##  Min.   :   1.0      Length:100294      Length:100294      Min.   : 1.000  
    ##  1st Qu.:  75.0      Class :character   Class :character   1st Qu.: 1.000  
    ##  Median : 102.0      Mode  :character   Mode  :character   Median : 2.000  
    ##  Mean   : 131.9                                            Mean   : 2.134  
    ##  3rd Qu.: 147.0                                            3rd Qu.: 3.000  
    ##  Max.   :6109.0                                            Max.   :32.000  
    ##  NA's   :19967                                             NA's   :1658    
    ##  propertyType       publishDate         ber_rating           ber_code         
    ##  Length:100294      Length:100294      Length:100294      Min.   :         0  
    ##  Class :character   Class :character   Class :character   1st Qu.: 106661911  
    ##  Mode  :character   Mode  :character   Mode  :character   Median : 113473896  
    ##                                                           Mean   : 113341265  
    ##                                                           3rd Qu.: 114880636  
    ##                                                           Max.   :1134291201  
    ##                                                           NA's   :43417       
    ##    ber_epi             latitude       longitude         category        
    ##  Length:100294      Min.   :51.44   Min.   :-10.451   Length:100294     
    ##  Class :character   1st Qu.:53.28   1st Qu.: -6.805   Class :character  
    ##  Mode  :character   Median :53.34   Median : -6.285   Mode  :character  
    ##                     Mean   :53.18   Mean   : -6.823                     
    ##                     3rd Qu.:53.37   3rd Qu.: -6.249                     
    ##                     Max.   :55.38   Max.   : -6.014                     
    ##                                                                         
    ##    location           url_link        
    ##  Length:100294      Length:100294     
    ##  Class :character   Class :character  
    ##  Mode  :character   Mode  :character  
    ##                                       
    ##                                       
    ##                                       
    ## 

Looking at the output of the previous step, some interesting things can
be observed:

- **id** and **daftShortCode** seem to describe values that look like
  identifiers, but identifiers that are used for different purposes.

- **title** contains values which look like addresses of properties.

- **price** are expected to be of *numeric* type, nevertheless, strings
  like *“Price on Application”* are also present.

- **size_meters_squared** and **propertySize**, at first glance, contain
  the same information / values, however, formatted differently. Another
  interesting point is that there are values missing on both variables.

- **bedrooms** and **bathrooms** contain the amount of each of those in
  the property and should therefore be of *numeric* type.

- **propertyType** contain values that describe what kind of property
  that is, for example: Bungalow and Detached.

- **publishDate** is an attribute related more to the ad than to the
  property itself and it describes the date when the ad was published.

- **ber_rating** is a variable that tells how energy efficient is a
  property, BER stands for Building Energy Rating.

- **ber_code** is simply the ID of the certificate that the house was
  given.

- **ber_epi** describes the energy consumption per square meter of a the
  property yearly.

- **latitude** and **longitude** are spatial values used to locate the
  property on the map.

- **category** only shows the value of *“Buy”*.

- **location** contains value with the concatenation of town/city and
  the county.

- **url_link** contains the value of the URL of the house on the
  platform’s website.

## Removal of duplicates

In this step the goal is to remove any observation that is duplicated in
the dataset. This is going to be done by searching for observations that
contain the same *id* and *url_link* values.

It is worth noting that currently the dataset has over 100 thousand
observations, after removing the duplicate observations, just under 13
thousand observations will remain in the dataset.

``` r
print(paste("Number of observations BEFORE removing duplicates:", 
            nrow(ireland_houses)))
```

    ## [1] "Number of observations BEFORE removing duplicates: 100294"

``` r
remove_duplicates <- function( dfHouses, dupes_column ) {
  subsetDfHouse <- dfHouses[dupes_column]
  return ( dfHouses[!duplicated(subsetDfHouse),] )
}

ireland_houses <- remove_duplicates(ireland_houses, c("id", "url_link"))

print(paste("Number of observations AFTER removing duplicates:", 
            nrow(ireland_houses)))
```

    ## [1] "Number of observations AFTER removing duplicates: 12860"

## Handling missing values - What is the % of values missing for each variable.

In this step, it is possible to see that there are variables with
missing values. Nevertheless, it is worth noting that most of those
features have been assigned the type of character and there might be
features with missing data, but due to the wrong data type, they are
displayed as if they were not missing.

At a later point, those features with the wrong data type will be
converted into the appropriate data type.

``` r
compile_missing_values_table <- function( dfHouses ) {
  percentage_missing <- colSums(is.na(dfHouses)) * 100 / nrow(dfHouses)
  percentage_missing_sorted <- percentage_missing[
    order(percentage_missing, decreasing = TRUE)
  ]

  percentage_missing_formatted = percent(
    formattable(percentage_missing_sorted) / 100
  )

  kbl(percentage_missing_formatted, col.names = NULL) %>%
    kable_paper(bootstrap_options = "striped", 
                full_width = F, 
                html_font = "Computer Modern") %>%
    add_header_above(header = c("Feature", "Percentage of Missing Values"))
}


compile_missing_values_table( ireland_houses )
```

<table class=" lightable-paper" style="font-family: Computer Modern; width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="1">

<div style="border-bottom: 1px solid #00000020; padding-bottom: 5px; ">

Feature

</div>

</th>
<th style="padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="1">

<div style="border-bottom: 1px solid #00000020; padding-bottom: 5px; ">

Percentage of Missing Values

</div>

</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
ber_code
</td>
<td style="text-align:right;">
42.47%
</td>
</tr>
<tr>
<td style="text-align:left;">
size_meters_squared
</td>
<td style="text-align:right;">
26.54%
</td>
</tr>
<tr>
<td style="text-align:left;">
bathrooms
</td>
<td style="text-align:right;">
2.05%
</td>
</tr>
<tr>
<td style="text-align:left;">
id
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
daftShortcode
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
title
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
price
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
propertySize
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
bedrooms
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
propertyType
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
publishDate
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_rating
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_epi
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
latitude
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
longitude
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
category
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
location
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
url_link
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
</tbody>
</table>

As we can see from the output of the step above, *ber_code* is missing
in 42.47% of the observations (5461 rows), *size_meters_squared* is
missing in 26.54% of the observations (3413 rows) and finally,
*bathrooms* is missing in 2.05% of the observations (263 rows).

### Handling missing values - BER Code

As the *ber_code* variable only represents the certificate number of the
BER rating (Building Energy Rating), we can safely remove this column
from the dataset as the certificate number will be individually assigned
to each property and do not actually influence on the house price,
instead the house’s BER rating and BER EPI (Energy Performance
Indicator) might, in fact, affect the house price.

``` r
ireland_houses <- ireland_houses[ , !names(ireland_houses) %in% c("ber_code") ]
```

### Handling missing values - Size Meters Squared and Bathrooms

The observations with no values for *size_meters_squared* and
*bathrooms* will also be removed to keep the dataset as clean as
possible and, no technique for inputing those missing values will be
used not to introduce any bias in the study.

``` r
ireland_houses <- ireland_houses %>% filter(!is.na(bathrooms))
ireland_houses <- ireland_houses %>% filter(!is.na(size_meters_squared))
```

Finally, It can be seen that there does not seem to be any values
missing. It will be investigated further later on whether or not this is
true when the data type conversion is performed.

There are over 9 thousand observations remaining in our dataset.

``` r
compile_missing_values_table( ireland_houses )
```

<table class=" lightable-paper" style="font-family: Computer Modern; width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="1">

<div style="border-bottom: 1px solid #00000020; padding-bottom: 5px; ">

Feature

</div>

</th>
<th style="padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="1">

<div style="border-bottom: 1px solid #00000020; padding-bottom: 5px; ">

Percentage of Missing Values

</div>

</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
id
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
daftShortcode
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
title
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
price
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
size_meters_squared
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
propertySize
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
bedrooms
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
bathrooms
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
propertyType
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
publishDate
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_rating
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_epi
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
latitude
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
longitude
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
category
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
location
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
url_link
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
</tbody>
</table>

## Removal of unnecessary variables

In order to keep the dataset concise and not be using too much
unnecessary data, let’s remove some other variables: *url_link*, *id*
and *daft_short_code* as those represent some sort of identifier.

Other variables that can be removed are *publishDate* as it only tells
us when the ad was put up on the website, *category* as nearly all but 7
observations have the same value of “Buy”, the others have a value of
“New Homes” and finally *propertySize* as that information is already
present in a variable called “size_meters_squared”.

``` r
vars_to_remove <- c( "url_link", "id", "daftShortcode", "publishDate", "category", "propertySize")

ireland_houses <- ireland_houses[ , !names(ireland_houses) %in% vars_to_remove ]
```

## Describing the dataset with *skim* function

Let’s see again what the dataset looks like and how the values across
the variables in it are statistically distributed with the function
*skim*.

``` r
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
9319
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
11
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
7
</td>
</tr>
<tr>
<td style="text-align:left;">
numeric
</td>
<td style="text-align:left;">
4
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
title
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
9159
</td>
<td style="text-align:right;">
0
</td>
</tr>
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
7
</td>
<td style="text-align:right;">
25
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
579
</td>
<td style="text-align:right;">
0
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
0
</td>
<td style="text-align:right;">
4
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
36
</td>
<td style="text-align:right;">
0
</td>
</tr>
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
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
14
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
9
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_rating
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
6
</td>
<td style="text-align:right;">
187
</td>
<td style="text-align:right;">
17
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_epi
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
18
</td>
<td style="text-align:right;">
4111
</td>
<td style="text-align:right;">
4733
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
119
</td>
<td style="text-align:right;">
0
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
size_meters_squared
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
147.01
</td>
<td style="text-align:right;">
150.37
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
86.00
</td>
<td style="text-align:right;">
113.00
</td>
<td style="text-align:right;">
166.00
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
52.62
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
▂▃▇▁▁
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
-7.37
</td>
<td style="text-align:right;">
1.18
</td>
<td style="text-align:right;">
-10.35
</td>
<td style="text-align:right;">
-8.47
</td>
<td style="text-align:right;">
-6.92
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
</tbody>
</table>

## Renaming Variables

It can be seen that some of the variables do not follow a naming
standard or use an adequate name, for example: *title* actually refers
to the *address* of the house and *size_meters_squared* refers to the
*size*.

The naming convention used across the variables is going to be
**camelCase**, therefore *ber_rating* and *ber_epi* will be renamed to
*berRating* and *berEPI* respectively.

``` r
ireland_houses <- rename( ireland_houses, 
  address = title,
  size = size_meters_squared,
  berRating = ber_rating,
  berEPI = ber_epi,
)
```

## Conversion into appropriate data types

The output of the **skim** function has showed some interesting details,
for example: *price*, *berEPI*, and *bedrooms* are of type
**character**, when **numeric** would be, in fact, a better type because
they represent quantitative data.

*propertyType* and *berRating* are of type characters, however,
**factor** may be a better data type because there is a limited number
of categorical values those can hold, **factor** is also a better data
type as it allows for better data manipulation so that typos can be
avoided and sorting the data in a meaningful way becomes possible.

Thus, in this next step, the values in those variables will be converted
into more suitable data types.

``` r
strs_to_replace_with_na <- c( "", "Price on Application",
                              "AMV: Price on Application")

ireland_houses <- mutate(ireland_houses,
  
  berEPI = as.numeric(gsub("kWh/m2/yr", "", berEPI)),
  
  bedrooms = as.numeric(bedrooms),
  
  propertyType = as.factor(propertyType),
  
  berRating = as.factor(berRating),
  
  price = as.numeric(format(
    (parse_number(gsub(",", "", price), strs_to_replace_with_na)), 
    scientific = FALSE, 
    big.mark ="")),
)
```

#### Fixing properties with empty factor for property type

It was noted that 2 properties have an empty property type. In order to
fix it, the house address was used to look it up online. Suitable
property types were found for those 2 observations and they are going to
be applied now.

``` r
propertyLevels <- levels(ireland_houses$propertyType)
semiDetached <- propertyLevels[7]
semiDetached <- factor( semiDetached, levels = propertyLevels )

detached <- propertyLevels[4]
detached <- factor( detached, levels = propertyLevels )

ireland_houses <- ireland_houses %>% 
  mutate( 
    propertyType = if_else( propertyType=="" & 
                            address == "Four bedroomed Semi-Detached, Owenmore Paddock, Ballinacarrow, Co. Sligo", 
                            semiDetached, 
                            propertyType ) 
  )

ireland_houses <- ireland_houses %>% 
  mutate( 
    propertyType = if_else( propertyType=="" & 
                            address == "House Tpye D, Moin Na Ri, Moin Na Ri, Kilworth, Co. Cork", 
                            detached, 
                            propertyType ) 
  )
```

Let’s describe the dataset one more time to see what it looks like now.

``` r
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
9319
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
11
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
2
</td>
</tr>
<tr>
<td style="text-align:left;">
numeric
</td>
<td style="text-align:left;">
7
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
9159
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
119
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
Det: 3630, Sem: 2325, Ter: 1471, Apa: 982
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
C3: 1130, C1: 1112, C2: 1111, D1: 1003
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
298
</td>
<td style="text-align:right;">
0.97
</td>
<td style="text-align:right;">
462170.95
</td>
<td style="text-align:right;">
555824.31
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
1.00
</td>
<td style="text-align:right;">
147.01
</td>
<td style="text-align:right;">
150.37
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
86.00
</td>
<td style="text-align:right;">
113.00
</td>
<td style="text-align:right;">
166.00
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
2
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3.45
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
1.00
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
berEPI
</td>
<td style="text-align:right;">
4111
</td>
<td style="text-align:right;">
0.56
</td>
<td style="text-align:right;">
19597.88
</td>
<td style="text-align:right;">
1385688.51
</td>
<td style="text-align:right;">
0.34
</td>
<td style="text-align:right;">
163.45
</td>
<td style="text-align:right;">
212.78
</td>
<td style="text-align:right;">
296.46
</td>
<td style="text-align:right;">
100000000\.00
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
1.00
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
52.62
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
▂▃▇▁▁
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
1.00
</td>
<td style="text-align:right;">
-7.37
</td>
<td style="text-align:right;">
1.18
</td>
<td style="text-align:right;">
-10.35
</td>
<td style="text-align:right;">
-8.47
</td>
<td style="text-align:right;">
-6.92
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
</tbody>
</table>

## Handling of missing values - Removing observations and variables

Once the date types have been correctly typed, it is possible to see the
presence of observations with missing number of **bedrooms**, only 2,
and also that about 44% of the observations are missing a value for
**berEPI**. Finally, there are also 298 observations without **price**,
which is the target variable of this study, so those can also be
removed.

For the 2 observations that do not have a valid value for **bedrooms**
and 298 observations without **price**, those will be removed. The
variable **berEPI** will also be removed as it is missing in nearly half
of the observations.

``` r
ireland_houses <- ireland_houses[ , !names(ireland_houses) %in% c("berEPI") ]
ireland_houses <- ireland_houses %>% filter(!is.na(bedrooms))
ireland_houses <- ireland_houses %>% filter(!is.na(price))
```

## Creation of new variables

In this step, we will try create new variables in order to try gain more
insight into the data. The variables that will be created are derived
from **address** and **location**. The goal is to try create a variable
which helps us identify the neighboorhood of the property as best as
possible.

``` r
parse_townOrNeighbourhood <- function(location) {
  
  str_tokens_vec <- str_split( location, "_" )[[1]]
  town_or_neighbourhood <- ""
  
  if (length(str_tokens_vec) == 1) {
    town_or_neighbourhood <-  str_tokens_vec[1]
  } else {
    town_or_neighbourhood <- stri_paste(str_tokens_vec[1 : length(str_tokens_vec)-1], collapse = "_"  )
  }
  
  return (town_or_neighbourhood)
}


parse_county <- function(location) {
  
  str_tokens_vec <- str_split( location, "_" )[[1]]
  county_token <- str_tokens_vec[length(str_tokens_vec)]
  
  if (tolower(county_token) == "city") {
    county_token <- str_tokens_vec[1]
  }
  
  return (county_token)
}


ireland_houses$county <- ireland_houses$location %>% 
  lapply( parse_county ) %>% 
  unlist %>% 
  as.factor


ireland_houses$townOrNeighbourhood <- ireland_houses$location %>% 
  lapply( parse_townOrNeighbourhood ) %>% 
  unlist %>% 
  as.factor
```

## Handling Outliers

This step is focused on trying to find out outliers in our dataset.
Outliers are not desirable as they can have great impact on the
statistical analyses of a machine learning project.

Let’s identify the outliers in our dataset. Only numerical variables
will be analysed initially as those can be found more easily with
techniques such as: histograms, box plots and z-score. Thus, the
variables that will be analysed are: price, size, bedrooms and
bathrooms.

``` r
create_annotations <- function( dfVariable, statsPosition ) {
  
  annotations <- data.frame(
    x = c(
      round(min(dfVariable), 2), 
      round(mean(dfVariable), 2), 
      round(max(dfVariable), 2)
    ),
    y = statsPosition,
    label = c("Min:", "Mean:", "Max:")
  ) 
  
  return (annotations)
}


create_histogram <- function( dataframe, props, labs, annotations ) {

  histogram <- ggplot(dataframe$df, aes(x = !!dataframe$col)) +
      geom_histogram(color = props$color, fill = props$fill, bins = props$bins) +
      labs( title = labs$title,
            x = labs$x,
            y = labs$y
      ) +
      scale_fill_brewer() +
      geom_text(data = annotations,
                aes(x = x, y = y, label = paste(label, x)),
                size = 4,
                fontface="bold")
  
  return (histogram)
}


sizeHistogram <- create_histogram( 
  dataframe = list( df = ireland_houses, col = sym("size") ),
  props = list(color = "darkblue", fill = "lightblue", bins = 30),
  labs  = list(title = "Histogram of house sizes", x = "Size", y = "Observations"),
  annotations = create_annotations(ireland_houses$size,  c(4100, 4700, 200))
)


priceHistogram <- create_histogram( 
  dataframe = list( df = ireland_houses, col = sym("price") ),
  props = list(color = "darkgreen", fill = "lightgreen", bins = 30),
  labs  = list(title = "Histogram of house prices", x = "Price", y = "Observations"),
  annotations = create_annotations(ireland_houses$price,  c(2800, 5500, 100))
)

bathroomsHistogram <- create_histogram( 
  dataframe = list(df = ireland_houses, col = sym("bathrooms") ),
  props = list(color = "deeppink", fill = "lightpink", bins = 15),
  labs  = list(title = "Histogram of number of bathrooms per house", x = "Bathrooms", y = "Observations"),
  annotations = create_annotations(ireland_houses$bathrooms,  c(5600, 3500, 100))
)

bedroomsHistogram <- create_histogram( 
  dataframe = list(df = ireland_houses, col = sym("bedrooms") ),
  props = list(color = "firebrick", fill = "orangered", bins = 15),
  labs  = list(title = "Histogram of number of bedrooms per house", x = "Bedrooms", y = "Observations"),
  annotations = create_annotations(ireland_houses$bedrooms,   c(500, 5000, 100))
)


grid.arrange(
  arrangeGrob(sizeHistogram, priceHistogram),
  arrangeGrob(bedroomsHistogram, bathroomsHistogram), ncol = 2)
```

![](DataCleaning-HousingDataset_files/figure-gfm/-%20create%20histograms%20and%20plot-1.png)<!-- -->

The histograms above show some interesting results in our dataset. For
example, it can be observed that there are properties with over 20
bathrooms or 20 bedrooms, which looks quite unrealistic at first sight,
but when you look it up those properties, you can clearly see that those
are mansions. This helps us to also understand the disparity in the
price of the house, where the minimum cost is about €40,000.00 and the
mean is €462,205.00, nevertheless the maximum price is €15,000,000.00.

The house size histogram does show us some clear outliers however. Those
outliers are houses with a size under 20 square meters for example.
There are 10 observations that fall under that filter, in fact, all of
those observations are under 16 square meters. Looking up the properties
in those 10 address, it is possible to see that those properties have
been incorrectly input in the dataset, so they can be filtered out.

``` r
ireland_houses <- ireland_houses %>% filter(!(size < 17))
```

## Scaling variables

This step will not be performed at this point, as some data exploration
activities are necessary to be carried out beforehand.

## Write Clean Dataset to disk

Finally, after doing some initial data exploration and cleaning, we can
proceed to start analyzing the variance and covariance of the variables
in our dataset, thus diving a little deeper into our analysis.

``` r
dataset_filename <- paste(dataset_directory, 
                          "ireland_houses_cleaned.Rda", 
                          sep="")

save(ireland_houses, file = dataset_filename)
```
