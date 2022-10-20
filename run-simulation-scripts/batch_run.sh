#!/bin/bash

#for i in {1..10}
#do
#   sbatch $USER_HOME/submit_job.sh wecc
#done

. /etc/parallelcluster/cfnconfig
USER_HOME="/home/${cfn_cluster_user}"

for bus in {1..2}
do
    for tc in $(seq 1.1 .01667 1.2)
    do
        if [ "$#" -lt 1 ]
        then
    	    /opt/slurm/bin/sbatch -D $USER_HOME/slurm_workdir/ $USER_HOME/aws-parallelcluster-monitoring/run-simulation-scripts/submit_job.sh 2 $bus $tc
        elif [ "$#" -eq 1 ]
	then
	    /opt/slurm/bin/sbatch -D $USER_HOME/slurm_workdir/ $USER_HOME/aws-parallelcluster-monitoring/run-simulation-scripts/submit_job.sh $1 $bus $tc
	fi
    done
done
