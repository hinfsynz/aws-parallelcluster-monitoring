#!/bin/bash

#for i in {1..10}
#do
#   sbatch $HOME/submit_job.sh wecc
#done

for bus in {1..2}
do
    for tc in $(seq 1.1 .01667 1.2)
    do
        if [ "$#" -lt 1 ]
        then
    	    sbatch -D $HOME/slurm_workdir/ $HOME/submit_job.sh 2 $bus $tc
        elif [ "$#" -eq 1 ]
	then
	    sbatch -D $HOME/slurm_workdir/ $HOME/submit_job.sh $1 $bus $tc
	fi
    done
done
