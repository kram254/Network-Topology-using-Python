import os
import networkx as nx
import matplotlib.pyplot as plt

def create_network():
    net = nx.DiGraph()


    # Create switches
    net.add_node('s1')
    net.add_node('s2')
    net.add_node('s3')
    net.add_node('s4')

    # Create hosts
    net.add_node('h1', mac='00:00:00:00:00:01')
    net.add_node('h2', mac='00:00:00:00:00:02')
    net.add_node('h3', mac='00:00:00:00:00:03')
    net.add_node('h4', mac='00:00:00:00:00:04')
    net.add_node('h5', mac='00:00:00:00:00:05')
    net.add_node('h6', mac='00:00:00:00:00:06')
    net.add_node('server', mac='00:00:00:00:00:07')
    net.add_node('udp', mac='00:00:00:00:00:08')

    # Create links
    net.add_edge('h1', 's1')
    net.add_edge('h2', 's1')
    net.add_edge('h3', 's2')
    net.add_edge('h4', 's2')
    net.add_edge('h5', 's3')
    net.add_edge('h6', 's3')
    net.add_edge('server', 's4')
    net.add_edge('udp', 's4')

    net.add_edge('s1', 's2')
    net.add_edge('s2', 's3')
    net.add_edge('s3', 's4')
    net.add_edge('s4', 's1')

    # Start network
    pos = nx.spring_layout(net)
    nx.draw_networkx(net, pos, with_labels=True)
    plt.show()

    # Configure VLANs
    net.node['s1']['vlan'] = 100
    net.node['s2']['vlan'] = 100
    net.node['s3']['vlan'] = 200

    # Run ONOS commands
    onos = net.node['server']
    onos.cmd('onos netcfg localhost /path/to/network-cfg.json')

    # Run CLI
    CLI(net)
    
if __name__ == '__main__':
    setLogLevel('info')
    create_network()