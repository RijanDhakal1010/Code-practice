library(ggplot2)
library(ggtree)

x <- read.tree("raw_data/tree.txt")
info <- read.csv("raw_data/counts.csv",sep = '\t',header=TRUE)

p <- ggtree(x) %<+% info + xlim(-.1, 5)

p2 <- p + geom_tiplab(offset = 0.2) + geom_tippoint(aes(caption = Increase)) + theme_tree2()+geom_tiplab(align=TRUE, linesize=.5)+ xlim(0,25)

ggsave("test_2.pdf", width = 60, height = 80, units = "cm", limitsize = FALSE)

print(p2)

?geom_tippoint
