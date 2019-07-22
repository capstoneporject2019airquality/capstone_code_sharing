# script to munge .txt of testing data to make suitable for modeling: one target var, eight predictor vars
# author: uak211


library(tidyverse)
library(lubridate)

# read in raw file
# swap spaces of any length for '=' separator to deal with wonky spacing issue
test.data <- read.delim("Test Data - SLC.txt", header = FALSE, skip = 1) %>%
   mutate(V1 = gsub("\\s+", "=", V1))

# all data is now in a single column as one big blob of text
test <- test.data %>%
   mutate(date = gsub("=.*", "", V1), # extracts first element
          station_id = sapply(strsplit(V1, "="), "[", 2), # splits on separator and takes second element
          V1 = ifelse(grepl("OBDII|Idle|Opacity|Waiver", V1), # removes variables already parsed
                      gsub("^.*(?=(OBDII|Idle|Opacity|Waiver))", "", V1, perl = TRUE),
                      gsub("^.*(?=NULL)", "", V1, perl = TRUE)),
          test_type = sapply(strsplit(V1, "="), "[", 1), # splits on separator and takes second element
          test_result = ifelse(grepl("Opacity|Waiver|NULL", test_type), sapply(strsplit(V1, "="), "[", 2),
                                               sapply(strsplit(V1, "="), "[", 3)), # some test types have two-part names, others one
          V1 = ifelse(grepl("Opacity|Waiver|NULL", test_type),
                       gsub("^(.*?=){2}", "", V1),
                       gsub("^(.*?=){3}", "", V1)),
          vin = sapply(strsplit(V1, "="), "[", 1),
          model_year = sapply(strsplit(V1, "="), "[", 2),
          vehicle_type = ifelse(grepl("Passenger", V1), # passenger car has two-part name, others just one
                                paste(sapply(strsplit(V1, "="), "[", 3),
                                      sapply(strsplit(V1, "="), "[", 4), sep = " "),
                                sapply(strsplit(V1, "="), "[", 3)),
          vehicle_class = ifelse(grepl("Passenger", V1), sapply(strsplit(V1, "="), "[", 5),
                                 sapply(strsplit(V1, "="), "[", 4)),
          gross_vehicle_weight_rating = ifelse(grepl("Passenger", V1),
                                               sapply(strsplit(V1, "="), "[", 6),
                                 sapply(strsplit(V1, "="), "[", 5))) %>%
   select(-V1) %>% # remove remaining text blob
   slice(1: n()-1) %>% # do not want last row
   mutate(gross_vehicle_weight_rating = # some vehicle class NAs put weight column data in wrong spot
             ifelse(is.na(gross_vehicle_weight_rating), vehicle_class, gross_vehicle_weight_rating),
          vehicle_class = ifelse(grepl("\\d{2,}", vehicle_class), "NULL", vehicle_class))

# export to flat file
write.csv(test, "test_data_clean.csv")
