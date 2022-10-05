#!/bin/bash
nohup python3 -u $HOME/aws-parallelcluster-monitoring/run-simulation-scripts/local_http_server.py >> $HOME/local_server_output.log &
