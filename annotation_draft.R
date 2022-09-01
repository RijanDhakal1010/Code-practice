library(ggtree)

p <- read.tree("tree_maybe.tre")

data_file <- read.table(file = 'Base_clade_results.txt', sep = '\t', header = TRUE)

data_file <- data_file[sample(1:217,217),]

row.names(data_file) <- NULL

print(data_file) 

p <- p %<+% data_file + geom_text + geom_tippoint() + geom_text(aes(color=place, label=value), hjust=1, vjust=1.4, size=3)

print(tree)