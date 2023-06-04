import os
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

def create_network():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch, link=TCLink)
    
    # Create switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    # Create hosts
    h1 = net.addHost('h1', mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', mac='00:00:00:00:00:02')
    h3 = net.addHost('h3', mac='00:00:00:00:00:03')
    h4 = net.addHost('h4', mac='00:00:00:00:00:04')
    h5 = net.addHost('h5', mac='00:00:00:00:00:05')
    h6 = net.addHost('h6', mac='00:00:00:00:00:06')
    server = net.addHost('server', mac='00:00:00:00:00:07')
    udp = net.addHost('udp', mac='00:00:00:00:00:08')

    # Create links
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(h5, s3)
    net.addLink(h6, s3)
    net.addLink(server, s4)
    net.addLink(udp, s4)

    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s4)
    net.addLink(s4, s1)

    # Start network
    net.build()
    net.start()

    # Configure VLANs
    s1.cmd('ovs-vsctl set port s1-eth1 tag=100')
    s1.cmd('ovs-vsctl set port s1-eth2 tag=100')
    s2.cmd('ovs-vsctl set port s2-eth1 tag=100')
    s2.cmd('ovs-vsctl set port s2-eth2 tag=100')
    s3.cmd('ovs-vsctl set port s3-eth1 tag=200')
    s3.cmd('ovs-vsctl set port s3-eth2 tag=200')

    # Run ONOS commands
    onos = net.get('server')
    onos.cmd('onos netcfg localhost /path/to/network-cfg.json')

    # Run CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
