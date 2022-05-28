import andes
import sys


if len(sys.argv) != 4:
    print('Error: Invalid arguments. Usage:\n\trun_tds.py case_index fault_bus_number fault_clearing_time\n')
    sys.exit(1)

#print(sys.argv[1])

supported_systems = ['placeholder','kundur', 'ieee14', 'wecc']
selection = int(sys.argv[1])
system_to_study = supported_systems[selection]
# only support IEEE14 bus system 
if selection != 2:
    print('Currently only support ieee14 system!') 
    sys.exit(1)

ss = andes.load(andes.get_case('ieee14/ieee14_fault.json'),   # hardcoded for now
                default_config=True, 
                setup=False)

fault_bus_no = int(sys.argv[1])
fault_tc = float(sys.argv[2])

# change the fault bus
ss.Fault.alter('bus',1, fault_bus_no)
# change contingency definition
ss.Fault.alter('tc', 1, fault_tc)
# change output file names
ss.files.txt = 'ieee14_fault_bus{0}_tc{1}_out.txt'.format(fault_bus_no, fault_tc)
ss.files.lst = 'ieee14_fault_bus{0}_tc{1}_out.lst'.format(fault_bus_no, fault_tc)
ss.files.lst = 'ieee14_fault_bus{0}_tc{1}_out.nps'.format(fault_bus_no, fault_tc)
# complete case change
ss.setup()
# solve power flow
ss.PFlow.run()
# run time-domain simulations
ss.TDS.run()

