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
    geom_bar(stat = "identity") +
    geom_text(aes(label = total, vjust = -0.25)) +
    scale_x_discrete(labels = c("hate speech", "offensive language", "neither")) +
    xlab("class") +
    ylab("quantity") +
    ggtitle("Number of tweets in each class (data: twitter-hate-speech2.csv)") %>% 
    print()
  
  # Histogram of tweet lengths
  encoded_tweets %>% 
    mutate(tweet_length = nchar(tweet)) %>% 
    ggplot(aes(x = tweet_length)) +
    geom_histogram(binwidth = 1) +
    scale_x_continuous(name = "Number of characters in tweet", 
                       limits = c(0, 300), 
                       expand = c(0, 0)) +
    ylab("Number of tweets") +
    ggtitle("Length of tweets (data: twitter-hate-speech2.csv)") %>% 
    print()
}
