#!/bin/sh

##Place PBS directives here
#PBS -N IBMAR
#PBS -l nodes=1:ppn=8
#BS -l walltime=168:00:00
#PBS -M jdean2@trinity.edu
#PBS -m ae

##Place Linux commands to run on the remote node here
##

#Find an example located in /data/usr/local/sfw/linux/ibamr/IBAMR/examples
#Copy the example to a folder in your data directory
#Add either the 2d makefile or 3d makefile to the directory
#Place that directory here
cd /data/hnguyenlab/jdean2/IBFE


#Uncomment below if making a 2d simulation  
#make main2d
#/data/usr/local/sfw/linux/openmpi/4.1.0/bin/mpirun -np 8 ./main2d input2d
#set x in '-np x' to correct number of processors (nodes * ppn)

#Uncomment below if making a 3d simulation
#If the input3d file has an exteinsion, such as ".sphere", replace the input3d below with "input3d.sphere"
make -j4 main3d
/data/usr/local/sfw/linux/openmpi/4.1.0/bin/mpirun -np 8 ./main3d input3d
#set x in '-np x' for mpirun to correct number of processors (nodes * ppn)
