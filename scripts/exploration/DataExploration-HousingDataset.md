Ireland Housing - Data Exploration
================
Marcos Cavalcante

First step is to install and load the necessary libraries.

``` r
packages <- c("tidyverse","haven", "devtools", "dplyr")

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

## Data Exploration

At this next stage, the dataset will be explored further with regards to
the data values it holds. Exploration around the lower and upper
boundaries of each numeric attribute as well as its histogram
distribution will be done.

Let’s start by using the skim library to have a glimpse of the dataset.

``` r
dataset_directory <- "../../datasets/"
dataset_filename <- paste(dataset_directory, "ireland_houses_filtered.csv", sep="")

ireland_houses <- read.csv(file = dataset_filename ) # Load the dataset

skim(ireland_houses)
```

|                                                  |                |
|:-------------------------------------------------|:---------------|
| Name                                             | ireland_houses |
| Number of rows                                   | 77785          |
| Number of columns                                | 11             |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |                |
| Column type frequency:                           |                |
| character                                        | 5              |
| numeric                                          | 6              |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |                |
| Group variables                                  | None           |

Data summary

**Variable type: character**

| skim_variable | n_missing | complete_rate | min | max | empty | n_unique | whitespace |
|:--------------|----------:|--------------:|----:|----:|------:|---------:|-----------:|
| title         |         0 |             1 |  18 | 102 |     0 |     8806 |          0 |
| propertyType  |         0 |             1 |   6 |  14 |     0 |        8 |          0 |
| ber_rating    |         0 |             1 |   0 |   6 |  2316 |       17 |          0 |
| ber_epi       |         0 |             1 |   0 |  18 | 35101 |     4625 |          0 |
| category      |         0 |             1 |   3 |   9 |     0 |        2 |          0 |

**Variable type: numeric**

| skim_variable       | n_missing | complete_rate |      mean |        sd |       p0 |       p25 |       p50 |       p75 |       p100 | hist  |
|:--------------------|----------:|--------------:|----------:|----------:|---------:|----------:|----------:|----------:|-----------:|:------|
| price               |         0 |             1 | 601026.72 | 656734.92 | 40000.00 | 300000.00 | 415000.00 | 650000.00 |  1.500e+07 | ▇▁▁▁▁ |
| size_meters_squared |         0 |             1 |    130.08 |    161.04 |     1.00 |     75.00 |    102.00 |    144.00 |  6.109e+03 | ▇▁▁▁▁ |
| bedrooms            |         0 |             1 |      3.19 |      1.43 |     1.00 |      2.00 |      3.00 |      4.00 |  3.000e+01 | ▇▁▁▁▁ |
| bathrooms           |         0 |             1 |      2.12 |      1.39 |     1.00 |      1.00 |      2.00 |      3.00 |  2.800e+01 | ▇▁▁▁▁ |
| latitude            |         0 |             1 |     53.19 |      0.50 |    51.44 |     53.29 |     53.33 |     53.36 |  5.538e+01 | ▁▁▇▁▁ |
| longitude           |         0 |             1 |     -6.72 |      0.93 |   -10.35 |     -6.43 |     -6.28 |     -6.25 | -6.010e+00 | ▁▁▁▁▇ |

Glimpse of the dataset without the latitude and longitude attributes:

``` r
skim(ireland_houses) %>%
  filter(!skim_variable %in% c("latitude", "longitude"))
```

|                                                  |                |
|:-------------------------------------------------|:---------------|
| Name                                             | ireland_houses |
| Number of rows                                   | 77785          |
| Number of columns                                | 11             |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |                |
| Column type frequency:                           |                |
| character                                        | 5              |
| numeric                                          | 4              |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |                |
| Group variables                                  | None           |

Data summary

**Variable type: character**

| skim_variable | n_missing | complete_rate | min | max | empty | n_unique | whitespace |
|:--------------|----------:|--------------:|----:|----:|------:|---------:|-----------:|
| title         |         0 |             1 |  18 | 102 |     0 |     8806 |          0 |
| propertyType  |         0 |             1 |   6 |  14 |     0 |        8 |          0 |
| ber_rating    |         0 |             1 |   0 |   6 |  2316 |       17 |          0 |
| ber_epi       |         0 |             1 |   0 |  18 | 35101 |     4625 |          0 |
| category      |         0 |             1 |   3 |   9 |     0 |        2 |          0 |

**Variable type: numeric**

| skim_variable       | n_missing | complete_rate |      mean |        sd |    p0 |    p25 |    p50 |    p75 |     p100 | hist  |
|:--------------------|----------:|--------------:|----------:|----------:|------:|-------:|-------:|-------:|---------:|:------|
| price               |         0 |             1 | 601026.72 | 656734.92 | 40000 | 300000 | 415000 | 650000 | 15000000 | ▇▁▁▁▁ |
| size_meters_squared |         0 |             1 |    130.08 |    161.04 |     1 |     75 |    102 |    144 |     6109 | ▇▁▁▁▁ |
| bedrooms            |         0 |             1 |      3.19 |      1.43 |     1 |      2 |      3 |      4 |       30 | ▇▁▁▁▁ |
| bathrooms           |         0 |             1 |      2.12 |      1.39 |     1 |      1 |      2 |      3 |       28 | ▇▁▁▁▁ |

## Understanding the data

The data already provides really good insights. For example:

-   The mean *price* of houses is €601,026 and the most expensive house
    in the dataset is worth €15 million euro.

-   The mean *size* of a house in $sq^2$ is 130 $sq^2$, and the biggest
    house has 6300 $sq^2$.

-   There appears to be some outliers as well, for instance: house with
    30 bedrooms and 28 bathrooms
