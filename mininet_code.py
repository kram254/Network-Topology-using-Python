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
    sta1 = net.addStation('sta1', mac='00:00:00:00:11', ip='192.168.1.1')
    sta2 = net.addStation('sta2', mac='00:00:00:00:12', ip='192.168.1.2')
    sta3 = net.addStation('sta3', mac='00:00:00:00:13', ip='192.168.1.3')
    sta4 = net.addStation('sta4', mac='00:00:00:00:14', ip='192.168.1.4')

    # Create links
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)

    net.addLink(sta1, ap1)
    net.addLink(sta2, ap2)
    net.addLink(sta3, ap3)
    net.addLink(sta4, ap4)

    # Start network
    net.build()
    net.start()

    # Configure traffic
    sta5 = net.get('sta5')
    sta6 = net.get('sta6')
    h1 = net.get('h1')
    h3 = net.get('h3')
    
    sta5.cmd('iperf -s -p 2214 &')
    sta6.cmd('iperf -c 192.168.1.5 -p 2214 &')
    h1.cmd('iperf -u -s -p 2214 &')
    h3.cmd('iperf -u -c 192.168.1.6 -p 2214 &')
    h1.cmd('vlc -vvv https://herts365-my.sharepoint.com/:v:/g/personal/wf17aae_herts_ac_uk/EcknDw6ylkFJgeldS0QqZUIBYgWRzWdc9Vplwt9pdw8F1Q?e=1bvEPZ &')
    h3.cmd('vlc -vvv udp://@192.168.1.6:1234 &')

    # Run CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()