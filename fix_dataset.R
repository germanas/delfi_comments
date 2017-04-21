setwd("C:/Users/Germanas/Desktop/Visualisation project/delfi_comments")

library(readr)
my_data <- read_delim("C:/Users/Germanas/Desktop/Visualisation project/delfi_comments/delfiout.csv", 
                       "\t", trim_ws = TRUE)


subset_of_text <- subset(my_data, !is.na(text))
subset_of_text$total_score <- subset_of_text$thumbs_up - subset_of_text$thumbs_down

subset_of_russia <- subset(my_data, country=="LT")
library(plyr)
library(dplyr)
library(ggplot2)
counts <- summarise(group_by(subset_of_text, country),count =n())

normalised <- filter(subset_of_text, country == "LT" | country == "GB" | country == "SE" | country == "IE" | country == "NO")

ggplot(data=normalised, aes(x=time, y=total_score, group=country, colour=country)) +
  geom_smooth() +
  stat_smooth()

write.csv(my_data, file = "clean_data.csv")
