# PURPOSE OF API : users can input the following to get an output from MCTS : max_levels, max_branches_per_node, and num_simulations
from flask import Flask , jsonify , request 
from main import Node, generate_tree, simulate_monte_carlo

app = Flask(__name__)

@app.route('/simulate', methods = ['POST'])
def simulate():
    data = request.get_json()
    max_levels = data.get("max_levels" , 10 ) # if not provided aautomatically sets to 10
    max_branches_per_node = data.get("max_branches_per_node" , 3)
    num_simulations = data.get("num_simulations" , 1000)

    root_node = Node("A", 1) # starting / root node 
    generate_tree(root_node , max_levels , max_branches_per_node) # generates our tree
    outcome_paths = simulate_monte_carlo(root_node , num_simulations) # performs MCTS

    return jsonify(outcome_paths[:10]) # returns the first 10 paths as a JSON

if __name__ == '__main__':
    app.run(debug=True)
