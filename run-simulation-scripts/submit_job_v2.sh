#!/bin/bash

# Usage: run Kundur's case
# alternatively, run command
# andes run kundur_full.xlsx -r tds

case_selection=$1
element_number=$2
event_time=$3
python3 ../run_tds_v2.py $case_selection $element_number $event_time
