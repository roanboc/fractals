import turtle
import random

class TreeDrawer:
    """
    A class to draw a tree with turtle graphics.

    Attributes:
        branch_length (int): Initial length of the main branch.
        length_decrement (int): Decrement in branch length for each recursive step.
        min_length (int): Minimum length of a branch to stop recursion.
        angle (int): Base angle for branches.
        angle_variation (int): Variability in the angle for randomness.
        leaf_probability (float): Probability of ending a branch with a leaf.
        max_depth (int): Maximum depth of recursion to prevent infinite loops.
        background_color (str): Background color of the drawing window.
        branch_color (str): Color of the branches.
        leaf_color (str): Color of the leaves.
        turtle_speed (int): Speed of the turtle drawing.
    """
    
    def __init__(self):
        """
        Initializes the TreeDrawer with default configuration values.
        """
        self.branch_length = 100
        self.length_decrement = 10
        self.min_length = 20
        self.angle = 15
        self.angle_variation = 20
        self.leaf_probability = 0.15
        self.max_depth = 300
        self.background_color = "white"
        self.branch_color = "brown"
        self.leaf_color = "green"
        self.turtle_speed = 0  # 0 for fastest speed
    
    def draw_leaf(self, t):
        """
        Draws a leaf at the current turtle position.
        
        Parameters:
            t (turtle.Turtle): The turtle object used for drawing.
        """
        t.color(self.leaf_color)
        t.begin_fill()
        t.left(45)
        for _ in range(2):
            t.circle(4, 90)
            t.circle(4 // 2, 90)
        t.right(45)
        t.end_fill()
        t.color(self.branch_color)
    
    def draw_branch(self, branch_length, depth, t):
        """
        Recursively draws a branch with optional sub-branches and leaves.
        
        Parameters:
            branch_length (int): The current length of the branch.
            depth (int): The current depth of the recursion.
            t (turtle.Turtle): The turtle object used for drawing.
        """
        if depth > self.max_depth:
            return
        
        if branch_length > self.min_length:
            if random.random() < self.leaf_probability:
                self.draw_leaf(t)
                return
            
            t.color(self.branch_color)
            arc_radius = branch_length / 2
            arc_extent = 60
            
            # Draw the main branch using an arc
            t.circle(arc_radius, arc_extent)
            angle = random.randint(self.angle - self.angle_variation, self.angle + self.angle_variation)
            
            # Draw the right subtree
            t.right(angle)
            self.draw_branch(branch_length - self.length_decrement, depth + 1, t)
            
            # Return to the original position and orientation
            t.left(2 * angle)
            self.draw_branch(branch_length - self.length_decrement, depth + 1, t)
            
            # Return to the original position and orientation
            t.right(angle)
            t.circle(-arc_radius, arc_extent)
        else:
            self.draw_leaf(t)
    
    def setup_turtle(self):
        """
        Sets up the turtle and window for drawing.
        
        Returns:
            turtle.Turtle: The turtle object used for drawing.
        """
        window = turtle.Screen()
        window.bgcolor(self.background_color)
        
        t = turtle.Turtle()
        t.shape("turtle")
        t.speed(self.turtle_speed)
        
        t.left(90)
        t.up()
        t.backward(300)
        t.down()
        t.forward(self.branch_length * 1.5)
        
        return t
    
    def draw_tree(self):
        """
        Draws the tree with the configured settings.
        """
        t = self.setup_turtle()
        subtree_segment = 1
        
        for _ in range(1, 6):
            self.draw_branch(self.branch_length * subtree_segment, 0, t)
            subtree_segment -= 0.05
        
        turtle.done()

if __name__ == "__main__":
    tree_drawer = TreeDrawer()
    tree_drawer.draw_tree()
