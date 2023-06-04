from mininet.net import Mininet
from mininet.node import Controller, OVSKernelAP
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def create_network():
    net = Mininet(controller=Controller, accessPoint=OVSKernelAP, link=TCLink)

    # Create access points
    ap1 = net.addAccessPoint('ap1', ssid='adhocUH', mode='g', channel='1', position='10,10,0', range=40)
    ap2 = net.addAccessPoint('ap2', ssid='adhocUH', mode='g', channel='1', position='30,10,0', range=40)
    ap3 = net.addAccessPoint('ap3', ssid='adhocUH', mode='g', channel='1', position='20,20,0', range=40)

    # Create stations
    sta4refad = net.addStation('sta4refad', mac='00:00:00:00:11', ip='192.168.1.1', position='5,5,0')
    sta5refad = net.addStation('sta5refad', mac='00:00:00:00:12', ip='192.168.1.2', position='15,15,0')
    sta6refad = net.addStation('sta6refad', mac='00:00:00:00:13', ip='192.168.1.3', position='25,25,0')

    # Create links
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap1, ap3)

    net.addLink(sta4refad, ap1)
    net.addLink(sta5refad, ap2)
    net.addLink(sta6refad, ap3)

    # Start network
    net.build()
    net.start()

    # Ping tests
    print("Ping sta4refad - sta5refad")
    print(sta4refad.cmd('ping -c 5 192.168.1.2'))
    print("Ping sta5refad - sta6refad")
    print(sta5refad.cmd('ping -c 5 192.168.1.3'))
    print("Ping sta4refad - sta6refad")
    print(sta4refad.cmd('ping -c 5 192.168.1.3'))

    # Transfer 100MB in TCP traffic between stations
    print("Transfer 100MB in TCP traffic between sta4refad and sta5refad")
    print(sta4refad.cmd('iperf -s -p 5001 &'))
    print(sta5refad.cmd('iperf -c 192.168.1.1 -p 5001 -t 10 -i 1'))

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
