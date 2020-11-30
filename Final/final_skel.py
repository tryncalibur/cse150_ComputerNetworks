#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class final_topo(Topo):
  def build(self):
    # Host
    h1 = self.addHost('h10',mac='00:00:00:00:00:01',ip='10.1.1.10/24', defaultRoute="h10-eth0")
    h2 = self.addHost('h20',mac='00:00:00:00:00:02',ip='10.1.2.20/24', defaultRoute="h20-eth0")
    h3 = self.addHost('h30',mac='00:00:00:00:00:03',ip='10.1.3.30/24', defaultRoute="h30-eth0")
    h4 = self.addHost('h40',mac='00:00:00:00:00:04',ip='10.1.4.40/24', defaultRoute="h40-eth0")

    h5 = self.addHost('h50',mac='00:00:00:00:00:05',ip='10.2.5.50/24', defaultRoute="h50-eth0")
    h6 = self.addHost('h60',mac='00:00:00:00:00:06',ip='10.2.6.60/24', defaultRoute="h60-eth0")
    h7 = self.addHost('h70',mac='00:00:00:00:00:07',ip='10.2.7.70/24', defaultRoute="h70-eth0")
    h8 = self.addHost('h80',mac='00:00:00:00:00:08',ip='10.2.8.80/24', defaultRoute="h80-eth0")

    hT = self.addHost('h_trust',mac='00:00:00:00:00:09',ip='108.24.31.112/24', defaultRoute="h_trust-eth0")
    hU = self.addHost('h_untrust',mac='00:00:00:00:00:10',ip='106.44.82.103/24', defaultRoute="h_untrust-eth0")

    hS = self.addHost('h_server',mac='00:00:00:00:00:11',ip='10.3.9.90/24', defaultRoute="h_server-eth0")


    # Switches
    core = self.addSwitch('s1')      #1 core
    f1s1 = self.addSwitch('s2')      #2 f1s1
    f1s2 = self.addSwitch('s3')      #3 f1s2
    f2s1 = self.addSwitch('s4')      #4 f2s1
    f2s2 = self.addSwitch('s5')      #5 f2s2
    data = self.addSwitch('s6')      #6 data


    # Switch to Switch Links
    self.addLink(core, data, port1=1, port2=1)
    self.addLink(core, f1s1, port1=2, port2=1)
    self.addLink(core, f1s2, port1=3, port2=1)
    self.addLink(core, f2s1, port1=4, port2=1)
    self.addLink(core, f2s2, port1=5, port2=1)

    # Server Link
    self.addLink(data, hS, port1=2, port2=0)

    # External Host Link
    self.addLink(core, hT, port1=6, port2=0)
    self.addLink(core, hU, port1=7, port2=0)

    # F1 Links
    self.addLink(f1s1, h1, port1=3, port2=0)
    self.addLink(f1s1, h2, port1=4, port2=0)
    
    self.addLink(f1s2, h3, port1=3, port2=0)
    self.addLink(f1s2, h4, port1=4, port2=0)

    # F2 Links
    self.addLink(f2s1, h5, port1=3, port2=0)
    self.addLink(f2s1, h6, port1=4, port2=0)

    self.addLink(f2s2, h7, port1=3, port2=0)
    self.addLink(f2s2, h8, port1=4, port2=0)
    
    



def configure():
  topo = final_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()

  #h1, h2, h3, h4 ,h5, h6, h7, h8, hT, hU, hS = net.get('h1', 'h2', 'h3', 'h4' ,'h5', 'h6', 'h7', 'h8', 'hT', 'hU', 'hS')

  CLI(net)
  
  net.stop()


if __name__ == '__main__':
  configure()
