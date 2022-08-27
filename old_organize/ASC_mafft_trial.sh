#!/bin/bash

#source /opt/asn/etc/asn-bash-profiles-special/modules.sh
#module load mafft/7.481_gcc9

for files in Homologs/*
do
	base_name="$(basename $file .fa)"
	new_ext=".afa"
	new_file="$base_name$new_ext"
	mafft $file > $new_file
done
