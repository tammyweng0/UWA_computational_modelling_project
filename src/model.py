'''
HOW the simulation works
'''

import networkx as nx
import random


def create_network(num_customers, edges_per_new_node):
    """
    Create a consumer social network using the Barabasi-Albert preferential attachment model.

    Parameters
    ----------
    num_customers : int
        Number of consumers in the network.

    edges_per_new_node : int
        Number of edges created by each new node.

    Returns
    -------
    G : networkx.Graph
        The generated consumer social network.
    """

    G = nx.barabasi_albert_graph(
        num_customers,
        edges_per_new_node
    )

    return G
    

def select_influencer(G, strategy):
    """
    Select a customer as the influencer based on their position in the social network.

    Parameters
    ----------
    G : networkx.Graph
        The customer social network.

    strategy : str
        Strategy used to select the influencer.

    Returns
    -------
    influencer : int
        Node ID of the selected influencer.
    """

    degrees = dict(G.degree())

    if strategy == "central":
        influencer = max(
            degrees,
            key=degrees.get
        )

    elif strategy == "less_central":
        # Sort customers from lowest to highest degree
        ranked_customers = sorted(
            degrees,
            key=degrees.get
        )

        # Select customer around the 25th percentile
        index = len(ranked_customers) // 4

        influencer = ranked_customers[index]

    else:
        raise ValueError(
            "strategy must be 'central' or 'less_central'"
        )

    return influencer


def initialise_customers(G, influencer):
    """
    Initialise the purchase state of all customers.

    All customers start without purchasing the product,
    except the selected influencer.

    Parameters
    ----------
    G : networkx.Graph
        The customer social network.

    influencer : int
        Node ID of the selected influencer.
    """

    # Initially, nobody has purchased the product
    for customer in G.nodes():
        G.nodes[customer]["purchased"] = False

    # The influencer starts with the product
    G.nodes[influencer]["purchased"] = True


def purchase_probability(G, customer, social_influence):
    """
    Calculate a customer's probability of purchasing.
    """
    pass


def simulation_step(G, social_influence):
    """
    Perform one time step of the simulation.
    """
    pass


def run_simulation(
    num_customers,
    edges_per_new_node,
    influencer_strategy,
    social_influence,
    max_steps
):
    """
    Run the complete simulation.
    """
    pass