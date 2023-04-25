Ireland Housing - Model Selection
================
Marcos Cavalcante
2023-04-26

- <a href="#model-selection" id="toc-model-selection">Model Selection</a>
  - <a href="#installing-libraries" id="toc-installing-libraries">Installing
    Libraries</a>
  - <a href="#load-dataset" id="toc-load-dataset">Load dataset</a>
  - <a href="#split-dataset" id="toc-split-dataset">Split dataset</a>
- <a href="#generalized-linear-models"
  id="toc-generalized-linear-models">Generalized Linear Models</a>
  - <a href="#linear-regression-model"
    id="toc-linear-regression-model">Linear Regression Model</a>
    - <a href="#stepwise-procedure" id="toc-stepwise-procedure">Stepwise
      Procedure</a>
    - <a href="#anderson-darling-normality-test-for-testing-residual-error"
      id="toc-anderson-darling-normality-test-for-testing-residual-error">Anderson
      Darling normality test for testing residual error</a>
    - <a href="#plotting-the-residual-errors"
      id="toc-plotting-the-residual-errors">Plotting the Residual Errors</a>
    - <a href="#box-cox-transformation"
      id="toc-box-cox-transformation">Box-Cox transformation</a>
    - <a href="#box-cox-with-stepwise" id="toc-box-cox-with-stepwise">Box-Cox
      with Stepwise</a>
    - <a href="#final-anderson-darling-test"
      id="toc-final-anderson-darling-test">Final Anderson Darling test</a>
- <a href="#regression-trees-and-ensemble-methods"
  id="toc-regression-trees-and-ensemble-methods">Regression Trees and
  Ensemble Methods</a>
  - <a href="#regression-trees" id="toc-regression-trees">Regression
    Trees</a>
    - <a href="#building-the-first-regression-tree"
      id="toc-building-the-first-regression-tree">Building the first
      regression tree</a>
    - <a href="#visualising-the-tree"
      id="toc-visualising-the-tree">Visualising the tree</a>
    - <a href="#grid-search" id="toc-grid-search">Grid Search</a>
    - <a href="#find-the-best-hyperparameters"
      id="toc-find-the-best-hyperparameters">Find the best Hyperparameters</a>
    - <a href="#prediction" id="toc-prediction">Prediction</a>
    - <a href="#plot-of-the-tuned-tree" id="toc-plot-of-the-tuned-tree">Plot
      of the tuned tree</a>
    - <a href="#variable-importance" id="toc-variable-importance">Variable
      Importance</a>
  - <a href="#random-forest" id="toc-random-forest">Random Forest</a>
    - <a href="#training-of-the-random-forest"
      id="toc-training-of-the-random-forest">Training of the Random Forest</a>
    - <a href="#grid-search-and-finding-hyperparameters"
      id="toc-grid-search-and-finding-hyperparameters">Grid Search and Finding
      Hyperparameters</a>
    - <a href="#tuned-random-forest-prediction"
      id="toc-tuned-random-forest-prediction">Tuned Random Forest
      Prediction</a>
    - <a href="#random-frest-variable-importance"
      id="toc-random-frest-variable-importance">Random Frest Variable
      Importance</a>
  - <a href="#extreme-gradient-boosting"
    id="toc-extreme-gradient-boosting">eXtreme Gradient Boosting</a>
    - <a href="#convert-datasets-to-xgboost-data-type"
      id="toc-convert-datasets-to-xgboost-data-type">Convert datasets to
      xgboost data type</a>
    - <a href="#naive-extreme-gradient-boosting"
      id="toc-naive-extreme-gradient-boosting">Naive eXtreme Gradient
      Boosting</a>
    - <a href="#naive-implementation---error-versus-number-of-trees"
      id="toc-naive-implementation---error-versus-number-of-trees">Naive
      Implementation - Error versus Number of trees</a>
    - <a href="#tuning" id="toc-tuning">Tuning</a>
    - <a href="#training-tuned-model" id="toc-training-tuned-model">Training
      tuned model</a>
    - <a href="#predicting" id="toc-predicting">Predicting</a>
- <a href="#testing-all-models-on-testing-dataset"
  id="toc-testing-all-models-on-testing-dataset">Testing all models on
  testing dataset</a>
  - <a href="#regression-tree" id="toc-regression-tree">Regression tree</a>
  - <a href="#random-forest-1" id="toc-random-forest-1">Random Forest</a>
  - <a href="#extreme-gradient-boosting-1"
    id="toc-extreme-gradient-boosting-1">Extreme Gradient Boosting</a>

# Model Selection

This project will use supervised machine learning algorithms to solve a
regression problem. The goal is to understand whether socioeconomic
variables along with house characteristics can improve the accuracy of
house valuation predictions. The machine learning algorithms that will
be used are generalized linear models (*linear regression*), *regression
trees*, *random forests* and, *extreme gradient boosting*.

In this study, to train tree and ensemble based models, **grid search**
is going to be used to find the *hyperparameters* that yield the best
result, **cross-validation** (*10-fold*) is also used when training the
model.

## Installing Libraries

First step is to install and load the necessary libraries.

``` r
packages <- c("tidyverse", "dplyr", "ggplot2", "corrplot", "knitr", "vip",
              "ranger", "randomForest", "caret", "rpart", "rpart.plot", "splines", 
              "gtools", "Rmisc", "scales", "viridis", "caret",  "gridExtra",
              "AMR", "kableExtra", "rattle", "forecast", "plotly", "reshape2",
              "nortest", "rgl", "car", "olsrr", "jtools", "MASS", "xgboost", "lime")

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
```

## Load dataset

``` r
dataset_directory <- "../../datasets/"
dataset_filename <- paste(dataset_directory, "ireland_houses_explored.Rda", 
                          sep="")
options(scipen = 999) # turn off scientific notation

load(file = dataset_filename) # loads ireland_houses dataframe
```

## Split dataset

Let us start by splitting the dataset into: *training*, *validation* and
*testing* sets. Those sets of the main dataset are going to be used for
different purposes:

1.  **training_set**: This dataset is only used for training the model
    that we are about to create.
2.  **validation_set**: The validation dataset is used for validating
    the hyperparameters used in the ML model on unseen/untrained data.
3.  **testing_set**: The testing dataset is the most pristine set as it
    is used for evaluating the model’s performance on completely unseen
    data. This is the last step in the model selection and it must not
    be used during the training or validation stages.

``` r
SEED_VALUE <- 2360873

# To allow reproducibility of the results
set.seed(SEED_VALUE)

# Data split is done accordingly: training (70%), validation (15%), and testing (15%) datasets.
sets <- sample(1:3,
          size = nrow(ireland_houses), 
          replace = TRUE,
          prob = c(0.70, 0.15, 0.15)) # Probability of being 1 is 70%, 2 is 15% and 3 is 15%

training_set <- ireland_houses[sets==1, ] # 70% of the observations
validation_set <- ireland_houses[sets==2, ] # 15% of the observations
testing_set <- ireland_houses[sets==3, ] # 15% of the observations
```

# Generalized Linear Models

## Linear Regression Model

The *linear regression* model will be the first one to be trained. To do
that, we will make use of the following variables in the dataset:
**price** as the target variable and we will use every other variable in
the dataset as the predictors. Please note that factor variables have
been transformed into dummy variables in the EDA notebook and that
character variables have been removed, there are only *numeric* and
*factor* variables in this dataset.

``` r
linear_model <- lm( formula = price ~ ., 
                     data = training_set )

summary(linear_model)
```

    ## 
    ## Call:
    ## lm(formula = price ~ ., data = training_set)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -978372  -38445    7039   43694 1024463 
    ## 
    ## Coefficients:
    ##                             Estimate  Std. Error t value             Pr(>|t|)
    ## (Intercept)              -672704.353  683021.752  -0.985             0.324714
    ## size                        2576.695      35.982  71.611 < 0.0000000000000002
    ## bedrooms                    8577.116    2210.082   3.881             0.000105
    ## bathrooms                   3984.151    2055.724   1.938             0.052659
    ## latitude                    5998.847   12569.781   0.477             0.633205
    ## longitude                   2981.649    7039.533   0.424             0.671903
    ## pricePerSqMeter              135.111       1.539  87.773 < 0.0000000000000002
    ## nearestHospitals           14070.627    3032.767   4.640       0.000003563383
    ## nearestGardaStations       -2268.892     802.088  -2.829             0.004688
    ## nearestEducationCentres     -161.141      81.929  -1.967             0.049247
    ## nearestPublicTransports      -39.739      20.876  -1.904             0.057012
    ## propertyTypeApartment    -100223.133    7559.031 -13.259 < 0.0000000000000002
    ## propertyTypeBungalow      -40792.815   14416.663  -2.830             0.004676
    ## propertyTypeDuplex        -26101.958   19722.071  -1.323             0.185721
    ## propertyTypeEndOfTerrace    6996.988    7474.893   0.936             0.349276
    ## propertyTypeSemiD          12358.155    4791.204   2.579             0.009922
    ## propertyTypeTerrace         1165.922    5762.343   0.202             0.839662
    ## propertyTypeTownhouse     -24317.789   13695.092  -1.776             0.075838
    ## countyCarlow               -2169.696   24869.347  -0.087             0.930481
    ## countyCavan               -61238.580   18621.147  -3.289             0.001012
    ## countyClare               -42854.530   23347.880  -1.835             0.066482
    ## countyCork                 -4164.224   23402.185  -0.178             0.858775
    ## countyDonegal             -70417.780   26689.047  -2.638             0.008349
    ## countyGalway              -31958.982   19931.881  -1.603             0.108895
    ## countyKerry               -46714.917   28075.841  -1.664             0.096186
    ## countyKildare             -25780.980   11257.288  -2.290             0.022045
    ## countyKilkenny            -35738.461   18225.835  -1.961             0.049939
    ## countyLaois               -34154.773   19484.317  -1.753             0.079662
    ## countyLeitrim             -47919.651   25280.791  -1.895             0.058073
    ## countyLimerick            -30079.208   20992.704  -1.433             0.151953
    ## countyLongford            -43484.217   23241.560  -1.871             0.061396
    ## countyLouth               -31802.787   16256.312  -1.956             0.050470
    ## countyMayo                -44222.576   24448.155  -1.809             0.070525
    ## countyMeath               -34320.607   11532.556  -2.976             0.002932
    ## countyMonaghan            -52611.073   29245.875  -1.799             0.072079
    ## countyOffaly              -35689.657   22233.047  -1.605             0.108489
    ## countyRoscommon           -33356.520   19330.722  -1.726             0.084474
    ## countySligo               -25080.481   25873.079  -0.969             0.332400
    ## countyTipperary           -25138.672   18368.856  -1.369             0.171190
    ## countyWaterford           -18952.889   20444.656  -0.927             0.353945
    ## countyWestmeath           -57767.105   21468.994  -2.691             0.007149
    ## countyWexford             -38661.330   15929.730  -2.427             0.015253
    ## countyWicklow             -18714.984   12448.583  -1.503             0.132791
    ## berRating                  82298.141   13402.602   6.140       0.000000000874
    ## berRatingA1                38592.275   66306.428   0.582             0.560568
    ## berRatingA2                61152.838   15457.914   3.956       0.000077033694
    ## berRatingA3                21104.928   13155.740   1.604             0.108712
    ## berRatingB1                 -946.328   18584.849  -0.051             0.959391
    ## berRatingB2               -16033.832   10016.546  -1.601             0.109486
    ## berRatingB3                 2562.938    7555.972   0.339             0.734475
    ## berRatingC1                 7185.734    6626.076   1.084             0.278202
    ## berRatingC2                 7231.333    6601.341   1.095             0.273369
    ## berRatingD1                 1673.000    6808.781   0.246             0.805913
    ## berRatingD2                 5256.302    7100.301   0.740             0.459150
    ## berRatingE1               -11231.394    8196.909  -1.370             0.170674
    ## berRatingE2                -3063.855    9128.195  -0.336             0.737148
    ## berRatingF                 -6156.505    8773.246  -0.702             0.482870
    ## berRatingG                 14888.427    8133.391   1.831             0.067218
    ## berRatingSi666             45739.471   10239.451   4.467       0.000008073158
    ##                             
    ## (Intercept)                 
    ## size                     ***
    ## bedrooms                 ***
    ## bathrooms                .  
    ## latitude                    
    ## longitude                   
    ## pricePerSqMeter          ***
    ## nearestHospitals         ***
    ## nearestGardaStations     ** 
    ## nearestEducationCentres  *  
    ## nearestPublicTransports  .  
    ## propertyTypeApartment    ***
    ## propertyTypeBungalow     ** 
    ## propertyTypeDuplex          
    ## propertyTypeEndOfTerrace    
    ## propertyTypeSemiD        ** 
    ## propertyTypeTerrace         
    ## propertyTypeTownhouse    .  
    ## countyCarlow                
    ## countyCavan              ** 
    ## countyClare              .  
    ## countyCork                  
    ## countyDonegal            ** 
    ## countyGalway                
    ## countyKerry              .  
    ## countyKildare            *  
    ## countyKilkenny           *  
    ## countyLaois              .  
    ## countyLeitrim            .  
    ## countyLimerick              
    ## countyLongford           .  
    ## countyLouth              .  
    ## countyMayo               .  
    ## countyMeath              ** 
    ## countyMonaghan           .  
    ## countyOffaly                
    ## countyRoscommon          .  
    ## countySligo                 
    ## countyTipperary             
    ## countyWaterford             
    ## countyWestmeath          ** 
    ## countyWexford            *  
    ## countyWicklow               
    ## berRating                ***
    ## berRatingA1                 
    ## berRatingA2              ***
    ## berRatingA3                 
    ## berRatingB1                 
    ## berRatingB2                 
    ## berRatingB3                 
    ## berRatingC1                 
    ## berRatingC2                 
    ## berRatingD1                 
    ## berRatingD2                 
    ## berRatingE1                 
    ## berRatingE2                 
    ## berRatingF                  
    ## berRatingG               .  
    ## berRatingSi666           ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 129100 on 6229 degrees of freedom
    ## Multiple R-squared:  0.8243, Adjusted R-squared:  0.8227 
    ## F-statistic: 503.9 on 58 and 6229 DF,  p-value: < 0.00000000000000022

From the output of the linear model above, it is possible to see that
the R-squared value is *0.8243* and the adjusted R-squared is *0.8227*.

The intercept point is at *0.041* and it is also quite clear that many
of the *county*, *berRating* dummy variables will likely be removed
during the **stepwise** procedure. Similarly, it is also clear that
*latitude* and *longitude* may also be removed.

### Stepwise Procedure

``` r
linear_model_stepwise <- step(linear_model, k = 3.841459, trace = 0)
summary( linear_model_stepwise )
```

    ## 
    ## Call:
    ## lm(formula = price ~ size + bedrooms + bathrooms + pricePerSqMeter + 
    ##     nearestHospitals + nearestEducationCentres + nearestPublicTransports + 
    ##     propertyTypeApartment + propertyTypeBungalow + propertyTypeSemiD + 
    ##     countyDonegal + countyKerry + berRating + berRatingA2 + berRatingB2 + 
    ##     berRatingE1 + berRatingSi666, data = training_set)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -980752  -34642    8098   41679 1025053 
    ## 
    ## Coefficients:
    ##                            Estimate  Std. Error t value             Pr(>|t|)
    ## (Intercept)             -411619.526    7091.867 -58.041 < 0.0000000000000002
    ## size                       2577.537      34.513  74.682 < 0.0000000000000002
    ## bedrooms                   8233.995    2173.113   3.789             0.000153
    ## bathrooms                  4113.343    1931.472   2.130             0.033240
    ## pricePerSqMeter             138.443       1.361 101.753 < 0.0000000000000002
    ## nearestHospitals          10471.787    2558.634   4.093       0.000043168483
    ## nearestEducationCentres    -221.477      68.583  -3.229             0.001247
    ## nearestPublicTransports     -41.166      15.731  -2.617             0.008896
    ## propertyTypeApartment    -95086.435    6242.340 -15.232 < 0.0000000000000002
    ## propertyTypeBungalow     -34145.273   14100.797  -2.422             0.015484
    ## propertyTypeSemiD         13787.224    4000.261   3.447             0.000571
    ## countyDonegal            -31519.034   10490.227  -3.005             0.002670
    ## countyKerry              -29350.126   10199.658  -2.878             0.004021
    ## berRating                 79758.180   12626.166   6.317       0.000000000285
    ## berRatingA2               55984.727   14852.406   3.769             0.000165
    ## berRatingB2              -21284.763    9008.445  -2.363             0.018170
    ## berRatingE1              -14904.699    6917.239  -2.155             0.031222
    ## berRatingSi666            40891.456    9230.989   4.430       0.000009592290
    ##                            
    ## (Intercept)             ***
    ## size                    ***
    ## bedrooms                ***
    ## bathrooms               *  
    ## pricePerSqMeter         ***
    ## nearestHospitals        ***
    ## nearestEducationCentres ** 
    ## nearestPublicTransports ** 
    ## propertyTypeApartment   ***
    ## propertyTypeBungalow    *  
    ## propertyTypeSemiD       ***
    ## countyDonegal           ** 
    ## countyKerry             ** 
    ## berRating               ***
    ## berRatingA2             ***
    ## berRatingB2             *  
    ## berRatingE1             *  
    ## berRatingSi666          ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 129300 on 6270 degrees of freedom
    ## Multiple R-squared:  0.8225, Adjusted R-squared:  0.822 
    ## F-statistic:  1709 on 17 and 6270 DF,  p-value: < 0.00000000000000022

As expected, many of the *county*, *berRating* dummy variables and,
*latitude*, *longitude* also got removed. The **R-squared** and
**Adjusted R-squared** values marginally changed after applying
stepwise.

| Model                 | R-squared | Adjusted R-sqaured |
|-----------------------|-----------|--------------------|
| linear model          | 0.8243    | 0.8227             |
| linear model stepwise | 0.8225    | 0.822              |

### Anderson Darling normality test for testing residual error

The *Anderson Darling* test for residual normality was used instead of
the well known *Shapiro-Francia* as Anderson Darling can handle datasets
with over 5,000 observations.

It can be interpreted in the same manner as Shapiro-Francia, where:

- **H0**: The null hypothesis says that if the *p-value* is greater than
  0.05, the residual errors follow a normal distribution.

- **H1**: The alternative hypothesis says if the *p-value* is lesser
  than 0.05, the residual errors do not follow a normal distribution.

``` r
ad.test(linear_model_stepwise$residuals)
```

    ## 
    ##  Anderson-Darling normality test
    ## 
    ## data:  linear_model_stepwise$residuals
    ## A = 350.04, p-value < 0.00000000000000022

As per the p-value above, it is possible to see that the residual errors
do not follow a normal distribution and the *alternative hypothesis*
will be taken. It is possible however, to use the *Box-Cox*
transformation on the target variable to try improve the normality of
the resiudals so good predictions using the linear model can be made.

### Plotting the Residual Errors

Plot of the residual errors.

``` r
# Adding Normal curve to compare the distribution
training_set %>%
  mutate(residuals = linear_model_stepwise$residuals) %>%
  ggplot(aes(x = residuals)) +
  geom_histogram(aes(y = after_stat(density)), 
                 color = "white", 
                 fill = "#55C667FF", 
                 bins = 20,
                 alpha = 0.6) +
  stat_function(fun = dnorm, 
                args = list(mean = mean(linear_model_stepwise$residuals),
                            sd = sd(linear_model_stepwise$residuals)),
                linewidth = 2, color = "grey30") +
  scale_color_manual(values = "grey50") +
  labs(x = "Residuals",
       y = "Frequency") +
  theme_bw()
```

![](ModelSelection-HousingDataset_files/figure-gfm/Plotting%20the%20residuals-1.png)<!-- -->

### Box-Cox transformation

Let us now run the **Box-Cox** transformation on the *price* variable.

``` r
housing_box_cox <- powerTransform(training_set$price)
housing_box_cox
```

    ## Estimated transformation parameter 
    ## training_set$price 
    ##         -0.1280778

``` r
#Creating a box-cox field in the dataset to estimate new model
bc_price <- (((training_set$price ^ housing_box_cox$lambda) - 1) / 
                            housing_box_cox$lambda)

linear_model_box_cox <- lm( formula = bc_price ~ . - price, 
                             data = training_set )

summary(linear_model_box_cox)
```

    ## 
    ## Call:
    ## lm(formula = bc_price ~ . - price, data = training_set)
    ## 
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max 
    ## -0.35462 -0.01712  0.00411  0.02332  0.14543 
    ## 
    ## Coefficients:
    ##                               Estimate    Std. Error t value
    ## (Intercept)               7.3981500120  0.2169273902  34.104
    ## size                      0.0007466234  0.0000114279  65.334
    ## bedrooms                  0.0096264529  0.0007019210  13.714
    ## bathrooms                 0.0032140303  0.0006528970   4.923
    ## latitude                 -0.0244468233  0.0039921564  -6.124
    ## longitude                 0.0102055550  0.0022357525   4.565
    ## pricePerSqMeter           0.0000442775  0.0000004889  90.568
    ## nearestHospitals          0.0060540965  0.0009632054   6.285
    ## nearestGardaStations     -0.0000266205  0.0002547428  -0.104
    ## nearestEducationCentres   0.0000260860  0.0000260207   1.003
    ## nearestPublicTransports  -0.0000206933  0.0000066303  -3.121
    ## propertyTypeApartment    -0.0631001908  0.0024007447 -26.284
    ## propertyTypeBungalow     -0.0227383625  0.0045787255  -4.966
    ## propertyTypeDuplex       -0.0286104633  0.0062637206  -4.568
    ## propertyTypeEndOfTerrace -0.0240191556  0.0023740226 -10.117
    ## propertyTypeSemiD        -0.0132167375  0.0015216843  -8.686
    ## propertyTypeTerrace      -0.0319764802  0.0018301173 -17.472
    ## propertyTypeTownhouse    -0.0357553583  0.0043495549  -8.220
    ## countyCarlow             -0.0376468866  0.0078984932  -4.766
    ## countyCavan              -0.0374681733  0.0059140677  -6.335
    ## countyClare              -0.0183528308  0.0074152758  -2.475
    ## countyCork               -0.0275109867  0.0074325232  -3.701
    ## countyDonegal            -0.0000477531  0.0084764290  -0.006
    ## countyGalway              0.0009567000  0.0063303562   0.151
    ## countyKerry              -0.0322537036  0.0089168740  -3.617
    ## countyKildare            -0.0056280333  0.0035753095  -1.574
    ## countyKilkenny           -0.0372682278  0.0057885166  -6.438
    ## countyLaois              -0.0345042845  0.0061882100  -5.576
    ## countyLeitrim            -0.0351913727  0.0080291673  -4.383
    ## countyLimerick           -0.0314396792  0.0066672732  -4.716
    ## countyLongford           -0.0442271311  0.0073815086  -5.992
    ## countyLouth              -0.0043661415  0.0051629970  -0.846
    ## countyMayo               -0.0169289185  0.0077647227  -2.180
    ## countyMeath               0.0026173372  0.0036627345   0.715
    ## countyMonaghan           -0.0343505914  0.0092884764  -3.698
    ## countyOffaly             -0.0230335401  0.0070612053  -3.262
    ## countyRoscommon          -0.0373779505  0.0061394282  -6.088
    ## countySligo              -0.0103618113  0.0082172777  -1.261
    ## countyTipperary          -0.0504363768  0.0058339400  -8.645
    ## countyWaterford          -0.0419378569  0.0064932133  -6.459
    ## countyWestmeath          -0.0183505391  0.0068185424  -2.691
    ## countyWexford            -0.0489869351  0.0050592749  -9.683
    ## countyWicklow            -0.0075453618  0.0039536641  -1.908
    ## berRating                -0.0225673963  0.0042566602  -5.302
    ## berRatingA1               0.0495676647  0.0210588907   2.354
    ## berRatingA2               0.0206521211  0.0049094262   4.207
    ## berRatingA3               0.0165490724  0.0041782571   3.961
    ## berRatingB1               0.0074572965  0.0059025394   1.263
    ## berRatingB2               0.0087854979  0.0031812502   2.762
    ## berRatingB3               0.0126032555  0.0023997733   5.252
    ## berRatingC1               0.0067146383  0.0021044387   3.191
    ## berRatingC2               0.0044806760  0.0020965827   2.137
    ## berRatingD1              -0.0010144064  0.0021624656  -0.469
    ## berRatingD2              -0.0054792423  0.0022550522  -2.430
    ## berRatingE1              -0.0110196831  0.0026033345  -4.233
    ## berRatingE2              -0.0198212258  0.0028991104  -6.837
    ## berRatingF               -0.0245639344  0.0027863787  -8.816
    ## berRatingG               -0.0377232087  0.0025831613 -14.604
    ## berRatingSi666           -0.0453482691  0.0032520448 -13.945
    ##                                      Pr(>|t|)    
    ## (Intercept)              < 0.0000000000000002 ***
    ## size                     < 0.0000000000000002 ***
    ## bedrooms                 < 0.0000000000000002 ***
    ## bathrooms                0.000000875460373658 ***
    ## latitude                 0.000000000969927204 ***
    ## longitude                0.000005098011165973 ***
    ## pricePerSqMeter          < 0.0000000000000002 ***
    ## nearestHospitals         0.000000000349229159 ***
    ## nearestGardaStations                 0.916776    
    ## nearestEducationCentres              0.316136    
    ## nearestPublicTransports              0.001810 ** 
    ## propertyTypeApartment    < 0.0000000000000002 ***
    ## propertyTypeBungalow     0.000000701362685562 ***
    ## propertyTypeDuplex       0.000005027285278603 ***
    ## propertyTypeEndOfTerrace < 0.0000000000000002 ***
    ## propertyTypeSemiD        < 0.0000000000000002 ***
    ## propertyTypeTerrace      < 0.0000000000000002 ***
    ## propertyTypeTownhouse    0.000000000000000244 ***
    ## countyCarlow             0.000001918648112235 ***
    ## countyCavan              0.000000000253219832 ***
    ## countyClare                          0.013350 *  
    ## countyCork                           0.000216 ***
    ## countyDonegal                        0.995505    
    ## countyGalway                         0.879879    
    ## countyKerry                          0.000300 ***
    ## countyKildare                        0.115506    
    ## countyKilkenny           0.000000000129827835 ***
    ## countyLaois              0.000000025672322235 ***
    ## countyLeitrim            0.000011901063922516 ***
    ## countyLimerick           0.000002463426205725 ***
    ## countyLongford           0.000000002193806232 ***
    ## countyLouth                          0.397775    
    ## countyMayo                           0.029277 *  
    ## countyMeath                          0.474892    
    ## countyMonaghan                       0.000219 ***
    ## countyOffaly                         0.001112 ** 
    ## countyRoscommon          0.000000001210027957 ***
    ## countySligo                          0.207364    
    ## countyTipperary          < 0.0000000000000002 ***
    ## countyWaterford          0.000000000113568777 ***
    ## countyWestmeath                      0.007137 ** 
    ## countyWexford            < 0.0000000000000002 ***
    ## countyWicklow                        0.056379 .  
    ## berRating                0.000000118698561069 ***
    ## berRatingA1                          0.018615 *  
    ## berRatingA2              0.000026284873161405 ***
    ## berRatingA3              0.000075544993331300 ***
    ## berRatingB1                          0.206491    
    ## berRatingB2                          0.005768 ** 
    ## berRatingB3              0.000000155570112861 ***
    ## berRatingC1                          0.001426 ** 
    ## berRatingC2                          0.032626 *  
    ## berRatingD1                          0.639017    
    ## berRatingD2                          0.015137 *  
    ## berRatingE1              0.000023400105762747 ***
    ## berRatingE2              0.000000000008856826 ***
    ## berRatingF               < 0.0000000000000002 ***
    ## berRatingG               < 0.0000000000000002 ***
    ## berRatingSi666           < 0.0000000000000002 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 0.04099 on 6229 degrees of freedom
    ## Multiple R-squared:  0.8722, Adjusted R-squared:  0.871 
    ## F-statistic: 732.9 on 58 and 6229 DF,  p-value: < 0.00000000000000022

From the results, it can be seen that the lambda parameter value is
-0.1280778. And that many predictors do no meet the *p-value* criteria.
Nevertheless, the R-squared and Adjusted R-Squared increased
considerably.

| Model                 | R-squared | Adjusted R-sqaured |
|-----------------------|-----------|--------------------|
| linear model          | 0.8243    | 0.8227             |
| linear model stepwise | 0.8225    | 0.822              |
| linear model box-cox  | 0.8722    | 0.871              |

### Box-Cox with Stepwise

Let us apply again the stewise method, but this time on the model using
box-cox.

``` r
linear_model_box_cox_stepwise <- step(linear_model_box_cox, k = 3.841459, trace = 0)
summary(linear_model_box_cox_stepwise)
```

    ## 
    ## Call:
    ## lm(formula = bc_price ~ size + bedrooms + bathrooms + latitude + 
    ##     longitude + pricePerSqMeter + nearestHospitals + nearestPublicTransports + 
    ##     propertyTypeApartment + propertyTypeBungalow + propertyTypeDuplex + 
    ##     propertyTypeEndOfTerrace + propertyTypeSemiD + propertyTypeTerrace + 
    ##     propertyTypeTownhouse + countyCarlow + countyCavan + countyClare + 
    ##     countyCork + countyKerry + countyKilkenny + countyLaois + 
    ##     countyLeitrim + countyLimerick + countyLongford + countyMayo + 
    ##     countyMonaghan + countyOffaly + countyRoscommon + countySligo + 
    ##     countyTipperary + countyWaterford + countyWestmeath + countyWexford + 
    ##     berRating + berRatingA1 + berRatingA2 + berRatingA3 + berRatingB2 + 
    ##     berRatingB3 + berRatingC1 + berRatingC2 + berRatingD2 + berRatingE1 + 
    ##     berRatingE2 + berRatingF + berRatingG + berRatingSi666, data = training_set)
    ## 
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max 
    ## -0.35425 -0.01752  0.00414  0.02358  0.14671 
    ## 
    ## Coefficients:
    ##                              Estimate   Std. Error t value             Pr(>|t|)
    ## (Intercept)               7.301412171  0.097453168  74.922 < 0.0000000000000002
    ## size                      0.000746700  0.000011386  65.583 < 0.0000000000000002
    ## bedrooms                  0.009614912  0.000700188  13.732 < 0.0000000000000002
    ## bathrooms                 0.003288042  0.000649828   5.060 0.000000431562581911
    ## latitude                 -0.022825544  0.001817286 -12.560 < 0.0000000000000002
    ## longitude                 0.009092178  0.000874925  10.392 < 0.0000000000000002
    ## pricePerSqMeter           0.000044351  0.000000475  93.364 < 0.0000000000000002
    ## nearestHospitals          0.006000957  0.000773834   7.755 0.000000000000010264
    ## nearestPublicTransports  -0.000015596  0.000002710  -5.754 0.000000009119522637
    ## propertyTypeApartment    -0.062603082  0.002358765 -26.541 < 0.0000000000000002
    ## propertyTypeBungalow     -0.022215589  0.004551519  -4.881 0.000001082191345710
    ## propertyTypeDuplex       -0.027439687  0.006204003  -4.423 0.000009903848464124
    ## propertyTypeEndOfTerrace -0.023851244  0.002360372 -10.105 < 0.0000000000000002
    ## propertyTypeSemiD        -0.013243757  0.001511877  -8.760 < 0.0000000000000002
    ## propertyTypeTerrace      -0.031947802  0.001819959 -17.554 < 0.0000000000000002
    ## propertyTypeTownhouse    -0.035726322  0.004345664  -8.221 0.000000000000000243
    ## countyCarlow             -0.034288767  0.007372874  -4.651 0.000003376863798618
    ## countyCavan              -0.036222987  0.004722481  -7.670 0.000000000000019783
    ## countyClare              -0.017874451  0.004364105  -4.096 0.000042605696030430
    ## countyCork               -0.024988454  0.003760303  -6.645 0.000000000032815166
    ## countyKerry              -0.031385534  0.004828874  -6.500 0.000000000086791306
    ## countyKilkenny           -0.034232857  0.004553918  -7.517 0.000000000000063821
    ## countyLaois              -0.032266146  0.005441904  -5.929 0.000000003206970172
    ## countyLeitrim            -0.035621676  0.005943105  -5.994 0.000000002164678881
    ## countyLimerick           -0.030181564  0.003890394  -7.758 0.000000000000010016
    ## countyLongford           -0.043379428  0.006251505  -6.939 0.000000000004346601
    ## countyMayo               -0.018297463  0.003511364  -5.211 0.000000193931364595
    ## countyMonaghan           -0.033377124  0.008526034  -3.915 0.000091469491925345
    ## countyOffaly             -0.021400970  0.006393370  -3.347             0.000821
    ## countyRoscommon          -0.037461701  0.003909037  -9.583 < 0.0000000000000002
    ## countySligo              -0.011562268  0.005271544  -2.193             0.028320
    ## countyTipperary          -0.048360113  0.004112309 -11.760 < 0.0000000000000002
    ## countyWaterford          -0.038515319  0.004493529  -8.571 < 0.0000000000000002
    ## countyWestmeath          -0.016995763  0.005994890  -2.835             0.004597
    ## countyWexford            -0.044993026  0.003359646 -13.392 < 0.0000000000000002
    ## berRating                -0.022116059  0.004127903  -5.358 0.000000087307088493
    ## berRatingA1               0.049344936  0.021029941   2.346             0.018986
    ## berRatingA2               0.020567747  0.004798462   4.286 0.000018439094077318
    ## berRatingA3               0.016971301  0.004049512   4.191 0.000028162644131581
    ## berRatingB2               0.008768996  0.003014523   2.909             0.003640
    ## berRatingB3               0.012562468  0.002172702   5.782 0.000000007741065615
    ## berRatingC1               0.006832030  0.001844510   3.704             0.000214
    ## berRatingC2               0.004634656  0.001837084   2.523             0.011666
    ## berRatingD2              -0.005422564  0.001999207  -2.712             0.006699
    ## berRatingE1              -0.010876229  0.002383648  -4.563 0.000005143018630067
    ## berRatingE2              -0.019582355  0.002701416  -7.249 0.000000000000470916
    ## berRatingF               -0.024386433  0.002576555  -9.465 < 0.0000000000000002
    ## berRatingG               -0.037580306  0.002354995 -15.958 < 0.0000000000000002
    ## berRatingSi666           -0.045287419  0.003077048 -14.718 < 0.0000000000000002
    ##                             
    ## (Intercept)              ***
    ## size                     ***
    ## bedrooms                 ***
    ## bathrooms                ***
    ## latitude                 ***
    ## longitude                ***
    ## pricePerSqMeter          ***
    ## nearestHospitals         ***
    ## nearestPublicTransports  ***
    ## propertyTypeApartment    ***
    ## propertyTypeBungalow     ***
    ## propertyTypeDuplex       ***
    ## propertyTypeEndOfTerrace ***
    ## propertyTypeSemiD        ***
    ## propertyTypeTerrace      ***
    ## propertyTypeTownhouse    ***
    ## countyCarlow             ***
    ## countyCavan              ***
    ## countyClare              ***
    ## countyCork               ***
    ## countyKerry              ***
    ## countyKilkenny           ***
    ## countyLaois              ***
    ## countyLeitrim            ***
    ## countyLimerick           ***
    ## countyLongford           ***
    ## countyMayo               ***
    ## countyMonaghan           ***
    ## countyOffaly             ***
    ## countyRoscommon          ***
    ## countySligo              *  
    ## countyTipperary          ***
    ## countyWaterford          ***
    ## countyWestmeath          ** 
    ## countyWexford            ***
    ## berRating                ***
    ## berRatingA1              *  
    ## berRatingA2              ***
    ## berRatingA3              ***
    ## berRatingB2              ** 
    ## berRatingB3              ***
    ## berRatingC1              ***
    ## berRatingC2              *  
    ## berRatingD2              ** 
    ## berRatingE1              ***
    ## berRatingE2              ***
    ## berRatingF               ***
    ## berRatingG               ***
    ## berRatingSi666           ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 0.04099 on 6239 degrees of freedom
    ## Multiple R-squared:  0.872,  Adjusted R-squared:  0.871 
    ## F-statistic: 885.2 on 48 and 6239 DF,  p-value: < 0.00000000000000022

It looks like after applying the *stepwise* procedure on the *box-cox*
model the **R-squared** and **Adjusted R-squared** had no noticeable
improvement from the *box-cox* only model.

| Model                         | R-squared | Adjusted R-sqaured |
|-------------------------------|-----------|--------------------|
| linear model                  | 0.8243    | 0.8227             |
| linear model stepwise         | 0.8225    | 0.822              |
| linear model box-cox          | 0.8722    | 0.871              |
| linear model box-cox stepwise | 0.872     | 0.871              |

### Final Anderson Darling test

``` r
ad.test(linear_model_box_cox_stepwise$residuals)
```

    ## 
    ##  Anderson-Darling normality test
    ## 
    ## data:  linear_model_box_cox_stepwise$residuals
    ## A = 101.27, p-value < 0.00000000000000022

As seen above, the null hypothesis will be accepted and the model cannot
be used because it does not have a normal residual error distribution.

The result above tells that there might be some issues, such as
**heteroskedasticity** or simply that there is no normal distribution.

From the Exploratory Data Analysis step, it was seen that the house
prices are not normally distributed and, rather, they are skewed to the
right, meaning that most of the houses are valued lower than the
average.

Potentially, a Gamma Generalized Linear Model may be a better fit as
Gamma GLMs build better models when the data is continuous, positive and
skewed as it can capture non-linear relationships.

# Regression Trees and Ensemble Methods

## Regression Trees

Regression Trees can be good to model complicated data that does not
have any apparent structure. Regression trees are also easy to visualise
(when not deep) and provide good insights into the splits done by the
tree during its decision process.

In regression trees, the decision about splitting across nodes is taken
based on the Residual Sum of Square (RSS), many splits are computed and
the one that minimizes RSS is chosen.

### Building the first regression tree

``` r
tree_house_naive <- rpart(
  formula = price ~ .,
  data    = training_set,
  method  = "anova"
)


# Let's see what was used in the tree splits
tree_house_naive
```

    ## n= 6288 
    ## 
    ## node), split, n, deviance, yval
    ##       * denotes terminal node
    ## 
    ##  1) root 6288 590566200000000  420555.3  
    ##    2) pricePerSqMeter< 4812.665 5090 215391700000000  351329.7  
    ##      4) size< 190.5 4130  64405310000000  296541.0  
    ##        8) pricePerSqMeter< 2456.005 1730  10220680000000  216493.4 *
    ##        9) pricePerSqMeter>=2456.005 2400  35108890000000  354242.0  
    ##         18) size< 120.5 1724  10727580000000  303810.7 *
    ##         19) size>=120.5 676   8814430000000  482856.7 *
    ##      5) size>=190.5 960  85254220000000  587035.0  
    ##       10) pricePerSqMeter< 2503.685 672  23638590000000  462535.9  
    ##         20) size< 419 621  12951600000000  432427.7 *
    ##         21) size>=419 51   3269464000000  829147.1 *
    ##       11) pricePerSqMeter>=2503.685 288  26895550000000  877533.0  
    ##         22) size< 339.5 254   8185070000000  795687.0 *
    ##         23) size>=339.5 34   4297889000000 1488971.0 *
    ##    3) pricePerSqMeter>=4812.665 1198 247145800000000  714677.6  
    ##      6) size< 167 1004  51630660000000  556383.3  
    ##       12) size< 99.5 623   8883155000000  422470.4 *
    ##       13) size>=99.5 381  13307260000000  775353.7  
    ##         26) pricePerSqMeter< 6760.415 290   3800271000000  704592.2 *
    ##         27) pricePerSqMeter>=6760.415 91   3427387000000 1000857.0 *
    ##      7) size>=167 194  40162160000000 1533891.0  
    ##       14) size< 269.5 151  17136240000000 1373112.0  
    ##         28) pricePerSqMeter< 7589.515 117   5170025000000 1242521.0 *
    ##         29) pricePerSqMeter>=7589.515 34   3104612000000 1822500.0 *
    ##       15) size>=269.5 43   5415477000000 2098488.0 *

### Visualising the tree

``` r
viridis_palette = scales::viridis_pal(begin=.75, end=1)(20)
rpart.plot(tree_house_naive, box.palette = viridis_palette)
```

![](ModelSelection-HousingDataset_files/figure-gfm/Visualising%20the%20tree-1.png)<!-- -->

``` r
plotcp(tree_house_naive)
```

![](ModelSelection-HousingDataset_files/figure-gfm/Visualising%20the%20tree-2.png)<!-- -->

### Grid Search

``` r
tree_grid_search <- expand.grid(
  minsplit = seq(3, 30, 1),
  maxdepth = seq(15, 50, 1)
)


cat("Size of Grid Search", nrow(tree_grid_search))
```

    ## Size of Grid Search 1008

### Find the best Hyperparameters

``` r
hyper_trees <- list()

for (i in 1:nrow(tree_grid_search)) {
  
  minsplit <- tree_grid_search$minsplit[i]
  maxdepth <- tree_grid_search$maxdepth[i]
  
  set.seed(SEED_VALUE) # be able to reproduce
  
  hyper_trees[[i]] <- rpart(
    formula = price ~ .,
    data    = training_set,
    method  = "anova",
    control = list(minsplit = minsplit, 
                   maxdepth = maxdepth)
  )
}
```

``` r
get_cp <- function(tree) {
  min <- which.min(tree$cptable[, "xerror"])
  cp  <- tree$cptable[min, "CP"] 
}

get_min_error <- function(tree) {
  min    <- which.min(tree$cptable[, "xerror"])
  xerror <- tree$cptable[min, "xerror"] 
}

tree_grid_search %>%
  mutate(
    cp    = purrr::map_dbl(hyper_trees, get_cp),
    error = purrr::map_dbl(hyper_trees, get_min_error)
    ) %>%
  arrange(error) %>%
  head(10)
```

    ##    minsplit maxdepth   cp     error
    ## 1         3       15 0.01 0.1713882
    ## 2         4       15 0.01 0.1713882
    ## 3         5       15 0.01 0.1713882
    ## 4         6       15 0.01 0.1713882
    ## 5         7       15 0.01 0.1713882
    ## 6         8       15 0.01 0.1713882
    ## 7         9       15 0.01 0.1713882
    ## 8        10       15 0.01 0.1713882
    ## 9        11       15 0.01 0.1713882
    ## 10       12       15 0.01 0.1713882

### Prediction

``` r
tuned_tree <- rpart(
    formula = price ~ .,
    data    = training_set,
    method  = "anova",
    control = list(minsplit = 3, maxdepth = 15, cp = 0.01)
)

tree_estimated <- predict(tuned_tree, 
                       newdata = validation_set)

calculate_metrics( observed = tree_estimated, 
                   expected = validation_set$price, 
                   training = training_set$price)
```

    ## Root Mean Squared Error (RMSE):  122957.3 
    ## Mean Absolute Error (MAE):  90201.25 
    ## Mean Squared Error (MSE):  15118498751 
    ## Impurity Error:  0.1877301 
    ## Residual Error:  15118498751

### Plot of the tuned tree

``` r
rpart.plot(tuned_tree, box.palette = viridis_palette)
```

![](ModelSelection-HousingDataset_files/figure-gfm/Plot%20of%20the%20tuned%20tree-1.png)<!-- -->

### Variable Importance

``` r
vip::vip(tuned_tree)
```

![](ModelSelection-HousingDataset_files/figure-gfm/Variable%20Importance-1.png)<!-- -->

## Random Forest

### Training of the Random Forest

At this point, the random forest algorithm can start it is training
phase.

``` r
set.seed(SEED_VALUE)

naive_random_forest <- randomForest(
  formula = price ~ .,
  data    = training_set,
  ntree   = 500
)

plot(naive_random_forest)
```

![](ModelSelection-HousingDataset_files/figure-gfm/Random%20Forest%20Naive-1.png)<!-- -->

``` r
cat("Number of trees with lowest MSE error:", which.min(naive_random_forest$mse), "\n")
```

    ## Number of trees with lowest MSE error: 496

``` r
cat("RMSE of the best random forest:", sqrt(naive_random_forest$mse[which.min(naive_random_forest$mse)]), "\n")
```

    ## RMSE of the best random forest: 54958.73

### Grid Search and Finding Hyperparameters

#### Creating Grid

``` r
rf_grid_search <- expand.grid(
  mtry       = seq(5, 57, by = 2),
  node_size  = seq(3, 20, by = 2),
  sampe_size = c(.55, .632, .70, .80),
  OOB_RMSE   = 0
)

cat("Size of Random Forest Grid Search: ", nrow(rf_grid_search))
```

    ## Size of Random Forest Grid Search:  972

#### Performing Random Forest Grid Search

``` r
for(i in 1:nrow(rf_grid_search)) {
  
  model <- ranger(
    formula         = price ~ ., 
    data            = training_set, 
    num.trees       = 1000,
    mtry            = rf_grid_search$mtry[i],
    min.node.size   = rf_grid_search$node_size[i],
    sample.fraction = rf_grid_search$sampe_size[i],
    seed            = SEED_VALUE
  )
  
  # add OOB error to grid
  rf_grid_search$OOB_RMSE[i] <- sqrt(model$prediction.error)
}

rf_grid_search %>% 
  dplyr::arrange(OOB_RMSE) %>%
  head(10)
```

    ##    mtry node_size sampe_size OOB_RMSE
    ## 1    57         3        0.8 23043.45
    ## 2    57         5        0.8 23163.58
    ## 3    57         7        0.8 23440.24
    ## 4    55         3        0.8 23464.69
    ## 5    55         5        0.8 23632.68
    ## 6    53         3        0.8 23840.07
    ## 7    57         3        0.7 23891.60
    ## 8    57         5        0.7 24006.63
    ## 9    57         9        0.8 24012.19
    ## 10   55         7        0.8 24013.61

### Tuned Random Forest Prediction

``` r
tuned_random_forest <- ranger(
  formula   = price ~ ., 
  data      = training_set, 
  num.trees = 1000,
  mtry      = 57,
  min.node.size = 3,
  sample.fraction = .8,
  importance      = 'impurity'
)

random_forest_estimated <- predict(tuned_random_forest, validation_set)
calculate_metrics( observed = random_forest_estimated$predictions, 
                   expected = validation_set$price, 
                   training = training_set$price
)
```

    ## Root Mean Squared Error (RMSE):  11061.66 
    ## Mean Absolute Error (MAE):  4407.45 
    ## Mean Squared Error (MSE):  122360272 
    ## Impurity Error:  0.001519378 
    ## Residual Error:  122360272

### Random Frest Variable Importance

``` r
vip(tuned_random_forest) + ggtitle("ranger: RF")
```

![](ModelSelection-HousingDataset_files/figure-gfm/Random%20Frest%20Variable%20Importance-1.png)<!-- -->

## eXtreme Gradient Boosting

### Convert datasets to xgboost data type

``` r
features <- setdiff(names(training_set), "price")

treatplan <- vtreat::designTreatmentsZ(training_set, features, verbose = FALSE)

vtreat_traininig_predictors <- vtreat::prepare(treatplan, training_set) %>% as.matrix()
vtreat_trainining_target <- training_set$price

vtreat_validation_predictors <- vtreat::prepare(treatplan, validation_set) %>% as.matrix()
vtreat_validation_target <- validation_set$price

vtreat_testing_predictors <- vtreat::prepare(treatplan, testing_set) %>% as.matrix()
vtreat_testing_target <- testing_set$price
```

### Naive eXtreme Gradient Boosting

``` r
set.seed(SEED_VALUE)

naive_xgb <- xgb.cv(
  data = vtreat_traininig_predictors,
  label = vtreat_trainining_target,
  nrounds = 10000,
  nfold = 10,
  objective = "reg:squarederror",
  verbose = 0 
)

naive_xgb$evaluation_log %>%
  dplyr::summarise(
    ntrees.train = which(train_rmse_mean == min(train_rmse_mean))[1],
    rmse.train   = min(train_rmse_mean),
    ntrees.test  = which(test_rmse_mean == min(test_rmse_mean))[1],
    rmse.test   = min(test_rmse_mean),
  )
```

    ##   ntrees.train rmse.train ntrees.test rmse.test
    ## 1         3472  0.2412913        2502  24801.85

### Naive Implementation - Error versus Number of trees

``` r
ggplot(naive_xgb$evaluation_log) +
  geom_line(aes(iter, train_rmse_mean), color = "red") +
  geom_line(aes(iter, test_rmse_mean), color = "blue")
```

![](ModelSelection-HousingDataset_files/figure-gfm/Naive%20Implementation%20-%20Error%20versus%20Number%20of%20trees-1.png)<!-- -->

### Tuning

#### Grid Search Definition

``` r
xgboost_grid <- expand.grid(
  eta = c(.01, .05, .1),
  max_depth = c(3, 5, 7),
  min_child_weight = c(1, 3, 5),
  subsample = c(.65, .8), 
  colsample_bytree = c(.8, .9, 1),
  optimal_trees = 0,               
  min_RMSE = 0  
)

nrow(xgboost_grid)
```

    ## [1] 162

#### Finding Hyperparameters

``` r
for(i in 1:nrow(xgboost_grid)) {
  
  params <- list(
    eta = xgboost_grid$eta[i],
    max_depth = xgboost_grid$max_depth[i],
    min_child_weight = xgboost_grid$min_child_weight[i],
    subsample = xgboost_grid$subsample[i],
    colsample_bytree = xgboost_grid$colsample_bytree[i]
  )
  
  cat("Iteration value:", i, "\n", "Time Started:", format(Sys.time(), "%H:%M:%S"), "\n")
  set.seed(SEED_VALUE)
  
  model <- xgb.cv(
    params = params,
    data = vtreat_traininig_predictors,
    label = vtreat_trainining_target,
    nrounds = 3500,
    nfold = 10,
    objective = "reg:squarederror",
    verbose = 0,               
    early_stopping_rounds = 15 
  )
  
  xgboost_grid$optimal_trees[i] <- which.min(model$evaluation_log$test_rmse_mean)
  xgboost_grid$min_RMSE[i] <- min(model$evaluation_log$test_rmse_mean)
}


xgboost_grid %>%
  arrange(min_RMSE) %>%
  head(10)
```

Hyperparameters can be found below.

|     | eta  | max_depth | min_child_weight | subsample | colsample_bytree | optimal_trees | min_RMSE |
|-----|------|-----------|------------------|-----------|------------------|---------------|----------|
| 1   | 0.05 | 3         | 3                | 0.65      | 1.0              | 2761          | 13991.78 |
| 2   | 0.05 | 3         | 3                | 0.80      | 1.0              | 3338          | 14064.99 |
| 3   | 0.05 | 3         | 1                | 0.80      | 1.0              | 3173          | 14332.72 |
| 4   | 0.05 | 3         | 1                | 0.65      | 1.0              | 2140          | 14404.10 |
| 5   | 0.01 | 5         | 3                | 0.65      | 1.0              | 3497          | 14640.60 |
| 6   | 0.05 | 3         | 5                | 0.80      | 1.0              | 3283          | 14702.79 |
| 7   | 0.05 | 3         | 1                | 0.65      | 0.9              | 2457          | 14943.85 |
| 8   | 0.05 | 3         | 3                | 0.65      | 0.9              | 2102          | 15082.14 |
| 9   | 0.05 | 3         | 1                | 0.80      | 0.9              | 3464          | 15091.21 |
| 10  | 0.05 | 3         | 3                | 0.80      | 0.9              | 2495          | 15215.54 |

### Training tuned model

``` r
# parameter list
params <- list(
  eta = 0.05,
  max_depth = 3,
  min_child_weight = 3,
  subsample = 0.65,
  colsample_bytree = 1
)

set.seed(SEED_VALUE)

tuned_xgb <- xgboost(
  params = params,
  data = vtreat_traininig_predictors,
  label = vtreat_trainining_target,
  nrounds = 2800,
  objective = "reg:squarederror",
  verbose = 0
)
```

#### Visualising Variable Importance

``` r
variable_importance_matrix <- xgb.importance(model = tuned_xgb)
xgb.plot.importance(variable_importance_matrix, top_n = 10, measure = "Gain")
```

![](ModelSelection-HousingDataset_files/figure-gfm/Visualising%20Variable%20Importance-1.png)<!-- -->

#### Explaining variables used with LIME

``` r
local_obs <- vtreat::prepare(treatplan, training_set[10:13,])


# apply LIME
explainer <- lime(data.frame(vtreat_traininig_predictors), tuned_xgb)
explanation <- explain(local_obs, explainer, n_features = 5)
plot_features(explanation)
```

![](ModelSelection-HousingDataset_files/figure-gfm/Explaining%20variables%20used%20with%20LIME-1.png)<!-- -->

### Predicting

``` r
# predict values for test data
pred <- predict(tuned_xgb, vtreat_validation_predictors)



calculate_metrics( observed = pred, 
                   expected = vtreat_validation_target, 
                   training = vtreat_trainining_target
)
```

    ## Root Mean Squared Error (RMSE):  12727.64 
    ## Mean Absolute Error (MAE):  5828.174 
    ## Mean Squared Error (MSE):  161992820 
    ## Impurity Error:  0.002011505 
    ## Residual Error:  161992820

# Testing all models on testing dataset

## Regression tree

``` r
tree_estimated <- predict(tuned_tree, 
                       newdata = testing_set)

calculate_metrics( observed = tree_estimated, 
                   expected = testing_set$price, 
                   training = training_set$price)
```

    ## Root Mean Squared Error (RMSE):  131472 
    ## Mean Absolute Error (MAE):  92134.84 
    ## Mean Squared Error (MSE):  17284894411 
    ## Impurity Error:  0.1627699 
    ## Residual Error:  17284894411

## Random Forest

``` r
random_forest_estimated <- predict(tuned_random_forest, testing_set)

calculate_metrics( observed = random_forest_estimated$predictions, 
                   expected = testing_set$price, 
                   training = training_set$price)
```

    ## Root Mean Squared Error (RMSE):  19489.01 
    ## Mean Absolute Error (MAE):  5663.361 
    ## Mean Squared Error (MSE):  379821356 
    ## Impurity Error:  0.003576734 
    ## Residual Error:  379821356

## Extreme Gradient Boosting

``` r
pred <- predict(tuned_xgb, vtreat_testing_predictors)



calculate_metrics( observed = pred, 
                   expected = vtreat_testing_target, 
                   training = vtreat_trainining_target)
```

    ## Root Mean Squared Error (RMSE):  14717.2 
    ## Mean Absolute Error (MAE):  6652.643 
    ## Mean Squared Error (MSE):  216595854 
    ## Impurity Error:  0.002039658 
    ## Residual Error:  216595854
