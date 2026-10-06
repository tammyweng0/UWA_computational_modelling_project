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

    return influencer


def initialise_customers(G):
    """
    Give each customer an initial purchase state.
    """
    pass


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