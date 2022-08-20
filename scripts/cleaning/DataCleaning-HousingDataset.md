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

## Removing Columns

After looking at the first few rows, it is possible to see that there
are columns with missing data, different data types and format as well
as columns which, at first glance, do not bring any value to our
analysis.

However, before starting to remove any data, let’s explore it a little
more by running the summary and skim functions. Those functions will
give an statistical overview of our data.

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

From the information above, it can be seen that:

-   **url_link**: It provides the URL of the house listing and, it
    should be removed as it doesn’t impact the analysis.

-   **ber_code**: BER stands for Building Energy Rating and the BER Code
    is simply the ID of the certificate that the house was given.

-   **id**: ID is a property used within the property website database
    for managing the data.

-   **daftShortcode**: This code is another ID-like property which is
    used for managing data within the property website database.

-   **publishDate**: This attribute contains infnormation about the date
    of the property listing and it will not be taken into consideration
    in this study.

-   **location**: It would be a useful attribute to be kept, however,
    this information is also present in the title column (which is, in
    fact, the address of the property)

-   **propertySize**: Similar to the *location* attribute,
    *propertySize* is already captured by another attribute:
    *size_meters_squared*.

As a result, The columns mentioned above can be removed as they do not
contribute to this analysis. After removing the unwanted attributes, we
save the resulting dataset in a new variable.

``` r
ireland_houses %>% 
  select(-c(url_link, ber_code, id, daftShortcode, publishDate, location, propertySize)) ->
  ireland_houses_cleaned


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

``` r
skim(ireland_houses_cleaned)
```

|                                                  |                        |
|:-------------------------------------------------|:-----------------------|
| Name                                             | ireland_houses_cleaned |
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
| title         |         0 |             1 |  12 | 105 |     0 |    12362 |          0 |
| price         |         0 |             1 |   7 |  25 |     0 |      705 |          0 |
| bedrooms      |         0 |             1 |   0 |   9 |   187 |       45 |          0 |
| propertyType  |         0 |             1 |   0 |  14 |    40 |       10 |          0 |
| ber_rating    |         0 |             1 |   0 |   6 |  3919 |       17 |          0 |
| ber_epi       |         0 |             1 |   0 |  18 | 50104 |     5674 |          0 |
| category      |         0 |             1 |   3 |   9 |     0 |        2 |          0 |

**Variable type: numeric**

| skim_variable       | n_missing | complete_rate |   mean |     sd |     p0 |   p25 |    p50 |    p75 |    p100 | hist  |
|:--------------------|----------:|--------------:|-------:|-------:|-------:|------:|-------:|-------:|--------:|:------|
| size_meters_squared |     19967 |          0.80 | 131.94 | 163.58 |   1.00 | 75.00 | 102.00 | 147.00 | 6109.00 | ▇▁▁▁▁ |
| bathrooms           |      1658 |          0.98 |   2.13 |   1.47 |   1.00 |  1.00 |   2.00 |   3.00 |   32.00 | ▇▁▁▁▁ |
| latitude            |         0 |          1.00 |  53.18 |   0.53 |  51.44 | 53.28 |  53.34 |  53.37 |   55.38 | ▁▁▇▁▁ |
| longitude           |         0 |          1.00 |  -6.82 |   1.01 | -10.45 | -6.80 |  -6.28 |  -6.25 |   -6.01 | ▁▁▁▁▇ |

## Removing rows with missing data

After removing the columns that do not help our study, we can now focus
on removing rows where important data is missing. From the output of the
*skim* method, we can observe that:

-   There are *19967* rows which do not contain information about the
    property size.
-   It is also possible to note that there are *1658* properties which
    do not have a bathroom.

Another peculiar detail is the fact that *bedrooms* and *price* are of
type **character**. But, firstly, let’s proceed to remove the rows with
missing data.

``` r
ireland_houses_size_filtered <- filter(ireland_houses_cleaned, !is.na(size_meters_squared))
ireland_houses_filtered <- filter(ireland_houses_size_filtered, !is.na(bathrooms))
skim(ireland_houses_filtered)
```

|                                                  |                         |
|:-------------------------------------------------|:------------------------|
| Name                                             | ireland_houses_filtered |
| Number of rows                                   | 79123                   |
| Number of columns                                | 11                      |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |                         |
| Column type frequency:                           |                         |
| character                                        | 7                       |
| numeric                                          | 4                       |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |                         |
| Group variables                                  | None                    |

Data summary

**Variable type: character**

| skim_variable | n_missing | complete_rate | min | max | empty | n_unique | whitespace |
|:--------------|----------:|--------------:|----:|----:|------:|---------:|-----------:|
| title         |         0 |             1 |  18 | 102 |     0 |     9159 |          0 |
| price         |         0 |             1 |   7 |  25 |     0 |      579 |          0 |
| bedrooms      |         0 |             1 |   0 |   4 |     7 |       39 |          0 |
| propertyType  |         0 |             1 |   0 |  14 |     6 |        9 |          0 |
| ber_rating    |         0 |             1 |   0 |   6 |  2349 |       17 |          0 |
| ber_epi       |         0 |             1 |   0 |  18 | 35961 |     4733 |          0 |
| category      |         0 |             1 |   3 |   9 |     0 |        2 |          0 |

**Variable type: numeric**

| skim_variable       | n_missing | complete_rate |   mean |     sd |     p0 |   p25 |    p50 |    p75 |    p100 | hist  |
|:--------------------|----------:|--------------:|-------:|-------:|-------:|------:|-------:|-------:|--------:|:------|
| size_meters_squared |         0 |             1 | 131.02 | 160.77 |   1.00 | 75.00 | 102.00 | 145.00 | 6109.00 | ▇▁▁▁▁ |
| bathrooms           |         0 |             1 |   2.13 |   1.40 |   1.00 |  1.00 |   2.00 |   3.00 |   28.00 | ▇▁▁▁▁ |
| latitude            |         0 |             1 |  53.18 |   0.50 |  51.44 | 53.28 |  53.33 |  53.36 |   55.38 | ▁▁▇▁▁ |
| longitude           |         0 |             1 |  -6.74 |   0.95 | -10.35 | -6.46 |  -6.28 |  -6.25 |   -6.01 | ▁▁▁▁▇ |

## Type convertion - Price

Once missing data is removed, we can start looking at converting the
values of *price* and *bedrooms* from character to numeric.

The filtered dataset was further explored in Excel to better understand
why *price* and *bedrooms* are of type character. It could be seen that:

-   *price* was mostly a numeric value, but there are instances where
    the strings: **“Price on Application”**, **“AMV: Price on
    Application”** and **“AMV: ‚Ç¨** appear.

What will be done is the following:

-   rows with **“Price on Application”** and **“AMV: Price on
    Application”** will be attempted to convert to numeric and fail,
    instead the value **“NA”** will be used, which can then be filtered
    out.

-   rows that start with **“AMV: ‚Ç¨** and are followed by the house
    value will be stripped off the initial string and the price will be
    kept. After that, the string value resultant will be converted to
    numeric.

``` r
strip_chars_from_price <- function(house_df) {
  house_df$price <- extract_numeric(house_df$price)
  
  return(house_df)
}

ireland_houses_prices_numeric <- strip_chars_from_price(ireland_houses_filtered)
```

    ## extract_numeric() is deprecated: please use readr::parse_number() instead

``` r
convert_bedrooms_numeric <- function(house_df) {
  house_df$bedrooms <- as.numeric(house_df$bedrooms)
  return(house_df)
}

ireland_houses_filtered <- filter(strip_chars_from_price(ireland_houses_filtered), !is.na(price))
```

    ## extract_numeric() is deprecated: please use readr::parse_number() instead

``` r
ireland_houses_filtered <- filter(convert_bedrooms_numeric(ireland_houses_filtered), !is.na(bedrooms))
ireland_houses_filtered <- filter(ireland_houses_filtered, propertyType!="")

skim(ireland_houses_filtered)
```

|                                                  |                         |
|:-------------------------------------------------|:------------------------|
| Name                                             | ireland_houses_filtered |
| Number of rows                                   | 78028                   |
| Number of columns                                | 11                      |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |                         |
| Column type frequency:                           |                         |
| character                                        | 5                       |
| numeric                                          | 6                       |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |                         |
| Group variables                                  | None                    |

Data summary

**Variable type: character**

| skim_variable | n_missing | complete_rate | min | max | empty | n_unique | whitespace |
|:--------------|----------:|--------------:|----:|----:|------:|---------:|-----------:|
| title         |         0 |             1 |  18 | 102 |     0 |     8879 |          0 |
| propertyType  |         0 |             1 |   6 |  14 |     0 |        8 |          0 |
| ber_rating    |         0 |             1 |   0 |   6 |  2316 |       17 |          0 |
| ber_epi       |         0 |             1 |   0 |  18 | 35259 |     4637 |          0 |
| category      |         0 |             1 |   3 |   9 |     0 |        2 |          0 |

**Variable type: numeric**

| skim_variable       | n_missing | complete_rate |      mean |        sd |       p0 |       p25 |       p50 |       p75 |       p100 | hist  |
|:--------------------|----------:|--------------:|----------:|----------:|---------:|----------:|----------:|----------:|-----------:|:------|
| price               |         0 |             1 | 599857.97 | 656086.50 | 40000.00 | 300000.00 | 415000.00 | 650000.00 |  1.500e+07 | ▇▁▁▁▁ |
| size_meters_squared |         0 |             1 |    130.07 |    160.87 |     1.00 |     75.00 |    102.00 |    144.00 |  6.109e+03 | ▇▁▁▁▁ |
| bedrooms            |         0 |             1 |      3.19 |      1.43 |     1.00 |      2.00 |      3.00 |      4.00 |  3.000e+01 | ▇▁▁▁▁ |
| bathrooms           |         0 |             1 |      2.12 |      1.39 |     1.00 |      1.00 |      2.00 |      3.00 |  2.800e+01 | ▇▁▁▁▁ |
| latitude            |         0 |             1 |     53.19 |      0.50 |    51.44 |     53.29 |     53.33 |     53.36 |  5.538e+01 | ▁▁▇▁▁ |
| longitude           |         0 |             1 |     -6.72 |      0.93 |   -10.35 |     -6.43 |     -6.28 |     -6.25 | -6.010e+00 | ▁▁▁▁▇ |

## Write Clean dataset to file

Finally, the clean dataset can be write back to a CSV file.

``` r
dataset_filename <- paste(dataset_directory, "ireland_houses_filtered.csv", sep="")
write.csv(ireland_houses_filtered, dataset_filename, row.names = FALSE)
```
