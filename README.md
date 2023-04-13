# Ireland Housing Dataset Analysis

In this repository you can find details about a data analysis and machine learning project aimed at investigating
whether or not social economical variables have any influence on the price of houses in Ireland.

The dataset used in this analysis was obtained by webscrapping the Daft.ie website using the well-known python package [daftlistings](https://pypi.org/project/daftlistings/1.1.6/).

The steps followed in this project to do the analysis can be better visualised in the image below.

![](assets/machine-learning-pipeline.png)

For the Data Collection step, you can find further information at:

* [Collect Data](/scripts/collection/)
  * In this folder, the python scripts used for collecting the data are stored, you can follow the instructions defined in the README file to run it.
  
  * One important caveat is the fact that the dataset of house listings is time dependent, which means that houses listed today may not be available anymore tomorrow or in a few months time.

  * In order to address the above, the dataset collected is stored and kept prestine inside the [datasets folder](/datasets/house_listings_all.csv)

* [Data Preparation](/scripts/cleaning/)

    * 