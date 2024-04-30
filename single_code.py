import matplotlib.pyplot as plt
import matplotlib.patches as Patches
import numpy as np


class SquareSymbol:
    def __init__(self, symbol_txt, color_lst, case):
        self.symbol_txt = symbol_txt
        self.color_lst = color_lst
        self.case = case  # This is the new attribute for case number

    def get_color_lst(self):
        return self.color_lst

    def get_case(self):
        return self.case


def generate_alphabet_square(ax, square_symbol_obj):
    """
    Generate an image of a square with polygons defined explicitly without vertex markers.
    :param symbol: Character or symbol to label the square with.
    :param colors: List of colors for the edges of the polygons.
    """

    # Define polygons with explicit vertices
    case_1 = [
        # Coordinates for each vertex
        np.array([[0, 0], [0, 3], [1, 3], [1, 1]]),
        np.array([[1, 1], [1, 3], [3, 3]]),
        np.array([[0, 0], [1, 0], [1, 1]]),
        np.array([[1, 0], [1, 1], [2, 2], [2, 0]]),
        np.array([[2, 0], [2, 2], [3, 3], [3, 0]])
    ]
    case_2 = [
        np.array([[0, 0], [0, 3], [1, 3], [1, 1]]),
        np.array([[1, 1], [1, 3], [2, 3], [3, 3]]),
        np.array([[2, 2], [2, 3], [3, 3]]),
        np.array([[0, 0], [2, 0], [2, 2]]),
        np.array([[2, 0], [2, 2], [3, 0], [3, 3]]),
    ]
    case_3 = [
        np.array([[0, 3], [1, 3], [1, 2]]),
        np.array([[1, 2], [1, 3], [2, 3], [2, 1]]),
        np.array([[2, 3], [2, 1], [3, 3], [3, 0]]),
        np.array([[0, 0], [0, 3], [1, 2], [1, 0]]),
        np.array([[1, 0], [1, 2], [3, 0]]),
    ]
    case_4 = [
        np.array([[0, 3], [2, 1], [2, 3]]),
        np.array([[2, 3], [2, 1], [3, 0], [3, 3]]),
        np.array([[0, 0], [0, 3], [1, 2], [1, 0]]),
        np.array([[1, 0], [1, 2], [2, 1], [2, 0]]),
        np.array([[2, 0], [2, 1], [3, 0]]),
    ]
    cases = [case_1, case_2, case_3, case_4]

    # Get the current axis for plotting
    ax = plt.gca()

    # Apply colors cyclically based on available colors in the input
    num_colors = len(square_symbol_obj.get_color_lst())
    for i, polygon in enumerate(cases[square_symbol_obj.get_case() - 1]):
        color = square_symbol_obj.get_color_lst()[i % num_colors]
        # Create a patch object for each polygon, specifying edges and linewidth
        ax.add_patch(Patches.Polygon(polygon, fill=True,
                     edgecolor='black', facecolor=color, linewidth=2))

    # Setting the aspect of the plot to be equal, to maintain the square
    ax.set_aspect('equal')

    # Remove axes
    plt.axis('off')

    # Set limits and title
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    plt.title(
        f'Symbol: {square_symbol_obj.symbol_txt}, Case: {square_symbol_obj.get_case()}')

    # Show plot
    plt.show()


# Color dictionary for easier color management
color_dict = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
    'magenta': '#FF00FF',
    'cyan': '#00FFFF',
    'white': '#FFFFFF',
    'grey': '#808080',
    'black': '#000000'
}

# Example usage with a list of colors
# only use red, grey and white colors
symbols_dict = {
    # 'A': [color_dict['red'], color_dict['green'], color_dict['blue'], color_dict['yellow'], color_dict['grey']],
    'A': SquareSymbol('A', [color_dict['red'], color_dict['white'], color_dict['white'], color_dict['red'], color_dict['grey']], 1),
    'B': SquareSymbol('B', [color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['grey']], 1),
    'C': SquareSymbol('C', [color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['white']], 1),

}
if __name__ == '__main__':
    fig, ax = plt.subplots()

    # Generate squares for each symbol
    for symbol, square_symbol_obj in symbols_dict.items():
        generate_alphabet_square(ax, square_symbol_obj)
