library(readr)
delfi_data <- read_delim("~/RSTUDIO/delfiout.csv", 
                       "\t", trim_ws = TRUE)

# Load
library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

library(stringr)
library(anytime)


subset_of_text <- subset(delfi_data, !is.na(text))
subset_of_text$word_count <- str_count(delfi_data$text, '\\w+')

delfi_data$word_count <- str_count(delfi_data$text, '\\w+')
delfi_data$word_count



wordcloud(words = subset_of_text$text, min.freq = 50,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))


library(ggplot2)

ggplot(aes(x = time), data = delfi_data) +
  geom_histogram()

ggplot(aes(x = time, y = word_count), data = subset(delfi_data, !is.na(time))) +
  geom_point()
