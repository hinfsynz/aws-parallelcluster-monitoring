#!/bin/bash

. /etc/parallelcluster/cfnconfig
nohup python3 -u /home/${cfn_cluster_user}/${cfn_postinstall_args[1]}/run-simulation-scripts/local_http_server.py >> /tmp/local_server_output.log &
