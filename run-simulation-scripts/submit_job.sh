#!/bin/bash

# run Kundur's case
#ANDES_PATH=$(python3 -m site --user-site)
#sudo python3 -m andes run $temppath/andes/cases/kundur/kundur_full.xlsx
# alternatively, run
#python3 -m andes run $HOME/.local/lib/python3.7/site-packages/andes/cases/kundur/kundur_full.xlsx
#CASENAME=$1_full.xlsx
#echo $CASENAME
#sudo python3 -m andes run /root/.local/lib/python3.7/site-packages/andes/cases/$1/$CASENAME -r tds

. /etc/parallelcluster/cfnconfig
USER_HOME="/home/${cfn_cluster_user}"
case_selection=$1
fault_bus_number=$2
fault_clearing_time=$3
sudo python3 $USER_HOME/aws-parallelcluster-monitoring/run-simulation-scripts/run_tds.py $case_selection $fault_bus_number $fault_clearing_time
