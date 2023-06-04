import networkx as nx
import matplotlib.pyplot as plt

def create_network():
    # Create a graph
    G = nx.Graph()

    # Add access points to the graph
    G.add_node('ap1', ssid='AP1_SSID', position=(10, 20))
    G.add_node('ap2', ssid='AP2_SSID', position=(30, 20))
    G.add_node('ap3', ssid='AP3_SSID', position=(10, 40))
    G.add_node('ap4', ssid='AP4_SSID', position=(30, 40))

    # Add stations to the graph
    G.add_node('sta1', mac='00:00:00:00:11', ip='192.168.1.1', position=(0, 0))
    G.add_node('sta2', mac='00:00:00:00:12', ip='192.168.1.2', position=(0, 0))
    G.add_node('sta3', mac='00:00:00:00:13', ip='192.168.1.3', position=(0, 0))
    G.add_node('sta4', mac='00:00:00:00:14', ip='192.168.1.4', position=(0, 0))

    # Add links between nodes
    G.add_edge('ap1', 'ap2')
    G.add_edge('ap2', 'ap3')
    G.add_edge('ap3', 'ap4')

    G.add_edge('ap1', 'sta1')
    G.add_edge('ap2', 'sta2')
    G.add_edge('ap3', 'sta3')
    G.add_edge('ap4', 'sta4')

    # Draw the network
    pos = nx.get_node_attributes(G, 'position')
    ssid = nx.get_node_attributes(G, 'ssid')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, alpha=0.8)
    nx.draw_networkx_labels(G, pos, labels=ssid, font_size=8)

    # Save the network visualization
    plt.savefig('network.png')

    # Show the network visualization
    plt.show()

if __name__ == '__main__':
    create_network()

