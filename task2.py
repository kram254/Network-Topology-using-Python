from mininet.cli import CLI
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import RemoteController

def create_network():
    net = Mininet(controller=RemoteController, link=TCLink)

    # Add controller
    controller = net.addController('controller', ip='127.0.0.1', port=6653)

    # Create nodes
    sta4refad = net.addHost('sta4refad', ip='192.168.1.4')
    sta5refad = net.addHost('sta5refad', ip='192.168.1.5')
    sta6refad = net.addHost('sta6refad', ip='192.168.1.6')
    server = net.addHost('server', ip='192.168.1.7')
    h1 = net.addHost('h1', ip='192.168.1.8')
    h3 = net.addHost('h3', ip='192.168.1.9')

    # Create switches
    s1 = net.addSwitch('s1')

    # Add links
    net.addLink(sta4refad, s1)
    net.addLink(sta5refad, s1)
    net.addLink(sta6refad, s1)
    net.addLink(server, s1)
    net.addLink(h1, s1)
    net.addLink(h3, s1)

    # Start network
    net.start()

    # Configure TCP server and client
    sta5refad.cmd('python -m SimpleHTTPServer 80 &')
    sta6refad.cmd('curl http://192.168.1.5:80')

    # Configure UDP server and client
    server.cmd('iperf -s -u -p 2214 &')
    h1.cmd('iperf -c 192.168.1.7 -u -p 2214 -b 10M -t 500')

    # Configure video streaming
    h3.cmd('vlc -vvv https://herts365-my.sharepoint.com/:v:/g/personal/wf17aae_herts_ac_uk/EcknDw6ylkFJgeldS0QqZUIBYgWRzWdc9Vplwt9pdw8F1Q?e=1bvEPZ &')

    # Open Mininet command line interface
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    create_network()
