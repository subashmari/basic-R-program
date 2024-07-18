# install.packages('ggplot2')
# install.packages('dplyr')
library(ggplot2)
library(dplyr)

data <- as.data.frame(diamonds)

print("Attributes in diamonds dataset:")
print(colnames(data))

print("Attributes taken are cut and color")

print("Categories of cut:")
print(unique(data$cut))

print("Categories of color:")
print(unique(data$color))

print("Frequency Table of Cut and Color:")
data_freq <- diamonds %>% 
  group_by(cut, color) %>% 
  summarise(n = n())
print(data_freq)

print("Probability Table of Cut and Color:")
data_prop <- data_freq %>% 
  ungroup() %>% 
  mutate(prop = n / sum(n))
print(data_prop)

print("Cut and Color of diamond having the highest probability = ")
print(data_prop[data_prop$prop == max(data_prop$prop),])

print("Cut and Color of diamond having the lowest probability = ")
print(data_prop[data_prop$prop == min(data_prop$prop),])

color <- readline(prompt = "Enter color of diamond: ")
cut <- readline(prompt = "Enter cut of diamond: ")

cat("P(color =", color, ") and cut =", cut, ") = ")
print(data_prop[(data_prop$color == color) & (data_prop$cut == cut),])
