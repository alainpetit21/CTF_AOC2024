from engine.Challenge import Challenge
import matplotlib.pyplot as plt


class Node:
    def __init__(self, x, y, value, parent=None):
        self.x = x
        self.y = y
        self.value = value
        self.next: [Node] = []
        self.parent = parent
        self.score = 0

    def add_sub_tile(self, tile):
        self.next.append(tile)

    def set_score(self, score):
        self.score = score


class ChallengeDay10C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.trails = []
        self.numbers = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

        for y in range(len(self.data)):
            row = []
            for x in range(len(self.data[0])):
                if self.data[y][x] != '.':
                    row.append(int(self.data[y][x]))
                else:
                    row.append(-1)

            self.numbers.append(row)

    def visualize_tree(self):
        root = Node(-1, -1, -1)
        root.next = self.trails
        fig, ax = plt.subplots(figsize=(12, 8))

        # Recursive function to traverse and plot the tree
        def plot_node(node, x, y, x_offset, level=0):
            # Draw the node as a circle
            ax.plot(x, y, 'o', markersize=10, color='blue')

            # Annotate the node with its value and score
            ax.text(x, y, f'{node.value}', color='white',
                    ha='center', va='center', fontsize=9,
                    bbox=dict(facecolor='blue', edgecolor='none', boxstyle='round'))
            ax.text(x, y-0.3, f'{node.x};{node.y}', color='white',
                    ha='center', va='center', fontsize=5,
                    bbox=dict(facecolor='blue', edgecolor='none', boxstyle='round'))
            ax.text(x, y-0.6, f'{node.score}', color='white',
                    ha='center', va='center', fontsize=5,
                    bbox=dict(facecolor='blue', edgecolor='none', boxstyle='round'))

            # Position children horizontally around the parent node
            num_children = len(node.next)
            if num_children > 0:
                child_x_offset = x_offset / 2  # Reduce the spread of child nodes
                for i, child in enumerate(node.next):
                    child_x = x - x_offset / 2 + i * child_x_offset
                    child_y = y - 2  # Move down a level

                    # Draw the connecting line
                    ax.plot([x, child_x], [y, child_y], 'k-', lw=1)

                    # Recursive call to plot the child node
                    plot_node(child, child_x, child_y, child_x_offset, level + 1)

        # Initial call with the root node
        plot_node(root, 0, 0, 12)  # Start at (0, 0) with an x_offset of 6

        # Adjust plot appearance
        ax.set_aspect('equal')
        ax.axis('off')  # Turn off the axis for a cleaner look
        plt.show()

    def build_trail_tree(self, node, x, y, val, end_node_seen) -> int:
        nb_path_this_level = 0
        nb_path_sub_level = []

        # Check Left
        if x >= 1:
            if self.numbers[y][x - 1] == val + 1:
                trail = Node(x - 1, y, val + 1, node)
                ret = self.build_trail_tree(trail, x - 1, y, val + 1, end_node_seen)
                node.add_sub_tile(trail)

                nb_path_this_level += 1
                nb_path_sub_level.append(ret)

        # Check Right
        if x < len(self.numbers[0])-1:
            if self.numbers[y][x + 1] == val + 1:
                trail = Node(x + 1, y, val + 1, node)
                ret = self.build_trail_tree(trail, x + 1, y, val + 1, end_node_seen)
                node.add_sub_tile(trail)

                nb_path_this_level += 1
                nb_path_sub_level.append(ret)

        # Check Up
        if y >= 1:
            if self.numbers[y-1][x] == val + 1:
                trail = Node(x, y - 1, val + 1, node)
                ret = self.build_trail_tree(trail, x, y-1, val + 1, end_node_seen)
                node.add_sub_tile(trail)

                nb_path_this_level += 1
                nb_path_sub_level.append(ret)

        # Check Down
        if y < len(self.numbers)-1:
            if self.numbers[y+1][x] == val + 1:
                trail = Node(x, y + 1, val + 1, node)
                ret = self.build_trail_tree(trail, x, y+1, val + 1, end_node_seen)
                node.add_sub_tile(trail)

                nb_path_this_level += 1
                nb_path_sub_level.append(ret)

        if val != 9:
            node.set_score(sum(nb_path_sub_level))
            return node.score
        else:
            end_node_seen.append((x,y))
            return 1

    def run(self):
        for y in range(len(self.numbers)):
            for x in range(len(self.numbers)):
                if self.numbers[y][x] == 0:
                    end_node_seen = []
                    trail = Node(x, y, 0)
                    score = self.build_trail_tree(trail, x, y, 0 ,end_node_seen)
                    trail.set_score(score)
                    self.trails.append(trail)

        self.visualize_tree()
        self.result = sum([x.score for x in self.trails])
        return self.result
