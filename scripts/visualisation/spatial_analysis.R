packages <- c("tidyverse","sf","tmap","rgdal","rgeos","adehabitatHR","knitr",
              "kableExtra")

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

## Load the data and convert to Simple Feature object

ireland_houses <- read.csv(file = "ireland_houses_filtered.csv" ) # Load the dataset


# Lets create an sf object from our dataset
ireland_houses_sf <- st_as_sf(x = ireland_houses, 
                              coords = c("longitude", "latitude"), 
                              crs = 4326)


## Plotting the data spatially
tmap_mode("view")

tm_shape(shp = ireland_houses_sf) + 
  tm_dots(col = "deepskyblue4", 
          border.col = "black", 
          size = 0.02, 
          alpha = 0.8)


## Loading shapefile with the map of Ireland
shp_ireland <- readOGR("shapefile_ireland", "gadm41_IRL_0")

tm_shape(shp = shp_ireland) + 
  tm_borders()



## Joining the two objects together
tm_shape(shp = shp_ireland) + 
  tm_borders(alpha = 0.5) +
  tm_shape(shp = ireland_houses_sf) + 
  tm_dots(col = "propertyType", 
          size = 0.02)



