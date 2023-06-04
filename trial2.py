from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, Host

def create_network():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch, host=Host)

    # Create hosts
    ap1 = net.addHost('ap1', ip='192.168.0.1')
    ap2 = net.addHost('ap2', ip='192.168.0.2')
    ap3 = net.addHost('ap3', ip='192.168.0.3')
    ap4 = net.addHost('ap4', ip='192.168.0.4')
    sta1 = net.addHost('sta1', ip='192.168.1.1')
    sta2 = net.addHost('sta2', ip='192.168.1.2')
    sta3 = net.addHost('sta3', ip='192.168.1.3')
    sta4 = net.addHost('sta4', ip='192.168.1.4')

    # Create switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    # Create links
    net.addLink(ap1, s1)
    net.addLink(ap2, s2)
    net.addLink(ap3, s3)
    net.addLink(ap4, s4)
    net.addLink(sta1, s1)
    net.addLink(sta2, s2)
    net.addLink(sta3, s3)
    net.addLink(sta4, s4)
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s4)

    # Start network
    net.build()
    net.start()

    # Run CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    create_network()
