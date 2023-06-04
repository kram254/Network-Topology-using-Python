from mininet.net import Mininet
from mininet.node import Controller, AccessPoint
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_network():
    net = Mininet(controller=Controller, accessPoint=AccessPoint)

    # Create access points
    ap1 = net.addAccessPoint('ap1', ssid='AP1_SSID', mode='g', channel='1', position='10,20,0')
    ap2 = net.addAccessPoint('ap2', ssid='AP2_SSID', mode='g', channel='1', position='30,20,0')
    ap3 = net.addAccessPoint('ap3', ssid='AP3_SSID', mode='g', channel='1', position='10,40,0')
    ap4 = net.addAccessPoint('ap4', ssid='AP4_SSID', mode='g', channel='1', position='30,40,0')

    # Create stations
    sta4refad = net.addStation('sta4refad', ip='192.168.1.4', position='40,0,0')
    sta5refad = net.addStation('sta5refad', ip='192.168.1.5', position='40,10,0')
    sta6refad = net.addStation('sta6refad', ip='192.168.1.6', position='40,20,0')
    h1 = net.addHost('h1', ip='192.168.1.7')
    h3 = net.addHost('h3', ip='192.168.1.8')

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

    net.addLink(sta4refad, s1)
    net.addLink(sta5refad, s2)
    net.addLink(sta6refad, s3)
    net.addLink(h1, s4)
    net.addLink(h3, s4)

    # Start network
    net.build()
    net.start()

    # Configure traffic
    sta5refad.cmd('iperf -s -p 2214 &')
    sta6refad.cmd('iperf -c 192.168.1.5 -p 2214 &')
    h1.cmd('vlc -vvv https://herts365-my.sharepoint.com/:v:/g/personal/wf17aae_herts_ac_uk/EcknDw6ylkFJgeldS0QqZUIBYgWRzWdc9Vplwt9pdw8F1Q?e=1bvEPZ &')
    h3.cmd('vlc -vvv udp://@192.168.1.4:1234 &')

    # Run CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
