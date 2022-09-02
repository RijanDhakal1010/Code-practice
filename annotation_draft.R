library(ggtree)

p <- read.tree("tree_maybe.tre")

data_file <- read.table(file = 'Base_clade_results.txt', sep = '\t', header = TRUE)

p = ggtree(p, branch.length = 'none') %<+%  data_file

p + theme_tree2()+geom_tiplab(align=TRUE, linesize=.5)+ xlim(0,25)

p +  geom_text(aes(label=Increase), hjust=1, vjust=1.4, size=3)

p + theme_tree2()+geom_tiplab(align=TRUE, linesize=.5)+ xlim(0,25) +  geom_text(aes(label=Increase), hjust=1, vjust=1.4, size=3)

ggsave("numbers_hopefully.pdf" , width= 60, height = 80, units = "cm", limitsize = FALSE)
