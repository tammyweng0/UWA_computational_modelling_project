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
    Initialise customer purchase states and
    individual baseline purchase probabilities.
    """

    for customer in G.nodes():
        G.nodes[customer]["purchased"] = False

        G.nodes[customer]["baseline_probability"] = (
            random.uniform(0.01, 0.10)
        )

    G.nodes[influencer]["purchased"] = True


def purchase_probability(
    G,
    customer,
    social_influence
):
    """
    Calculate a customer's probability of purchasing
    based on the purchase behaviour of their neighbours.
    """

    neighbours = list(G.neighbors(customer))

    purchased_neighbours = 0

    for neighbour in neighbours:
        if G.nodes[neighbour]["purchased"]:
            purchased_neighbours += 1

    fraction_purchased = (
        purchased_neighbours / len(neighbours)
    )

    baseline_probability = (
        G.nodes[customer]["baseline_probability"]
    )

    probability = (
        baseline_probability
        + social_influence * fraction_purchased
    )

    probability = min(1.0, probability)

    return probability


def simulation_step(G, social_influence):
    """
    Perform one time step of the simulation.

    Customers who have not yet purchased decide whether
    to purchase based on their purchase probability.

    Parameters
    ----------
    G : networkx.Graph
        The customer social network.

    social_influence : float
        Strength of social influence.

    Returns
    -------
    new_purchases : list
        Customers who purchased during this time step.
    """

    new_purchases = []

    for customer in G.nodes():

        # Skip customers who already purchased
        if G.nodes[customer]["purchased"]:
            continue

        probability = purchase_probability(
            G,
            customer,
            social_influence
        )

        random_number = random.random()

        if random_number < probability:
            new_purchases.append(customer)

    # Update purchase states after all customers
    # have made their decisions
    for customer in new_purchases:
        G.nodes[customer]["purchased"] = True

    return new_purchases


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