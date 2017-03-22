library(readr)
delfi_data <- read_delim("delfiout.csv", 
                       "\t", trim_ws = TRUE)

# Load
library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

library(stringr)
library(anytime)
library(gridExtra)

subset_of_text <- subset(delfi_data, !is.na(text))
subset_of_text$word_count <- str_count(delfi_data$text, '\\w+')

delfi_data$word_count <- str_count(delfi_data$text, '\\w+')
delfi_data$word_count

find_text <- str_count(delfi_data$text, 'kad')
find_text



wordcloud(words = subset_of_text$text, min.freq = 10,
          max.words=1000, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))


subset_of_text$total_score <- subset_of_text$thumbs_up - subset_of_text$thumbs_down


library(ggplot2)

p1 <- ggplot(aes(x = country, y = time), data = subset_of_text) +
  geom_point(aes(size = total_score))+ 
             scale_size_area()

p2 <- ggplot(aes(x = country, y = time), data = subset_of_text) +
  geom_point(aes(size = thumbs_up))+ 
  scale_size_area()

grid.arrange(p1, p2, ncol=2)



ggplot(aes(x = time, y = total_score), data = subset_of_text) +
  geom_point()


library(maps)       # Provides functions that let us plot the maps
library(mapdata)