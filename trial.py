from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_network():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    # Create access points as switches
    ap1 = net.addSwitch('ap1')
    ap2 = net.addSwitch('ap2')
    ap3 = net.addSwitch('ap3')
    ap4 = net.addSwitch('ap4')

    # Create links
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)

    # Start network
    net.build()
    net.start()

    # Run CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
