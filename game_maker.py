import numpy as np
import argparse

def generate_bimatrix_game(actions_agent1, actions_agent2):
    """
    Generates a bimatrix game with random payoffs for two agents.

    Parameters:
    actions_agent1 (int): Number of actions for Agent 1.
    actions_agent2 (int): Number of actions for Agent 2.

    Returns:
    payoff_matrix_agent1 (numpy.ndarray): Payoff matrix for Agent 1.
    payoff_matrix_agent2 (numpy.ndarray): Payoff matrix for Agent 2.
    """
    payoff_matrix_agent1 = np.random.randint(-10, 10, (actions_agent1, actions_agent2))
    payoff_matrix_agent2 = np.random.randint(-10, 10, (actions_agent1, actions_agent2))
    return payoff_matrix_agent1, payoff_matrix_agent2

def generate_prisoners_dilemma():
    """
    Generates the payoff matrices for the Prisoner's Dilemma.

    Returns:
    payoff_matrix_agent1 (numpy.ndarray): Payoff matrix for Agent 1.
    payoff_matrix_agent2 (numpy.ndarray): Payoff matrix for Agent 2.
    """
    payoff_matrix_agent1 = np.array([[3, 0], [5, 1]])
    payoff_matrix_agent2 = np.array([[3, 5], [0, 1]])
    return payoff_matrix_agent1, payoff_matrix_agent2

def print_bimatrix_game(payoff_matrix_agent1, payoff_matrix_agent2):
    """
    Prints the bimatrix game in a readable format.

    Parameters:
    payoff_matrix_agent1 (numpy.ndarray): Payoff matrix for Agent 1.
    payoff_matrix_agent2 (numpy.ndarray): Payoff matrix for Agent 2.
    """
    print("Bimatrix Game:")
    rows, cols = payoff_matrix_agent1.shape
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(f"({payoff_matrix_agent1[i, j]}, {payoff_matrix_agent2[i, j]})")
        print("\t".join(row))

def main():
    parser = argparse.ArgumentParser(description="Generate a bimatrix game with specified action counts.")
    parser.add_argument("--actions_agent1", type=int, default=2, help="Number of actions for Agent 1 (default: 2)")
    parser.add_argument("--actions_agent2", type=int, default=2, help="Number of actions for Agent 2 (default: 2)")
    parser.add_argument("--prisoners_dilemma", action="store_true", help="Generate the Prisoner's Dilemma game")

    args = parser.parse_args()

    if args.prisoners_dilemma:
        payoff_matrix_agent1, payoff_matrix_agent2 = generate_prisoners_dilemma()
    else:
        actions_agent1 = args.actions_agent1
        actions_agent2 = args.actions_agent2
        payoff_matrix_agent1, payoff_matrix_agent2 = generate_bimatrix_game(actions_agent1, actions_agent2)

    print_bimatrix_game(payoff_matrix_agent1, payoff_matrix_agent2)

if __name__ == "__main__":
    main()
