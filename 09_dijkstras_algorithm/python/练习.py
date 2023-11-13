#第一个图
graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["c"] = 2

graph["a"] = {}
graph["a"]["b"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["d"] = 6
graph["b"]["fin"] = 3

graph["c"] = {}
graph["c"]["a"] = 8
graph["c"]["d"] = 7

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

#cost图表
infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = infinity
costs["c"] = 2
costs["d"] = infinity
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"]= "start"
parents["c"] = "start"
parents["b"]= None
parents["d"] = None
parents["fin"] = None
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: #遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: #如果当前节点的开销更低且未处理过
            lowest_cost = cost #就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node

# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)