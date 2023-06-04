from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, UserSwitch, OVSKernelAP
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def create_network():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch, link=TCLink)

    # Create access points
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='AP1_SSID', channel='1')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='AP2_SSID', channel='1')

    # Create stations
    sta1 = net.addStation('sta1', ip='192.168.1.1')
    sta2 = net.addStation('sta2', ip='192.168.1.2')
    sta3 = net.addStation('sta3', ip='192.168.1.3')
    sta4 = net.addStation('sta4', ip='192.168.1.4')
    sta5 = net.addStation('sta5', ip='192.168.1.5')
    sta6 = net.addStation('sta6', ip='192.168.1.6')

    # Create switches
    s1 = net.addSwitch('s1', cls=UserSwitch)
    s2 = net.addSwitch('s2', cls=UserSwitch)

    # Create servers
    server = net.addHost('server', ip='192.168.2.1')
    video_host = net.addHost('video_host', ip='192.168.2.2')

    # Create links
    net.addLink(ap1, s1)
    net.addLink(ap2, s1)
    net.addLink(s1, s2)
    net.addLink(s2, server)
    net.addLink(s2, video_host)

    # Start network
    net.build()
    net.start()

    # Configure TCP flow
    sta5.cmd('iperf -s -p 2214 &')
    sta6.cmd('iperf -c 192.168.1.5 -p 2214 -b 10M -t 500 &')

    # Configure UDP flow
    server.cmd('iperf -s -u -p 2214 &')
    video_host.cmd('vlc -vvv https://herts365-my.sharepoint.com/:v:/g/personal/wf17aae_herts_ac_uk/EcknDw6ylkFJgeldS0QqZUIBYgWRzWdc9Vplwt9pdw8F1Q?e=1bvEPZ &')

    # Run CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
