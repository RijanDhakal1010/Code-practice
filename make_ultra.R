# these are the libraries you will need to get this task done, I am unfortunately not sure what version of these libs you should use. I am writing this script in july 2020 and they  are currently working.

library(phytools) # not quite sure what this one does
library(phangorn) # not quite sure what this does
library(glue) # we will need it to make Rland fstrings for IO

# this is where we will read in the old files, with a loop. I have read that loops in Rlang are not that effiecient but as of right now I am not quite sure how else to do this.

# get a list of files, and loop through the files and convest them into their ultrametric versions one at a time.
# the path flag is set to "." to get it work in the current folder, need to change it to argparse based interactive use sometime later.
# The pattern is there to make sure we don't read in files we don't need to. The pattern is set to find ".tree" files for now, I wil change it to interactive use with arparse later.
# the all.files is set to false because we do not want to work with hidden files
# not sure what the full.names flag does, but it works for now ...

# this generate the list of files that we want to convert, look above for explanation for the flags.

list_of_files <- list.files(path=".", pattern = "([^\\s]+(\\.(?i)(tree))$)", all.files= FALSE, full.names=FALSE)

# this is a function to make them ultrametric and we will supply this function with old trees as input.

force.ultrametric<-function(tree,method=c("nnls","extend")){
    method<-method[1]
    if(method=="nnls") tree<-nnls.tree(cophenetic(tree),tree,
        rooted=TRUE,trace=0)
    else if(method=="extend"){
        h<-diag(vcv(tree))
        d<-max(h)-h
        ii<-sapply(1:Ntip(tree),function(x,y) which(y==x),
            y=tree$edge[,2])
        tree$edge.length[ii]<-tree$edge.length[ii]+d
    } else 
        cat("method not recognized: returning input tree\n\n")
    tree
}

# now let us loop through them.

for(i in list_of_files){
	old_tree = read.newick(file = i,text) # here you read in the old_tree
	# now we send the old tree to the function that forces them to become ultrametric
	new_and_better_ultra_tree = force.ultrametric(old_tree)

	# but we also need to make new names for the new trees if we want to loop through a bunch of them. For this we will use Rlang fstring and use the CRAN glue package.
	new_name <- glue('{i}.ultra') # so we take the old name and just add '.ultra' to it.

	write.tree(new_and_better_ultra_tree, file = new_name, append = FALSE, digits = 10, tree.names = FALSE)

}