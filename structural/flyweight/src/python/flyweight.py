from tkinter import Tk, Canvas

# Flyweight
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y, width, height):
        # Drawing a simple rectangle to represent the tree
        canvas.create_rectangle(x, y, x + width, y + height, fill=self.color)
        # Adding text to represent tree type and texture for demonstration
        canvas.create_text(x + width / 2, y + height / 2, text=f"{self.name}\n{self.texture}", fill='white')

# Flyweight Factory
class TreeFactory:
    tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls.tree_types:
            cls.tree_types[key] = TreeType(name, color, texture)
        return cls.tree_types[key]

# Context
class Tree:
    def __init__(self, x, y, width, height, tree_type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tree_type = tree_type

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y, self.width, self.height)

# Client
def main():
    root = Tk()
    root.title("Forest")
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()

    forest = []

    # Create different types of trees
    tree_type1 = TreeFactory.get_tree_type("Oak", "green", "Rough")
    tree_type2 = TreeFactory.get_tree_type("Pine", "darkgreen", "Smooth")

    # Create trees in the forest with shared tree types
    forest.append(Tree(10, 20, 50, 100, tree_type1))
    forest.append(Tree(70, 40, 60, 120, tree_type1))
    forest.append(Tree(150, 60, 40, 80, tree_type2))
    forest.append(Tree(220, 80, 50, 100, tree_type2))

    # Draw all trees
    for tree in forest:
        tree.draw(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
