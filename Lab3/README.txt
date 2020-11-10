README

1. lab3.pdf
	Includes screenshots of command results of pingall, iperf, and dpctl dump-flows for both commands. Pingall fails, but its ARP packets pass. iperf is successful.

2. lab3controller.py
	pox controller that will create rules for an openflow table based off the created firewall that will accept only TCP and ARP protocols. Any packet using any other packet will be dropped. 