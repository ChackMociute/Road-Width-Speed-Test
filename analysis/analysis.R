library(lme4) # This is the package that we need for using LMMs


setwd('C:\\Users\\Hackerman\\Desktop\\1.1 Cognitive Psychology and Its Applications\\Intuitive Driving')
data <- read.csv('data.csv')

#data <- data[data$width > 7,]

model <- lmer(
  response ~ lanes + (1|filename) + (1|name) + (1|environment),
  data=data
)

summary(model)
