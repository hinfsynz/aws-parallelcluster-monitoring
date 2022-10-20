#!/bin/bash
nohup python3 -u ${monitoring_home}/run-simulation-scripts/local_http_server.py >> /tmp/local_server_output.log &
