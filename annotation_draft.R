library(ggtree)

p <- read.tree("tree_maybe.tre")

data_file <- read.table(file = 'Base_clade_results.txt', sep = '\t', header = TRUE)

p = ggtree(p) %<+%  data_file

#ggtree(p,branch.length = 'none') + theme_tree2()+geom_tiplab(align=TRUE, linesize=.5)+ xlim(0,25)

#p + geom_text(aes(label=Increase), hjust=1, vjust=1.4, size=3)

p + geom_text(aes(label=Taxa), hjust=1, vjust=-0.4, size=3) + geom_text(aes(label=Increase), hjust=1, vjust=1.4, size=3)

print(p)
