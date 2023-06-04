import networkx as nx
import matplotlib.pyplot as plt

def create_network():
    # Create empty graph
    G = nx.Graph()

    # Create access points
    G.add_node('ap1', ssid='AP1_SSID', mode='g', channel='1', position=(10, 20))
    G.add_node('ap2', ssid='AP2_SSID', mode='g', channel='1', position=(30, 20))
    G.add_node('ap3', ssid='AP3_SSID', mode='g', channel='1', position=(10, 40))
    G.add_node('ap4', ssid='AP4_SSID', mode='g', channel='1', position=(30, 40))

    # Create stations
    G.add_node('sta4refad', mac='00:00:00:00:11', position=(40, 0))
    G.add_node('sta5refad', mac='00:00:00:00:12', position=(40, 0))
    G.add_node('sta6refad', mac='00:00:00:00:13', position=(40, 0))

    # Create links
    G.add_edge('ap1', 'ap2')
    G.add_edge('ap2', 'ap3')
    G.add_edge('ap3', 'ap4')
    G.add_edge('sta4refad', 'ap1')
    G.add_edge('sta5refad', 'ap2')
    G.add_edge('sta6refad', 'ap3')

    # Visualize network
    pos = nx.get_node_attributes(G, 'position')
    nx.draw(G, pos, with_labels=True)
    plt.show()

if __name__ == '__main__':
    create_network()
