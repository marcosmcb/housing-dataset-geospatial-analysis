Ireland Housing - Data Cleaning
================
Marcos Cavalcante

### Installing libraries

First step is to install and load the necessary libraries.

## Import the Ireland Housing dataset

At this step, the Ireland houses dataset will be imported

``` r
dataset_directory <- "../../datasets/"
dataset_filename <- paste(dataset_directory, "house_listings_all.csv", sep="")

ireland_houses <- read.csv(file = dataset_filename) # Load the dataset
```

## Data Exploration

In this step, the first five rows of our dataset will be displayed so
that we can take a look at the different pieces of data available to us
and what kind of information they bring to the analysis.

``` r
head(ireland_houses, 5)
```

    ##        id daftShortcode                                     title
    ## 1 3984227      19666819             Drumroe, Ardagh, Co. Longford
    ## 2 4003982     112963422                    Lissardowlan, Longford
    ## 3 3999348     112922102       Cartrongarrow, Ardagh, Co. Longford
    ## 4 3990203      19727521           Cloonfide, Moydow, Co. Longford
    ## 5 3979561      19620850 5 Rath Na Gcarraige, Ardagh, Co. Longford
    ##                  price size_meters_squared propertySize bedrooms bathrooms
    ## 1             295000.0                 273       273 m²        6         4
    ## 2             595000.0                 267       267 m²        4         4
    ## 3             130000.0                  NA                     2         1
    ## 4 Price on Application                  NA                     1         1
    ## 5             285000.0                 191       191 m²        4         3
    ##   propertyType publishDate ber_rating  ber_code          ber_epi latitude
    ## 1     Bungalow  2022-08-10         B3 114847999 131.08 kWh/m2/yr 53.68968
    ## 2     Detached  2022-08-02         B3 103099164 140.49 kWh/m2/yr 53.71720
    ## 3     Detached  2022-07-28         E2 107714511  108.1 kWh/m2/yr 53.67240
    ## 4     Detached  2022-07-21     SI_666        NA                  53.66372
    ## 5     Detached  2022-08-03         B2 112836572 114.83 kWh/m2/yr 53.64857
    ##   longitude category             location
    ## 1 -7.684429      Buy ABBEYSHRULE_LONGFORD
    ## 2 -7.726544      Buy ABBEYSHRULE_LONGFORD
    ## 3 -7.728253      Buy ABBEYSHRULE_LONGFORD
    ## 4 -7.787243      Buy ABBEYSHRULE_LONGFORD
    ## 5 -7.702947      Buy ABBEYSHRULE_LONGFORD
    ##                                                                                    url_link
    ## 1                   http://www.daft.ie/for-sale/bungalow-drumroe-ardagh-co-longford/3984227
    ## 2                  http://www.daft.ie/for-sale/detached-house-lissardowlan-longford/4003982
    ## 3       http://www.daft.ie/for-sale/detached-house-cartrongarrow-ardagh-co-longford/3999348
    ## 4           http://www.daft.ie/for-sale/detached-house-cloonfide-moydow-co-longford/3990203
    ## 5 http://www.daft.ie/for-sale/detached-house-5-rath-na-gcarraige-ardagh-co-longford/3979561

Looking at the output of the previous step, some interesting things can
be observed:

-   **id** and **daftShortCode** seem to describe values that look like
    identifiers, but identifiers that are used for different purposes.

-   **title** contains values which look like addresses of properties.

-   **price** are expected to be of *numeric* type, nevertheless,
    strings like *“Price on Application”* are also present.

-   **size_meters_squared** and **propertySize**, at first glance,
    contain the same information / values, however, formatted
    differently. Another interesting point is that there are values
    missing on both variables.

-   **bedrooms** and **bathrooms** contain the amount of each of those
    in the property and should therefore be of *numeric* type.

-   **propertyType** contain values that describe what kind of property
    that is, for example: Bungalow and Detached.

-   **publishDate** is an attribute related more to the ad than to the
    property itself and it describes the date when the ad was published.

-   **ber_rating** is a variable that tells how energy efficient is a
    property, BER stands for Building Energy Rating.

-   **ber_code** is simply the ID of the certificate that the house was
    given.

-   **ber_epi** describes the energy consumption per square meter of a
    the property yearly.

-   **latitude** and **longitude** are spatial values used to locate the
    property on the map.

-   **category** only shows the value of *“Buy”*.

-   **location** contains value with the concatenation of town/city and
    the county.

## Percentage of Missing Values in the dataset per feature

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
  percentage_missing_sorted <- percentage_missing[order(percentage_missing, decreasing = TRUE)]

  percentage_missing_formatted = percent(formattable(percentage_missing_sorted) / 100)

  kbl(percentage_missing_formatted, col.names = NULL) %>%
    kable_paper(bootstrap_options = "striped", full_width = F, html_font = "Computer Modern") %>%
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
43.29%
</td>
</tr>
<tr>
<td style="text-align:left;">
size_meters_squared
</td>
<td style="text-align:right;">
19.91%
</td>
</tr>
<tr>
<td style="text-align:left;">
bathrooms
</td>
<td style="text-align:right;">
1.65%
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

## Count of unique values per feature in the dataset

In this section, it is possible to understand how many distinct values
each feature has. By analysing the results, we can identify that there
is likely duplicate observations in the dataset.

For example, the dataset has over 100 thousand observations, but only
about 13 thousand different values for : *id*, *daftShortCode* and
*url_link*, which are usually used to uniquely identify a record.

``` r
compile_unique_values_table <- function( dfHouses ) {
  
  unique_values_list <- lapply(dfHouses, function(x) length(unique(x)) ) %>% 
    as.list()

  unique_values_sorted <- unique_values_list[ order( unlist(unique_values_list), decreasing = TRUE  ) ]

  unique_values_df <- data.frame( unique_values_sorted )

  kbl(t(unique_values_df)) %>%
    kable_paper(bootstrap_options = "striped", full_width = F, html_font = "Computer Modern") %>%
    kable_styling(fixed_thead = T) %>% 
    add_header_above(header = c("Total Number of Observations", nrow(ireland_houses) ), align = "right") %>%
    add_header_above(header = c("Feature", "Total of Unique Values"))
}

compile_unique_values_table(ireland_houses)
```

<table class=" lightable-paper table" style="font-family: Computer Modern; width: auto !important; margin-left: auto; margin-right: auto; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="1">

<div style="border-bottom: 1px solid #00000020; padding-bottom: 5px; ">

Feature

</div>

</th>
<th style="padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="1">

<div style="border-bottom: 1px solid #00000020; padding-bottom: 5px; ">

Total of Unique Values

</div>

</th>
</tr>
<tr>
<th style="padding-bottom:0; padding-left:3px;padding-right:3px;text-align: right; " colspan="1">

<div style="border-bottom: 1px solid #00000020; padding-bottom: 5px; ">

Total Number of Observations

</div>

</th>
<th style="padding-bottom:0; padding-left:3px;padding-right:3px;text-align: right; " colspan="1">

<div style="border-bottom: 1px solid #00000020; padding-bottom: 5px; ">

100294

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
12860
</td>
</tr>
<tr>
<td style="text-align:left;">
daftShortcode
</td>
<td style="text-align:right;">
12860
</td>
</tr>
<tr>
<td style="text-align:left;">
url_link
</td>
<td style="text-align:right;">
12860
</td>
</tr>
<tr>
<td style="text-align:left;">
title
</td>
<td style="text-align:right;">
12362
</td>
</tr>
<tr>
<td style="text-align:left;">
longitude
</td>
<td style="text-align:right;">
12275
</td>
</tr>
<tr>
<td style="text-align:left;">
latitude
</td>
<td style="text-align:right;">
12246
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_code
</td>
<td style="text-align:right;">
7232
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_epi
</td>
<td style="text-align:right;">
5674
</td>
</tr>
<tr>
<td style="text-align:left;">
price
</td>
<td style="text-align:right;">
705
</td>
</tr>
<tr>
<td style="text-align:left;">
propertySize
</td>
<td style="text-align:right;">
582
</td>
</tr>
<tr>
<td style="text-align:left;">
size_meters_squared
</td>
<td style="text-align:right;">
528
</td>
</tr>
<tr>
<td style="text-align:left;">
location
</td>
<td style="text-align:right;">
271
</td>
</tr>
<tr>
<td style="text-align:left;">
publishDate
</td>
<td style="text-align:right;">
179
</td>
</tr>
<tr>
<td style="text-align:left;">
bedrooms
</td>
<td style="text-align:right;">
45
</td>
</tr>
<tr>
<td style="text-align:left;">
bathrooms
</td>
<td style="text-align:right;">
21
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_rating
</td>
<td style="text-align:right;">
17
</td>
</tr>
<tr>
<td style="text-align:left;">
propertyType
</td>
<td style="text-align:right;">
10
</td>
</tr>
<tr>
<td style="text-align:left;">
category
</td>
<td style="text-align:right;">
2
</td>
</tr>
</tbody>
</table>

## Further Investigation

After doing some data exploration and gaining some insight into the
dataset, the next step is to look at the descriptive statistics of the
features in the dataset in order to get a general summary of the dataset
as a whole and explore properties like:

-   **Data types**
-   **Min and Max values**
-   **Completion rate**
-   **Mean**
-   **Percentiles**

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
100294
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
18
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
11
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
title
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
12
</td>
<td style="text-align:right;">
105
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12362
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
705
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
propertySize
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
11
</td>
<td style="text-align:right;">
19734
</td>
<td style="text-align:right;">
582
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
9
</td>
<td style="text-align:right;">
187
</td>
<td style="text-align:right;">
45
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
40
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
publishDate
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
179
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
3919
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
50104
</td>
<td style="text-align:right;">
5674
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
category
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
3
</td>
<td style="text-align:right;">
9
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
2
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
68
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
271
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
url_link
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
62
</td>
<td style="text-align:right;">
193
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12860
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
id
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3842395.83
</td>
<td style="text-align:right;">
362289.37
</td>
<td style="text-align:right;">
6800.00
</td>
<td style="text-align:right;">
3805133.00
</td>
<td style="text-align:right;">
3933349.50
</td>
<td style="text-align:right;">
3974191.00
</td>
<td style="text-align:right;">
4019790.00
</td>
<td style="text-align:left;">
▁▁▁▁▇
</td>
</tr>
<tr>
<td style="text-align:left;">
daftShortcode
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
28263078.16
</td>
<td style="text-align:right;">
28413858.53
</td>
<td style="text-align:right;">
1319566.00
</td>
<td style="text-align:right;">
18690195.00
</td>
<td style="text-align:right;">
19258514.00
</td>
<td style="text-align:right;">
19593376.00
</td>
<td style="text-align:right;">
113071717\.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
size_meters_squared
</td>
<td style="text-align:right;">
19967
</td>
<td style="text-align:right;">
0.80
</td>
<td style="text-align:right;">
131.94
</td>
<td style="text-align:right;">
163.58
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
75.00
</td>
<td style="text-align:right;">
102.00
</td>
<td style="text-align:right;">
147.00
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
1658
</td>
<td style="text-align:right;">
0.98
</td>
<td style="text-align:right;">
2.13
</td>
<td style="text-align:right;">
1.47
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
32.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
ber_code
</td>
<td style="text-align:right;">
43417
</td>
<td style="text-align:right;">
0.57
</td>
<td style="text-align:right;">
113341265\.10
</td>
<td style="text-align:right;">
44218210.12
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
106661911\.00
</td>
<td style="text-align:right;">
113473896\.00
</td>
<td style="text-align:right;">
114880636\.00
</td>
<td style="text-align:right;">
1134291201.00
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
53.18
</td>
<td style="text-align:right;">
0.53
</td>
<td style="text-align:right;">
51.44
</td>
<td style="text-align:right;">
53.28
</td>
<td style="text-align:right;">
53.34
</td>
<td style="text-align:right;">
53.37
</td>
<td style="text-align:right;">
55.38
</td>
<td style="text-align:left;">
▁▁▇▁▁
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
-6.82
</td>
<td style="text-align:right;">
1.01
</td>
<td style="text-align:right;">
-10.45
</td>
<td style="text-align:right;">
-6.80
</td>
<td style="text-align:right;">
-6.28
</td>
<td style="text-align:right;">
-6.25
</td>
<td style="text-align:right;">
-6.01
</td>
<td style="text-align:left;">
▁▁▁▁▇
</td>
</tr>
</tbody>
</table>

The output of the skim function shows us that our findings from the
initial data exploration are correct. For example, there are over 100
thousand observations in the dataset, but only about 12 thousand unique
values, it can also be seen that the datatypes used for some of the
features are clearly not right, for instance price is of type character.

Furthermore, there are features with a high number of missing values,
for example: *size* and *ber_code*. There is potentially more missing
values on other features, however, those are hidden for now due to the
wrong data type being used.

# Data Cleaning

This step will be completed in the following stages:

-   *Rename Variables*
-   *Removal of Duplicate observations*
-   *Convert variables into appropriate data types*
-   *Remove observations with missing values*

## Data Transformation - Renaming Variables

It was seen that some of the variables did not follow a naming standard
and used an adequate name, for example: *title* actually refers to the
*address* of the house and *size_meters_squared* refers to the *size*.

The naming convention used across the variables is **camel-case**,
therefore *ber_rating* and *ber_epi* will be renamed to *berRating* and
*berEPI* respectively.

``` r
ireland_houses <- rename( ireland_houses, 
  address = title,
  size = size_meters_squared,
  berRating = ber_rating,
  berEPI = ber_epi,
  urlLink = url_link,
  berCode = ber_code
)
```

## Data Cleaning - Removal of Duplicates

As it was seen before, there are many duplicate values, in fact, only
about 12% of the observations are unique. In order to remove the
duplicate values, the feature *url_link* will be used to filter out any
duplicate observations.

The rationale behind using the *url_link* is that URLs are guaranteed to
be unique across the internet and they are a concatenation of: property
type + address + id. Thus, by removing observations which have the same
URL, we are sure to remove observations that are the very same because
they were put on sale on the websites more than once and got different
ids.

So, in the step below, a new column, *urlNoId*, will be created from the
*urlLink* feature, however without the id information.

``` r
remove_id_from_url <- function(url) {
  url_tokens <- str_split(url, pattern = "/")[[1]]
  
  url_tokens_without_id <- stri_paste( url_tokens[1 : length(url_tokens) - 1], collapse = "/"  )
  return(url_tokens_without_id)
}


ireland_houses$urlNoId <- ireland_houses$urlLink %>%
  lapply(remove_id_from_url) %>%
  unlist
  
ireland_houses <- ireland_houses %>%
  distinct(urlNoId, .keep_all = T)


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
12586
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
19
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
12
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
12
</td>
<td style="text-align:right;">
105
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12354
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
699
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
propertySize
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
11
</td>
<td style="text-align:right;">
3239
</td>
<td style="text-align:right;">
578
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
9
</td>
<td style="text-align:right;">
42
</td>
<td style="text-align:right;">
42
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
7
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
publishDate
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
176
</td>
<td style="text-align:right;">
0
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
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
6
</td>
<td style="text-align:right;">
418
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
berEPI
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
6334
</td>
<td style="text-align:right;">
5612
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
category
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
3
</td>
<td style="text-align:right;">
9
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
2
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
126
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlLink
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
62
</td>
<td style="text-align:right;">
193
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12586
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlNoId
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
54
</td>
<td style="text-align:right;">
185
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12586
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
id
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3807180.78
</td>
<td style="text-align:right;">
484716.43
</td>
<td style="text-align:right;">
6800.00
</td>
<td style="text-align:right;">
3799357.00
</td>
<td style="text-align:right;">
3936423.00
</td>
<td style="text-align:right;">
3981312.75
</td>
<td style="text-align:right;">
4019790.00
</td>
<td style="text-align:left;">
▁▁▁▁▇
</td>
</tr>
<tr>
<td style="text-align:left;">
daftShortcode
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
31943300.77
</td>
<td style="text-align:right;">
32940821.61
</td>
<td style="text-align:right;">
1319566.00
</td>
<td style="text-align:right;">
18643729.00
</td>
<td style="text-align:right;">
19290126.00
</td>
<td style="text-align:right;">
19630261.00
</td>
<td style="text-align:right;">
113071717\.00
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
3311
</td>
<td style="text-align:right;">
0.74
</td>
<td style="text-align:right;">
147.55
</td>
<td style="text-align:right;">
162.45
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
165.00
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
251
</td>
<td style="text-align:right;">
0.98
</td>
<td style="text-align:right;">
2.30
</td>
<td style="text-align:right;">
1.36
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
32.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
berCode
</td>
<td style="text-align:right;">
5330
</td>
<td style="text-align:right;">
0.58
</td>
<td style="text-align:right;">
116162343\.21
</td>
<td style="text-align:right;">
60793991.08
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
106956786\.25
</td>
<td style="text-align:right;">
113669352\.50
</td>
<td style="text-align:right;">
114881650\.25
</td>
<td style="text-align:right;">
1134291201.00
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
53.10
</td>
<td style="text-align:right;">
0.73
</td>
<td style="text-align:right;">
51.44
</td>
<td style="text-align:right;">
52.60
</td>
<td style="text-align:right;">
53.29
</td>
<td style="text-align:right;">
53.44
</td>
<td style="text-align:right;">
55.38
</td>
<td style="text-align:left;">
▂▃▇▂▁
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
-7.47
</td>
<td style="text-align:right;">
1.20
</td>
<td style="text-align:right;">
-10.45
</td>
<td style="text-align:right;">
-8.51
</td>
<td style="text-align:right;">
-7.18
</td>
<td style="text-align:right;">
-6.30
</td>
<td style="text-align:right;">
-6.01
</td>
<td style="text-align:left;">
▁▃▃▂▇
</td>
</tr>
</tbody>
</table>

``` r
compile_missing_values_table(ireland_houses)
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
berCode
</td>
<td style="text-align:right;">
42.35%
</td>
</tr>
<tr>
<td style="text-align:left;">
size
</td>
<td style="text-align:right;">
26.31%
</td>
</tr>
<tr>
<td style="text-align:left;">
bathrooms
</td>
<td style="text-align:right;">
1.99%
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
address
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
berRating
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
berEPI
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
urlLink
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
<tr>
<td style="text-align:left;">
urlNoId
</td>
<td style="text-align:right;">
0.00%
</td>
</tr>
</tbody>
</table>

## Data Transformation - Convert variables into appropriate Data Types

The output of the **skim** function has showed some interesting details,
for instance: *price*, *berEPI*, and *bedrooms* are of type
**character**, when, in fact, **numeric** would be a better type because
they represent quantitative data.

*propertyType*, *category* and *berRating* are of type characters,
however, **factor** may be a better type because there is a limited
number of categorical values they can hold, **factor** is also a better
type as it allows for better data manipulation so that typos can be
avoided and sorting the data in a meaningful way becomes possible.

Thus, in this next step, the data will be tidied up in a better manner.

``` r
ireland_houses <- mutate(
  ireland_houses,
  price = parse_number(price),
  berEPI = as.numeric(str_remove(berEPI, "kWh/m2/yr")),
  bedrooms = as.numeric(bedrooms),
  
  propertyType = as.factor(propertyType),
  category = as.factor(category),
  berRating = as.factor(berRating)
)
```

    ## Warning: 582 parsing failures.
    ## row col expected               actual
    ##   4  -- a number Price on Application
    ## 225  -- a number Price on Application
    ## 231  -- a number Price on Application
    ## 232  -- a number Price on Application
    ## 233  -- a number Price on Application
    ## ... ... ........ ....................
    ## See problems(...) for more details.

    ## Warning in mask$eval_all_mutate(quo): NAs introduced by coercion

``` r
skim(ireland_houses)
```

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

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
12586
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
19
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
6
</td>
</tr>
<tr>
<td style="text-align:left;">
factor
</td>
<td style="text-align:left;">
3
</td>
</tr>
<tr>
<td style="text-align:left;">
numeric
</td>
<td style="text-align:left;">
10
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
12
</td>
<td style="text-align:right;">
105
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12354
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
propertySize
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
11
</td>
<td style="text-align:right;">
3239
</td>
<td style="text-align:right;">
578
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
publishDate
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
176
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
126
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlLink
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
62
</td>
<td style="text-align:right;">
193
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12586
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlNoId
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
54
</td>
<td style="text-align:right;">
185
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12586
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
10
</td>
<td style="text-align:left;">
Det: 4987, Sem: 3152, Ter: 1951, Apa: 1255
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
C3: 1491, C2: 1411, C1: 1351, D1: 1328
</td>
</tr>
<tr>
<td style="text-align:left;">
category
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
2
</td>
<td style="text-align:left;">
Buy: 12322, New: 264
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
id
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3807180.78
</td>
<td style="text-align:right;">
484716.43
</td>
<td style="text-align:right;">
6800.00
</td>
<td style="text-align:right;">
3799357.00
</td>
<td style="text-align:right;">
3936423.00
</td>
<td style="text-align:right;">
3981312.75
</td>
<td style="text-align:right;">
4019790.00
</td>
<td style="text-align:left;">
▁▁▁▁▇
</td>
</tr>
<tr>
<td style="text-align:left;">
daftShortcode
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
31943300.77
</td>
<td style="text-align:right;">
32940821.61
</td>
<td style="text-align:right;">
1319566.00
</td>
<td style="text-align:right;">
18643729.00
</td>
<td style="text-align:right;">
19290126.00
</td>
<td style="text-align:right;">
19630261.00
</td>
<td style="text-align:right;">
113071717\.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
price
</td>
<td style="text-align:right;">
582
</td>
<td style="text-align:right;">
0.95
</td>
<td style="text-align:right;">
426185.05
</td>
<td style="text-align:right;">
508200.62
</td>
<td style="text-align:right;">
25000.00
</td>
<td style="text-align:right;">
225000.00
</td>
<td style="text-align:right;">
320000.00
</td>
<td style="text-align:right;">
465000.00
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
3311
</td>
<td style="text-align:right;">
0.74
</td>
<td style="text-align:right;">
147.55
</td>
<td style="text-align:right;">
162.45
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
165.00
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
46
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3.41
</td>
<td style="text-align:right;">
1.40
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
40.00
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
251
</td>
<td style="text-align:right;">
0.98
</td>
<td style="text-align:right;">
2.30
</td>
<td style="text-align:right;">
1.36
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
32.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
berCode
</td>
<td style="text-align:right;">
5330
</td>
<td style="text-align:right;">
0.58
</td>
<td style="text-align:right;">
116162343\.21
</td>
<td style="text-align:right;">
60793991.08
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
106956786\.25
</td>
<td style="text-align:right;">
113669352\.50
</td>
<td style="text-align:right;">
114881650\.25
</td>
<td style="text-align:right;">
1134291201.00
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
6334
</td>
<td style="text-align:right;">
0.50
</td>
<td style="text-align:right;">
48371.56
</td>
<td style="text-align:right;">
2190185.66
</td>
<td style="text-align:right;">
1.30
</td>
<td style="text-align:right;">
165.64
</td>
<td style="text-align:right;">
214.39
</td>
<td style="text-align:right;">
298.66
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
53.10
</td>
<td style="text-align:right;">
0.73
</td>
<td style="text-align:right;">
51.44
</td>
<td style="text-align:right;">
52.60
</td>
<td style="text-align:right;">
53.29
</td>
<td style="text-align:right;">
53.44
</td>
<td style="text-align:right;">
55.38
</td>
<td style="text-align:left;">
▂▃▇▂▁
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
-7.47
</td>
<td style="text-align:right;">
1.20
</td>
<td style="text-align:right;">
-10.45
</td>
<td style="text-align:right;">
-8.51
</td>
<td style="text-align:right;">
-7.18
</td>
<td style="text-align:right;">
-6.30
</td>
<td style="text-align:right;">
-6.01
</td>
<td style="text-align:left;">
▁▃▃▂▇
</td>
</tr>
</tbody>
</table>

## Data Cleaning - Removing observations without Price

Once the date types have been sorted, it is possible to see the presence
of missing data in many of the variables in our dataset.

For example: \* *berEPI* is missing in about *50%* of the observations;
\* *berCode* is missing in about *42%* of the observations; \* *size* is
missing in *26%* of the observations; \* *price* is missing in about
*5%* of the observations; \* *bathrooms* is missing in about *2%* of the
observations; \* There are 46 out of 12.586 observations where number of
*bedrooms* is missing.

At this stage, the only observations that can be removed are those
without the price variable because that is the target variable of the
analysis.

``` r
ireland_houses <- ireland_houses %>% filter(!is.na(price))
skim(ireland_houses)
```

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

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
12004
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
19
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
6
</td>
</tr>
<tr>
<td style="text-align:left;">
factor
</td>
<td style="text-align:left;">
3
</td>
</tr>
<tr>
<td style="text-align:left;">
numeric
</td>
<td style="text-align:left;">
10
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
12
</td>
<td style="text-align:right;">
105
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
11860
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
propertySize
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
11
</td>
<td style="text-align:right;">
2943
</td>
<td style="text-align:right;">
562
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
publishDate
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
169
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
125
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlLink
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
62
</td>
<td style="text-align:right;">
193
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12004
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlNoId
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
54
</td>
<td style="text-align:right;">
185
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12004
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
10
</td>
<td style="text-align:left;">
Det: 4652, Sem: 3033, Ter: 1893, Apa: 1236
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
C3: 1458, C2: 1381, C1: 1315, D1: 1287
</td>
</tr>
<tr>
<td style="text-align:left;">
category
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
2
</td>
<td style="text-align:left;">
Buy: 11845, New: 159
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
id
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3828177.33
</td>
<td style="text-align:right;">
432292.05
</td>
<td style="text-align:right;">
6800.00
</td>
<td style="text-align:right;">
3806936.50
</td>
<td style="text-align:right;">
3938365.50
</td>
<td style="text-align:right;">
3981955.00
</td>
<td style="text-align:right;">
4019790.00
</td>
<td style="text-align:left;">
▁▁▁▁▇
</td>
</tr>
<tr>
<td style="text-align:left;">
daftShortcode
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
32446197.79
</td>
<td style="text-align:right;">
33343640.55
</td>
<td style="text-align:right;">
1319566.00
</td>
<td style="text-align:right;">
18713703.00
</td>
<td style="text-align:right;">
19309910.00
</td>
<td style="text-align:right;">
19637715.75
</td>
<td style="text-align:right;">
113071717\.00
</td>
<td style="text-align:left;">
▇▁▁▁▂
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
1.00
</td>
<td style="text-align:right;">
426185.05
</td>
<td style="text-align:right;">
508200.62
</td>
<td style="text-align:right;">
25000.00
</td>
<td style="text-align:right;">
225000.00
</td>
<td style="text-align:right;">
320000.00
</td>
<td style="text-align:right;">
465000.00
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
3013
</td>
<td style="text-align:right;">
0.75
</td>
<td style="text-align:right;">
146.23
</td>
<td style="text-align:right;">
163.01
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
85.00
</td>
<td style="text-align:right;">
112.00
</td>
<td style="text-align:right;">
162.50
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
37
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3.40
</td>
<td style="text-align:right;">
1.40
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
40.00
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
226
</td>
<td style="text-align:right;">
0.98
</td>
<td style="text-align:right;">
2.29
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
32.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
berCode
</td>
<td style="text-align:right;">
4942
</td>
<td style="text-align:right;">
0.59
</td>
<td style="text-align:right;">
115694143\.82
</td>
<td style="text-align:right;">
58503906.62
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
106898801\.75
</td>
<td style="text-align:right;">
113640903\.00
</td>
<td style="text-align:right;">
114882055\.25
</td>
<td style="text-align:right;">
1134291201.00
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
5907
</td>
<td style="text-align:right;">
0.51
</td>
<td style="text-align:right;">
49594.30
</td>
<td style="text-align:right;">
2217841.67
</td>
<td style="text-align:right;">
1.30
</td>
<td style="text-align:right;">
165.76
</td>
<td style="text-align:right;">
214.45
</td>
<td style="text-align:right;">
298.37
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
53.11
</td>
<td style="text-align:right;">
0.72
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
53.43
</td>
<td style="text-align:right;">
55.38
</td>
<td style="text-align:left;">
▂▃▇▂▁
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
-7.44
</td>
<td style="text-align:right;">
1.20
</td>
<td style="text-align:right;">
-10.45
</td>
<td style="text-align:right;">
-8.50
</td>
<td style="text-align:right;">
-7.09
</td>
<td style="text-align:right;">
-6.30
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

``` r
calc_area_size <- function( price_in_meter, price_in_ac ) {
  if ( is.na(price_in_meter) ) {
    acre_in_meters_ireland = 6555
    my_size <- as.numeric(str_remove(price_in_ac, "ac"))
    return( my_size * acre_in_meters_ireland )
  }
  
  return (price_in_meter)
}

ireland_houses$size <- mapply(calc_area_size, ireland_houses$size, ireland_houses$propertySize)

skim(ireland_houses)
```

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

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
12004
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
19
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
6
</td>
</tr>
<tr>
<td style="text-align:left;">
factor
</td>
<td style="text-align:left;">
3
</td>
</tr>
<tr>
<td style="text-align:left;">
numeric
</td>
<td style="text-align:left;">
10
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
12
</td>
<td style="text-align:right;">
105
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
11860
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
propertySize
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
11
</td>
<td style="text-align:right;">
2943
</td>
<td style="text-align:right;">
562
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
publishDate
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
169
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
125
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlLink
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
62
</td>
<td style="text-align:right;">
193
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12004
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlNoId
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
54
</td>
<td style="text-align:right;">
185
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
12004
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
10
</td>
<td style="text-align:left;">
Det: 4652, Sem: 3033, Ter: 1893, Apa: 1236
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
C3: 1458, C2: 1381, C1: 1315, D1: 1287
</td>
</tr>
<tr>
<td style="text-align:left;">
category
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
2
</td>
<td style="text-align:left;">
Buy: 11845, New: 159
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
id
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3828177.33
</td>
<td style="text-align:right;">
432292.05
</td>
<td style="text-align:right;">
6800.00
</td>
<td style="text-align:right;">
3806936.50
</td>
<td style="text-align:right;">
3938365.50
</td>
<td style="text-align:right;">
3981955.00
</td>
<td style="text-align:right;">
4019790.00
</td>
<td style="text-align:left;">
▁▁▁▁▇
</td>
</tr>
<tr>
<td style="text-align:left;">
daftShortcode
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
32446197.79
</td>
<td style="text-align:right;">
33343640.55
</td>
<td style="text-align:right;">
1319566.00
</td>
<td style="text-align:right;">
18713703.00
</td>
<td style="text-align:right;">
19309910.00
</td>
<td style="text-align:right;">
19637715.75
</td>
<td style="text-align:right;">
113071717\.00
</td>
<td style="text-align:left;">
▇▁▁▁▂
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
1.00
</td>
<td style="text-align:right;">
426185.05
</td>
<td style="text-align:right;">
508200.62
</td>
<td style="text-align:right;">
25000.00
</td>
<td style="text-align:right;">
225000.00
</td>
<td style="text-align:right;">
320000.00
</td>
<td style="text-align:right;">
465000.00
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
2943
</td>
<td style="text-align:right;">
0.75
</td>
<td style="text-align:right;">
24759.53
</td>
<td style="text-align:right;">
2273056.02
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
85.00
</td>
<td style="text-align:right;">
112.00
</td>
<td style="text-align:right;">
165.00
</td>
<td style="text-align:right;">
216314868\.90
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
37
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3.40
</td>
<td style="text-align:right;">
1.40
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
40.00
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
226
</td>
<td style="text-align:right;">
0.98
</td>
<td style="text-align:right;">
2.29
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
32.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
berCode
</td>
<td style="text-align:right;">
4942
</td>
<td style="text-align:right;">
0.59
</td>
<td style="text-align:right;">
115694143\.82
</td>
<td style="text-align:right;">
58503906.62
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
106898801\.75
</td>
<td style="text-align:right;">
113640903\.00
</td>
<td style="text-align:right;">
114882055\.25
</td>
<td style="text-align:right;">
1134291201.00
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
5907
</td>
<td style="text-align:right;">
0.51
</td>
<td style="text-align:right;">
49594.30
</td>
<td style="text-align:right;">
2217841.67
</td>
<td style="text-align:right;">
1.30
</td>
<td style="text-align:right;">
165.76
</td>
<td style="text-align:right;">
214.45
</td>
<td style="text-align:right;">
298.37
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
53.11
</td>
<td style="text-align:right;">
0.72
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
53.43
</td>
<td style="text-align:right;">
55.38
</td>
<td style="text-align:left;">
▂▃▇▂▁
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
-7.44
</td>
<td style="text-align:right;">
1.20
</td>
<td style="text-align:right;">
-10.45
</td>
<td style="text-align:right;">
-8.50
</td>
<td style="text-align:right;">
-7.09
</td>
<td style="text-align:right;">
-6.30
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

``` r
numeric_data <- ireland_houses %>% 
  select(price, size, bedrooms, bathrooms, berCode, berEPI, latitude, longitude) 


skim(numeric_data)
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
numeric_data
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of rows
</td>
<td style="text-align:left;">
12004
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
8
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
numeric
</td>
<td style="text-align:left;">
8
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
1.00
</td>
<td style="text-align:right;">
426185.05
</td>
<td style="text-align:right;">
508200.62
</td>
<td style="text-align:right;">
25000.00
</td>
<td style="text-align:right;">
225000.00
</td>
<td style="text-align:right;">
320000.00
</td>
<td style="text-align:right;">
465000.00
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
2943
</td>
<td style="text-align:right;">
0.75
</td>
<td style="text-align:right;">
24759.53
</td>
<td style="text-align:right;">
2273056.02
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
85.00
</td>
<td style="text-align:right;">
112.00
</td>
<td style="text-align:right;">
165.00
</td>
<td style="text-align:right;">
216314868\.90
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
37
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3.40
</td>
<td style="text-align:right;">
1.40
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
40.00
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
226
</td>
<td style="text-align:right;">
0.98
</td>
<td style="text-align:right;">
2.29
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
32.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
berCode
</td>
<td style="text-align:right;">
4942
</td>
<td style="text-align:right;">
0.59
</td>
<td style="text-align:right;">
115694143\.82
</td>
<td style="text-align:right;">
58503906.62
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
106898801\.75
</td>
<td style="text-align:right;">
113640903\.00
</td>
<td style="text-align:right;">
114882055\.25
</td>
<td style="text-align:right;">
1134291201.00
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
5907
</td>
<td style="text-align:right;">
0.51
</td>
<td style="text-align:right;">
49594.30
</td>
<td style="text-align:right;">
2217841.67
</td>
<td style="text-align:right;">
1.30
</td>
<td style="text-align:right;">
165.76
</td>
<td style="text-align:right;">
214.45
</td>
<td style="text-align:right;">
298.37
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
53.11
</td>
<td style="text-align:right;">
0.72
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
53.43
</td>
<td style="text-align:right;">
55.38
</td>
<td style="text-align:left;">
▂▃▇▂▁
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
-7.44
</td>
<td style="text-align:right;">
1.20
</td>
<td style="text-align:right;">
-10.45
</td>
<td style="text-align:right;">
-8.50
</td>
<td style="text-align:right;">
-7.09
</td>
<td style="text-align:right;">
-6.30
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

``` r
plot( price ~ size, data = numeric_data, main = "Scatter plot of data" )
```

![](DataCleaning-HousingDataset_files/figure-gfm/Data%20Exploration%20-%20Correlation-1.png)<!-- -->

``` r
cor.test( numeric_data$price, numeric_data$size, use = "complete.obs"  )
```

    ## 
    ##  Pearson's product-moment correlation
    ## 
    ## data:  numeric_data$price and numeric_data$size
    ## t = 0.29634, df = 9059, p-value = 0.767
    ## alternative hypothesis: true correlation is not equal to 0
    ## 95 percent confidence interval:
    ##  -0.01747828  0.02370266
    ## sample estimates:
    ##        cor 
    ## 0.00311351

``` r
cor( numeric_data$price, numeric_data$bedrooms, use = "complete.obs"  )
```

    ## [1] 0.3907015

``` r
cor( numeric_data$price, numeric_data$bathrooms, use = "complete.obs"  )
```

    ## [1] 0.3957492

``` r
cor( numeric_data$price, numeric_data$berCode, use = "complete.obs"  )
```

    ## [1] 0.004463803

``` r
cor( numeric_data$price, numeric_data$berEPI, use = "complete.obs"  )
```

    ## [1] -0.005456323

``` r
cor( numeric_data$price, numeric_data$latitude, use = "complete.obs"  )
```

    ## [1] 0.006207031

``` r
cor( numeric_data$price, numeric_data$longitude, use = "complete.obs"  )
```

    ## [1] 0.2067253

``` r
sum( with( numeric_data, bedrooms > 10 | bathrooms > 10  )  )
```

    ## [1] NA

``` r
ireland_houses_lm <- numeric_data %>%
  filter(!is.na(size)) %>%
  
  filter(!is.na(bedrooms)) 
  

#Estimando o modelo
modelo_tempodist <- lm(formula = price ~ bedrooms + size + bathrooms + longitude,
                       data = ireland_houses_lm)

#Observando os parâmetros do modelo_tempodist
summary(modelo_tempodist)
```

    ## 
    ## Call:
    ## lm(formula = price ~ bedrooms + size + bathrooms + longitude, 
    ##     data = ireland_houses_lm)
    ## 
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max 
    ## -3227645  -183158   -52016    80860 13556622 
    ## 
    ## Coefficients:
    ##               Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)  8.027e+05  3.313e+04  24.228   <2e-16 ***
    ## bedrooms     1.106e+05  5.359e+03  20.630   <2e-16 ***
    ## size        -9.994e-04  2.229e-03  -0.448    0.654    
    ## bathrooms    9.161e+04  5.302e+03  17.277   <2e-16 ***
    ## longitude    1.275e+05  4.405e+03  28.934   <2e-16 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 481900 on 8919 degrees of freedom
    ##   (121 observations deleted due to missingness)
    ## Multiple R-squared:  0.2409, Adjusted R-squared:  0.2406 
    ## F-statistic: 707.8 on 4 and 8919 DF,  p-value: < 2.2e-16

``` r
numeric_data %>%
  correlation(method = "pearson") %>%
  plot()
```

![](DataCleaning-HousingDataset_files/figure-gfm/Data%20Exploration%20-%20Correlation-2.png)<!-- -->

``` r
chart.Correlation((numeric_data), histogram = TRUE)
```

    ## Warning in hist.default(x, col = "light gray", probability = TRUE, axes =
    ## FALSE, : 'breaks = 2.81855e+07' is too large and set to 1e6

    ## Warning in hist.default(x, col = "light gray", probability = TRUE, axes =
    ## FALSE, : 'breaks = 6.8881e+06' is too large and set to 1e6

![](DataCleaning-HousingDataset_files/figure-gfm/Data%20Exploration%20-%20Correlation-3.png)<!-- -->

``` r
ireland_houses_cleaned <- ireland_houses %>%
  filter(!is.na(price)) %>%
  filter(!is.na(propertySize)) %>%
  filter(!is.na(bathrooms)) %>%
  filter(!is.na(bedrooms))
  
skim(ireland_houses_cleaned)
```

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

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
ireland_houses_cleaned
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of rows
</td>
<td style="text-align:left;">
11771
</td>
</tr>
<tr>
<td style="text-align:left;">
Number of columns
</td>
<td style="text-align:left;">
19
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
6
</td>
</tr>
<tr>
<td style="text-align:left;">
factor
</td>
<td style="text-align:left;">
3
</td>
</tr>
<tr>
<td style="text-align:left;">
numeric
</td>
<td style="text-align:left;">
10
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
12
</td>
<td style="text-align:right;">
102
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
11634
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
propertySize
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
11
</td>
<td style="text-align:right;">
2847
</td>
<td style="text-align:right;">
544
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
publishDate
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
167
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
124
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlLink
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
62
</td>
<td style="text-align:right;">
180
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
11771
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
urlNoId
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
54
</td>
<td style="text-align:right;">
172
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
11771
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
9
</td>
<td style="text-align:left;">
Det: 4511, Sem: 2999, Ter: 1866, Apa: 1219
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
C3: 1443, C2: 1374, C1: 1313, D1: 1275
</td>
</tr>
<tr>
<td style="text-align:left;">
category
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
2
</td>
<td style="text-align:left;">
Buy: 11621, New: 150
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
id
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
3831260.70
</td>
<td style="text-align:right;">
424356.58
</td>
<td style="text-align:right;">
6800.00
</td>
<td style="text-align:right;">
3807539.00
</td>
<td style="text-align:right;">
3938718.00
</td>
<td style="text-align:right;">
3982070.50
</td>
<td style="text-align:right;">
4019790.00
</td>
<td style="text-align:left;">
▁▁▁▁▇
</td>
</tr>
<tr>
<td style="text-align:left;">
daftShortcode
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1.00
</td>
<td style="text-align:right;">
32477718.34
</td>
<td style="text-align:right;">
33367218.44
</td>
<td style="text-align:right;">
1319566.00
</td>
<td style="text-align:right;">
18718947.00
</td>
<td style="text-align:right;">
19312135.00
</td>
<td style="text-align:right;">
19639182.50
</td>
<td style="text-align:right;">
113071717\.00
</td>
<td style="text-align:left;">
▇▁▁▁▂
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
1.00
</td>
<td style="text-align:right;">
426245.03
</td>
<td style="text-align:right;">
502611.14
</td>
<td style="text-align:right;">
30000.00
</td>
<td style="text-align:right;">
228500.00
</td>
<td style="text-align:right;">
320000.00
</td>
<td style="text-align:right;">
465000.00
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
2847
</td>
<td style="text-align:right;">
0.76
</td>
<td style="text-align:right;">
25090.66
</td>
<td style="text-align:right;">
2290437.15
</td>
<td style="text-align:right;">
1.00
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
216314868\.90
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
1.00
</td>
<td style="text-align:right;">
3.40
</td>
<td style="text-align:right;">
1.39
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
40.00
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
2.29
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
32.00
</td>
<td style="text-align:left;">
▇▁▁▁▁
</td>
</tr>
<tr>
<td style="text-align:left;">
berCode
</td>
<td style="text-align:right;">
4794
</td>
<td style="text-align:right;">
0.59
</td>
<td style="text-align:right;">
115553210\.80
</td>
<td style="text-align:right;">
57699941.51
</td>
<td style="text-align:right;">
0.00
</td>
<td style="text-align:right;">
106884257\.00
</td>
<td style="text-align:right;">
113640239\.00
</td>
<td style="text-align:right;">
114881964\.00
</td>
<td style="text-align:right;">
1134291201.00
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
5756
</td>
<td style="text-align:right;">
0.51
</td>
<td style="text-align:right;">
50265.96
</td>
<td style="text-align:right;">
2232902.94
</td>
<td style="text-align:right;">
1.30
</td>
<td style="text-align:right;">
165.71
</td>
<td style="text-align:right;">
214.02
</td>
<td style="text-align:right;">
297.60
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
53.10
</td>
<td style="text-align:right;">
0.72
</td>
<td style="text-align:right;">
51.44
</td>
<td style="text-align:right;">
52.61
</td>
<td style="text-align:right;">
53.29
</td>
<td style="text-align:right;">
53.43
</td>
<td style="text-align:right;">
55.38
</td>
<td style="text-align:left;">
▂▃▇▂▁
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
-7.44
</td>
<td style="text-align:right;">
1.20
</td>
<td style="text-align:right;">
-10.45
</td>
<td style="text-align:right;">
-8.50
</td>
<td style="text-align:right;">
-7.08
</td>
<td style="text-align:right;">
-6.30
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

The last step removed 22.260 observations, which represents about 22.2%
of all the observations. As the data tidy up process is done, the
resulting data frame can be written to disk in CSV format.

## Data Transformation - Deriving other variables

In this step, the address variable will be studied further. The address
information is a concatenation of building or apartment number, street
name, neighborhood and post town or city. In order to gather more
meaningful information from the address variable, the post town or city
information will be extracted into another variable called town.

``` r
get_town_from_address <- function(address) {
  address_tokens <- str_split(address, pattern = ",")[[1]]
  town <- str_trim( address_tokens[length(address_tokens)]  )
  return(town)
}

ireland_houses_cleaned$town <- ireland_houses_cleaned$address %>% 
  lapply(get_town_from_address) %>%
  unlist
```

## Write Clean Dataset to Disk

Finally, after doing some initial data exploration and cleaning, we can
proceed to start analyzing the variance and covariance of the variables
in our dataset, thus diving a little deeper into our analysis.

``` r
dataset_filename <- paste(dataset_directory, "ireland_houses_cleaned.csv", sep="")
write.csv(ireland_houses_cleaned, dataset_filename, row.names = FALSE)
```
