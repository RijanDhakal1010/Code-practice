library(tidyverse)
library(ggtree)
tree <- read.tree("raw_data/tree.txt")

dd <- read_tsv("raw_data/counts.csv")
row.names(dd) <- NULL

tree <- tree %<+% dd + geom_tiplab(aes()) +geom_tippoint(aes(size=Increase), alpha=0.25)
