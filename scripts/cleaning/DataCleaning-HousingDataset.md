Ireland Housing - Data Cleaning
================
Marcos Cavalcante

### Installing libraries

First step is to install and load the necessary libraries.

## Import the Ireland Housing dataset

At this step, the Ireland housing dataset will be imported

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

## Further Investigation

From looking at the first 5 observations, it can be noted that some
variables are only used by the property website to manage their
database, some examples are: *id*, *daftShortCode*, *ber_code* and
*url_link*.

Nevertheless, skimming and summarizing the data further will provide
better a better understanding of the variables available.

``` r
summary(ireland_houses)
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
    ##  Length:100294      Length:100294      Length:100294      Min.   :0.000e+00  
    ##  Class :character   Class :character   Class :character   1st Qu.:1.067e+08  
    ##  Mode  :character   Mode  :character   Mode  :character   Median :1.135e+08  
    ##                                                           Mean   :1.133e+08  
    ##                                                           3rd Qu.:1.149e+08  
    ##                                                           Max.   :1.134e+09  
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

``` r
skim(ireland_houses)
```

|                                                  |                |
|:-------------------------------------------------|:---------------|
| Name                                             | ireland_houses |
| Number of rows                                   | 100294         |
| Number of columns                                | 18             |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |                |
| Column type frequency:                           |                |
| character                                        | 11             |
| numeric                                          | 7              |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |                |
| Group variables                                  | None           |

Data summary

**Variable type: character**

| skim_variable | n_missing | complete_rate | min | max | empty | n_unique | whitespace |
|:--------------|----------:|--------------:|----:|----:|------:|---------:|-----------:|
| title         |         0 |             1 |  12 | 105 |     0 |    12362 |          0 |
| price         |         0 |             1 |   7 |  25 |     0 |      705 |          0 |
| propertySize  |         0 |             1 |   0 |  11 | 19734 |      582 |          0 |
| bedrooms      |         0 |             1 |   0 |   9 |   187 |       45 |          0 |
| propertyType  |         0 |             1 |   0 |  14 |    40 |       10 |          0 |
| publishDate   |         0 |             1 |  10 |  10 |     0 |      179 |          0 |
| ber_rating    |         0 |             1 |   0 |   6 |  3919 |       17 |          0 |
| ber_epi       |         0 |             1 |   0 |  18 | 50104 |     5674 |          0 |
| category      |         0 |             1 |   3 |   9 |     0 |        2 |          0 |
| location      |         0 |             1 |   4 |  68 |     0 |      271 |          0 |
| url_link      |         0 |             1 |  62 | 193 |     0 |    12860 |          0 |

**Variable type: numeric**

| skim_variable       | n_missing | complete_rate |          mean |          sd |         p0 |           p25 |           p50 |           p75 |          p100 | hist  |
|:--------------------|----------:|--------------:|--------------:|------------:|-----------:|--------------:|--------------:|--------------:|--------------:|:------|
| id                  |         0 |          1.00 |    3842395.83 |   362289.37 |    6800.00 |    3805133.00 |    3933349.50 |    3974191.00 |    4019790.00 | ▁▁▁▁▇ |
| daftShortcode       |         0 |          1.00 |   28263078.16 | 28413858.53 | 1319566.00 |   18690195.00 |   19258514.00 |   19593376.00 | 113071717\.00 | ▇▁▁▁▁ |
| size_meters_squared |     19967 |          0.80 |        131.94 |      163.58 |       1.00 |         75.00 |        102.00 |        147.00 |       6109.00 | ▇▁▁▁▁ |
| bathrooms           |      1658 |          0.98 |          2.13 |        1.47 |       1.00 |          1.00 |          2.00 |          3.00 |         32.00 | ▇▁▁▁▁ |
| ber_code            |     43417 |          0.57 | 113341265\.10 | 44218210.12 |       0.00 | 106661911\.00 | 113473896\.00 | 114880636\.00 | 1134291201.00 | ▇▁▁▁▁ |
| latitude            |         0 |          1.00 |         53.18 |        0.53 |      51.44 |         53.28 |         53.34 |         53.37 |         55.38 | ▁▁▇▁▁ |
| longitude           |         0 |          1.00 |         -6.82 |        1.01 |     -10.45 |         -6.80 |         -6.28 |         -6.25 |         -6.01 | ▁▁▁▁▇ |

## Removing Variables

After doing some further investigation, it is possible to see that there
are variables with missing data, different data types and format as well
as variables which do not bring any value to our analysis, like it was
said before.

From the statistical summary and data exploration above, it can be seen
that:

-   **id**: ID is a property used within the property website database
    for managing the data.

-   **daftShortcode**: This code is another ID-like property which is
    used for managing data within the property website database.

-   **ber_code**: BER stands for Building Energy Rating and the BER Code
    is simply the ID of the certificate that the house was given.

-   **url_link**: It provides the URL of the house listing and, it
    should be removed as it doesn’t impact the analysis.

-   **publishDate**: This attribute contains information about the date
    of the property listing, and it will not be taken into consideration
    in this study.

-   **location**: It is a useful attribute to be kept, however, this
    information is also present in the title column (which is, in fact,
    the address of the property)

-   **propertySize**: Similar to the *location* attribute,
    *propertySize* is already captured by another attribute:
    *size_meters_squared*.

As a result, The columns mentioned above can be removed as they do not
contribute to this analysis. After removing the unwanted attributes, we
save the resulting dataset in a new variable.

``` r
ireland_houses_cleaned <- ireland_houses %>% 
  select(-c(id, daftShortcode, ber_code, url_link, publishDate, location, propertySize)) 

head(ireland_houses_cleaned, 5)
```

    ##                                       title                price
    ## 1             Drumroe, Ardagh, Co. Longford             295000.0
    ## 2                    Lissardowlan, Longford             595000.0
    ## 3       Cartrongarrow, Ardagh, Co. Longford             130000.0
    ## 4           Cloonfide, Moydow, Co. Longford Price on Application
    ## 5 5 Rath Na Gcarraige, Ardagh, Co. Longford             285000.0
    ##   size_meters_squared bedrooms bathrooms propertyType ber_rating
    ## 1                 273        6         4     Bungalow         B3
    ## 2                 267        4         4     Detached         B3
    ## 3                  NA        2         1     Detached         E2
    ## 4                  NA        1         1     Detached     SI_666
    ## 5                 191        4         3     Detached         B2
    ##            ber_epi latitude longitude category
    ## 1 131.08 kWh/m2/yr 53.68968 -7.684429      Buy
    ## 2 140.49 kWh/m2/yr 53.71720 -7.726544      Buy
    ## 3  108.1 kWh/m2/yr 53.67240 -7.728253      Buy
    ## 4                  53.66372 -7.787243      Buy
    ## 5 114.83 kWh/m2/yr 53.64857 -7.702947      Buy

## Data Transformation - Renaming Variables

It could also be seen that some of the variables did not follow a naming
standard and used an adequate name, for example: *title* actually refers
to the *address* of the house and *size_meters_squared* refers to the
*propertySize*.

The naming convention used across the variables is **camel-case**,
therefore *ber_rating* and *ber_epi* will be renamed to *berRating* and
*berEPI* respectively.

``` r
ireland_houses_renamed <- rename( ireland_houses_cleaned, 
  address = title,
  propertySize = size_meters_squared,
  berRating = ber_rating,
  berEPI = ber_epi
)

skim(ireland_houses_renamed)
```

|                                                  |                        |
|:-------------------------------------------------|:-----------------------|
| Name                                             | ireland_houses_renamed |
| Number of rows                                   | 100294                 |
| Number of columns                                | 11                     |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |                        |
| Column type frequency:                           |                        |
| character                                        | 7                      |
| numeric                                          | 4                      |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |                        |
| Group variables                                  | None                   |

Data summary

**Variable type: character**

| skim_variable | n_missing | complete_rate | min | max | empty | n_unique | whitespace |
|:--------------|----------:|--------------:|----:|----:|------:|---------:|-----------:|
| address       |         0 |             1 |  12 | 105 |     0 |    12362 |          0 |
| price         |         0 |             1 |   7 |  25 |     0 |      705 |          0 |
| bedrooms      |         0 |             1 |   0 |   9 |   187 |       45 |          0 |
| propertyType  |         0 |             1 |   0 |  14 |    40 |       10 |          0 |
| berRating     |         0 |             1 |   0 |   6 |  3919 |       17 |          0 |
| berEPI        |         0 |             1 |   0 |  18 | 50104 |     5674 |          0 |
| category      |         0 |             1 |   3 |   9 |     0 |        2 |          0 |

**Variable type: numeric**

| skim_variable | n_missing | complete_rate |   mean |     sd |     p0 |   p25 |    p50 |    p75 |    p100 | hist  |
|:--------------|----------:|--------------:|-------:|-------:|-------:|------:|-------:|-------:|--------:|:------|
| propertySize  |     19967 |          0.80 | 131.94 | 163.58 |   1.00 | 75.00 | 102.00 | 147.00 | 6109.00 | ▇▁▁▁▁ |
| bathrooms     |      1658 |          0.98 |   2.13 |   1.47 |   1.00 |  1.00 |   2.00 |   3.00 |   32.00 | ▇▁▁▁▁ |
| latitude      |         0 |          1.00 |  53.18 |   0.53 |  51.44 | 53.28 |  53.34 |  53.37 |   55.38 | ▁▁▇▁▁ |
| longitude     |         0 |          1.00 |  -6.82 |   1.01 | -10.45 | -6.80 |  -6.28 |  -6.25 |   -6.01 | ▁▁▁▁▇ |

## Data Transformation - Tidying Data

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
ireland_houses_tidy <- mutate(
  ireland_houses_renamed,
  price = parse_number(price),
  berEPI = as.numeric(str_remove(berEPI, "kWh/m2/yr")),
  bedrooms = as.numeric(bedrooms),
  
  propertyType = as.factor(propertyType),
  category = as.factor(category),
  berRating = as.factor(berRating)
)
```

    ## Warning: 2189 parsing failures.
    ## row col expected               actual
    ##   4  -- a number Price on Application
    ##  14  -- a number Price on Application
    ## 237  -- a number Price on Application
    ## 244  -- a number Price on Application
    ## 245  -- a number Price on Application
    ## ... ... ........ ....................
    ## See problems(...) for more details.

    ## Warning in mask$eval_all_mutate(quo): NAs introduced by coercion

``` r
skim(ireland_houses_tidy)
```

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

    ## Warning in sorted_count(x): Variable contains value(s) of "" that have been
    ## converted to "empty".

|                                                  |                     |
|:-------------------------------------------------|:--------------------|
| Name                                             | ireland_houses_tidy |
| Number of rows                                   | 100294              |
| Number of columns                                | 11                  |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |                     |
| Column type frequency:                           |                     |
| character                                        | 1                   |
| factor                                           | 3                   |
| numeric                                          | 7                   |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |                     |
| Group variables                                  | None                |

Data summary

**Variable type: character**

| skim_variable | n_missing | complete_rate | min | max | empty | n_unique | whitespace |
|:--------------|----------:|--------------:|----:|----:|------:|---------:|-----------:|
| address       |         0 |             1 |  12 | 105 |     0 |    12362 |          0 |

**Variable type: factor**

| skim_variable | n_missing | complete_rate | ordered | n_unique | top_counts                                     |
|:--------------|----------:|--------------:|:--------|---------:|:-----------------------------------------------|
| propertyType  |         0 |             1 | FALSE   |       10 | Ter: 32263, Sem: 22957, Det: 21205, Apa: 13016 |
| berRating     |         0 |             1 | FALSE   |       17 | D1: 10949, D2: 10558, C3: 9662, C2: 8634       |
| category      |         0 |             1 | FALSE   |        2 | Buy: 99251, New: 1043                          |

**Variable type: numeric**

| skim_variable | n_missing | complete_rate |      mean |         sd |       p0 |       p25 |       p50 |       p75 |       p100 | hist  |
|:--------------|----------:|--------------:|----------:|-----------:|---------:|----------:|----------:|----------:|-----------:|:------|
| price         |      2189 |          0.98 | 567082.61 |  622642.94 | 20000.00 | 295000.00 | 395000.00 | 595000.00 |  1.500e+07 | ▇▁▁▁▁ |
| propertySize  |     19967 |          0.80 |    131.94 |     163.58 |     1.00 |     75.00 |    102.00 |    147.00 |  6.109e+03 | ▇▁▁▁▁ |
| bedrooms      |       212 |          1.00 |      3.22 |       1.50 |     1.00 |      2.00 |      3.00 |      4.00 |  4.000e+01 | ▇▁▁▁▁ |
| bathrooms     |      1658 |          0.98 |      2.13 |       1.47 |     1.00 |      1.00 |      2.00 |      3.00 |  3.200e+01 | ▇▁▁▁▁ |
| berEPI        |     50104 |          0.50 |  18282.52 | 1338991.26 |     0.34 |    176.78 |    246.93 |    344.06 |  1.000e+08 | ▇▁▁▁▁ |
| latitude      |         0 |          1.00 |     53.18 |       0.53 |    51.44 |     53.28 |     53.34 |     53.37 |  5.538e+01 | ▁▁▇▁▁ |
| longitude     |         0 |          1.00 |     -6.82 |       1.01 |   -10.45 |     -6.80 |     -6.28 |     -6.25 | -6.010e+00 | ▁▁▁▁▇ |

## Data Cleaning

Once the date types have been sorted, it is possible to see the presence
of missing data in many of the variables in our dataset.

For example, *berEPI* is missing in about *50%* of the observations,
*price* and *bathrooms* are missing in *2%* of the observations,
*propertySize* is missing in *20%* of the observations and there are 212
out of 100.294 observations where number of *bedrooms* is missing.

At this stage, those observations with missing data will be removed
because applying any strategy to replace those missing values may add
bias in our study. Nevertheless, if necessary, this decision will be
revisited in this study to evaluate whether or not having those
observations will help the analysis.

``` r
ireland_houses_cleaned <- ireland_houses_tidy %>%
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

|                                                  |                        |
|:-------------------------------------------------|:-----------------------|
| Name                                             | ireland_houses_cleaned |
| Number of rows                                   | 78034                  |
| Number of columns                                | 11                     |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |                        |
| Column type frequency:                           |                        |
| character                                        | 1                      |
| factor                                           | 3                      |
| numeric                                          | 7                      |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |                        |
| Group variables                                  | None                   |

Data summary

**Variable type: character**

| skim_variable | n_missing | complete_rate | min | max | empty | n_unique | whitespace |
|:--------------|----------:|--------------:|----:|----:|------:|---------:|-----------:|
| address       |         0 |             1 |  18 | 102 |     0 |     8881 |          0 |

**Variable type: factor**

| skim_variable | n_missing | complete_rate | ordered | n_unique | top_counts                                     |
|:--------------|----------:|--------------:|:--------|---------:|:-----------------------------------------------|
| propertyType  |         0 |             1 | FALSE   |        9 | Ter: 26424, Sem: 17710, Det: 15139, Apa: 10459 |
| berRating     |         0 |             1 | FALSE   |       17 | D2: 8555, D1: 8478, C3: 7631, C2: 6936         |
| category      |         0 |             1 | FALSE   |        2 | Buy: 78024, New: 10                            |

**Variable type: numeric**

| skim_variable | n_missing | complete_rate |      mean |        sd |       p0 |       p25 |       p50 |       p75 |       p100 | hist  |
|:--------------|----------:|--------------:|----------:|----------:|---------:|----------:|----------:|----------:|-----------:|:------|
| price         |         0 |          1.00 | 599841.20 | 656064.62 | 40000.00 | 300000.00 | 415000.00 | 650000.00 |  1.500e+07 | ▇▁▁▁▁ |
| propertySize  |         0 |          1.00 |    130.07 |    160.86 |     1.00 |     75.00 |    102.00 |    144.00 |  6.109e+03 | ▇▁▁▁▁ |
| bedrooms      |         0 |          1.00 |      3.19 |      1.43 |     1.00 |      2.00 |      3.00 |      4.00 |  3.000e+01 | ▇▁▁▁▁ |
| bathrooms     |         0 |          1.00 |      2.12 |      1.39 |     1.00 |      1.00 |      2.00 |      3.00 |  2.800e+01 | ▇▁▁▁▁ |
| berEPI        |     35265 |          0.55 |   2692.25 | 483553.68 |     0.34 |    173.71 |    246.86 |    344.67 |  1.000e+08 | ▇▁▁▁▁ |
| latitude      |         0 |          1.00 |     53.19 |      0.50 |    51.44 |     53.29 |     53.33 |     53.36 |  5.538e+01 | ▁▁▇▁▁ |
| longitude     |         0 |          1.00 |     -6.72 |      0.93 |   -10.35 |     -6.43 |     -6.28 |     -6.25 | -6.010e+00 | ▁▁▁▁▇ |

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
