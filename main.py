import random

class Node:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def generate_tree(root, max_levels, max_branches_per_node):
    if root.level >= max_levels:
        return

    num_branches = random.randint(1, max_branches_per_node)  # Random number of branches
    for i in range(num_branches):
        child_name = f"{root.name}.{chr(65 + i)}"  # Naming children like A, B, C, etc.
        child_node = Node(child_name, root.level + 1)
        root.add_child(child_node)
        generate_tree(child_node, max_levels, max_branches_per_node)


def simulate_monte_carlo(root, num_simulations):
    outcomes = []

    for _ in range(num_simulations):
        current_node = root
        path = [current_node.name]

        while current_node.children:
            current_node = random.choice(current_node.children)
            path.append(current_node.name)

        outcomes.append(path)

    return outcomes


# Example usage:
max_levels = 10  # Customize this to set how deep the tree should be
max_branches_per_node = 3  # Customize this to set max number of branches per node
num_simulations = 1000  # Number of Monte Carlo simulations

# Create the root of the tree
root_node = Node("A", 1)

# Generate the tree
generate_tree(root_node, max_levels, max_branches_per_node)

# Run the Monte Carlo simulations
outcome_paths = simulate_monte_carlo(root_node, num_simulations)

# Display results
for outcome in outcome_paths[:10]:  # Print first 10 outcomes as an example
    print(" -> ".join(outcome))
