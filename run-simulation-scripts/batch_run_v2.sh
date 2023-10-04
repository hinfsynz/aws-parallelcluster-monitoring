#!/bin/bash

#for i in {1..10}
#do
#   sbatch $USER_HOME/submit_job.sh wecc
#done

SCRIPTLOC=$PWD

for element_no in {1..4}
do
    for event_time in $(seq 1.1 .01667 1.2)
    do
        if [ "$#" -lt 1 ]
        then
    	    /opt/slurm/bin/sbatch -D $SCRIPTLOC/slurm_workdir $SCRIPTLOC/submit_job_v2.sh 2 $element_no $event_time
        elif [ "$#" -eq 1 ]
	then
	    /opt/slurm/bin/sbatch -D $SCRIPTLOC/slurm_workdir $SCRIPTLOC/submit_job_v2.sh $1 $element_no $event_time
	fi
    done
done
