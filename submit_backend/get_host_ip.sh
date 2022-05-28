# /bin/sh
ip route show | grep 'default' | awk '{print $3}'
