library(readr)
library(dplyr)
library(ggplot2)

# Explore the data in 'twitter-hate-speech2.csv'.

explore <- function() {
  encoded_tweets <- readr::read_csv("./data/twitter-hate-speech2.csv")
  names(encoded_tweets)[1] <- "id"
  
  # Bar chart of the number of tweets in each class
  encoded_tweets %>%
    dplyr::group_by(class) %>%
    dplyr::summarize(total = n()) %>%
    ggplot(aes(x = factor(class), y = total)) +
    geom_bar(stat = "identity", color = "blue", fill = "blue") +
    geom_text(aes(label = total, vjust = -0.25)) +
    scale_x_discrete(labels = c("hate speech", "offensive language", "neither")) +
    xlab("class") +
    ylab("quantity") +
    ggtitle("Number of tweets in each class")
}
