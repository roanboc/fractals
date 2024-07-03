import turtle
import random

# Configuration variables
BRANCH_LENGTH = 100
LENGTH_DECREMENT = 10
MIN_LENGTH = 20
ANGLE = 15

BACKGROUND_COLOR = "white"
BRANCH_COLOR = "brown"
LEAF_COLOR = "green"

TURTLE_SPEED = 0  # Adjust the speed (1 is slowest, 10 or 0 is fastest)

# Set and random values to make it more organic

LEAF_PROBABILITY = 0.15     # 15% probability of making the current branch a leaf. 0 for no randomness
ANGLE_VARIATION = 20         # 0 for no variability
MIN_ANGLE = ANGLE - ANGLE_VARIATION
MAX_ANGLE = ANGLE + ANGLE_VARIATION
MAX_DEPTH = 300             # Parameter to control the number of recursions

def draw_leaf(t):
    t.color(LEAF_COLOR)
    t.begin_fill()
    t.left(45)
    for _ in range(2):
        t.circle(4, 90)  # Draw one half of the oval
        t.circle(4 // 2, 90)  # Draw the other half of the oval
    t.right(45)
    t.end_fill()
    t.color(BRANCH_COLOR)

def draw_branch(branch_length, depth, t):
    if depth > MAX_DEPTH:
        return

    if branch_length > MIN_LENGTH:
        # 15% probability to terminate the branch here and make a leaf
        if random.random() < LEAF_PROBABILITY:
            draw_leaf(t)
            return

        t.color(BRANCH_COLOR)
        # Draw the main branch
        t.forward(branch_length)
        angle = random.randint(MIN_ANGLE, MAX_ANGLE)
        # Draw the right subtree
        t.right(angle)
        draw_branch(branch_length - LENGTH_DECREMENT, depth + 1, t)
        # Return to the original position and orientation
        t.left(2 * angle)
        draw_branch(branch_length - LENGTH_DECREMENT, depth + 1, t)
        # Return to the original position and orientation
        t.right(angle)
        t.backward(branch_length)
    else:
        draw_leaf(t)

def main():
    window = turtle.Screen()
    window.bgcolor(BACKGROUND_COLOR)

    # Create a turtle named 't'
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(TURTLE_SPEED)

    # Move the turtle to a good starting position
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.forward(BRANCH_LENGTH * 1.5)

    subtree_segment = 1
    # Draw the tree
    for subtrees in range(1, 6):
        draw_branch(BRANCH_LENGTH * subtree_segment, 0, t)
        subtree_segment = subtree_segment - 0.05

    window.mainloop()

if __name__ == "__main__":
    main()
