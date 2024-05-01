import matplotlib.pyplot as plt
import matplotlib.patches as Patches
import numpy as np
import math


class SquareSymbol:
    def __init__(self, symbol_txt, color_lst, case):
        self.symbol_txt = symbol_txt
        self.color_lst = color_lst
        self.case = case  # This is the new attribute for case number

    def get_color_lst(self):
        return self.color_lst

    def get_case(self):
        return self.case


def generate_alphabet_square(ax, square_symbol_obj, offset_x=0, offset_y=0):
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
        np.array([[1, 1], [1, 3], [2, 3], [2, 2]]),
        np.array([[2, 2], [2, 3], [3, 3]]),
        np.array([[0, 0], [2, 2], [2, 0]]),
        np.array([[2, 0], [2, 2], [3, 3], [3, 0]]),
    ]
    case_3 = [
        np.array([[0, 3], [1, 3], [1, 2]]),
        np.array([[1, 2], [1, 3], [2, 3], [2, 1]]),
        np.array([[2, 1], [2, 3], [3, 3], [3, 0]]),
        np.array([[0, 0], [0, 3], [1, 2], [1, 0]]),
        np.array([[1, 0], [1, 2], [3, 0]]),
    ]
    case_4 = [
        np.array([[0, 3], [2, 3], [2, 1]]),
        np.array([[2, 1], [2, 3], [3, 3], [3, 0]]),
        np.array([[0, 0], [0, 3], [1, 2], [1, 0]]),
        np.array([[1, 0], [1, 2], [2, 1], [2, 0]]),
        np.array([[2, 0], [2, 1], [3, 0]]),
    ]
    cases = [case_1, case_2, case_3, case_4]

    # Get the current axis for plotting
    # ax = plt.gca()

    # Apply colors
    num_colors = len(square_symbol_obj.get_color_lst())
    for i, polygon in enumerate(cases[square_symbol_obj.get_case() - 1]):
        color = square_symbol_obj.get_color_lst()[i % num_colors]
        polygon = polygon + np.array([offset_x,  -offset_y])
        # Create a patch object for each polygon, specifying edges and linewidth
        ax.add_patch(Patches.Polygon(polygon, fill=True,
                     edgecolor='black', facecolor=color, linewidth=2))

    # Calculate the center of the square for placing the text
    # Assuming all your squares are of size 3x3 based on the given cases
    center_x = offset_x + 1.5  # Halfway across the width of the square
    center_y = -offset_y + 1.5  # Halfway up the height of the square

    # Add text at the center of the square
    ax.text(center_x, center_y, square_symbol_obj.symbol_txt,
            horizontalalignment='center', verticalalignment='center',
            fontsize=12, color='b', weight='bold')


def plot_sentence(sentence, row_num, col_num):
    """
    Plot a sentence with each character offset by 3 times its index in either columns or rows.
    :param sentence: The sentence to render.
    :param symbols_dict: Dictionary of SquareSymbol objects for each character.
    :param row_num: Expected number of rows in the grid.
    :param col_num: Expected number of columns in the grid.
    """
    fig, ax = plt.subplots(figsize=(col_num * 3, row_num * 3)
                           )  # Scale figure size based on the number of columns and rows

    # PREPROCESSING
    processed_lst = []
    for idx, symbol in enumerate(sentence.upper()):
        if symbol.isspace():  # Skip spaces
            continue
         # Default to just the character itself if not decomposed
        components = decomposition_dict.get(
            symbol, (symbol,))
        for component in components:
            processed_lst.append(component)

    for idx, char in enumerate(processed_lst):
        # Calculate offset based on index
        # Horizontal offset (left to right)
        offset_x = (idx % col_num) * 3
        # Vertical offset (top to bottom)
        offset_y = (idx // col_num) * 3
        # Generate square with offset
        generate_alphabet_square(
            ax, symbols_dict[char], offset_x, offset_y)

    # Set the x-axis limits to accommodate all columns
    ax.set_xlim(0, col_num * 3)
    # Set the y-axis limits to accommodate all rows
    ax.set_ylim(-row_num*3, row_num * 3)
    # Maintain aspect ratio
    ax.set_aspect('equal')
    # Hide axis
    ax.axis('off')

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
    'grey': '#404040',
    'black': '#000000'
}

# Example usage with a list of colors
# only use red, grey and white colors
symbols_dict = {
    'A': SquareSymbol('A', [color_dict['red'], color_dict['white'], color_dict['white'], color_dict['red'], color_dict['grey']], 1),
    'B': SquareSymbol('B', [color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['grey']], 1),
    'C': SquareSymbol('C', [color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['white']], 1),
    'D': SquareSymbol('D', [color_dict['red'], color_dict['grey'], color_dict['grey'], color_dict['red'], color_dict['white']], 1),
    'E': SquareSymbol('E', [color_dict['white'], color_dict['grey'], color_dict['grey'], color_dict['white'], color_dict['red']], 1),
    'F': SquareSymbol('F', [color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['red']], 1),
    'G': SquareSymbol('G', [color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['grey']], 1),
    'H': SquareSymbol('H', [color_dict['white'], color_dict['red'], color_dict['red'], color_dict['white'], color_dict['grey']], 1),
    'I': SquareSymbol('I', [color_dict['grey'], color_dict['red'], color_dict['red'], color_dict['grey'], color_dict['white']], 1),
    'J': SquareSymbol('J', [color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['white']], 1),
    'K': SquareSymbol('K', [color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['red']], 1),
    'L': SquareSymbol('L', [color_dict['grey'], color_dict['white'], color_dict['white'], color_dict['grey'], color_dict['red']], 1),
    'M': SquareSymbol('M', [color_dict['red'], color_dict['white'], color_dict['white'], color_dict['grey'], color_dict['red']], 1),
    'N': SquareSymbol('N', [color_dict['red'], color_dict['grey'], color_dict['grey'], color_dict['white'], color_dict['red']], 1),
    'O': SquareSymbol('O', [color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['white'], color_dict['red']], 2),
    'P': SquareSymbol('P', [color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['grey'], color_dict['red']], 2),
    'Q': SquareSymbol('Q', [color_dict['white'], color_dict['grey'], color_dict['grey'], color_dict['red'], color_dict['white']], 1),
    'R': SquareSymbol('R', [color_dict['white'], color_dict['red'], color_dict['red'], color_dict['grey'], color_dict['white']], 1),
    'S': SquareSymbol('S', [color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['grey'], color_dict['white']], 2),
    'T': SquareSymbol('T', [color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['red'], color_dict['white']], 2),
    'U': SquareSymbol('U', [color_dict['grey'], color_dict['red'], color_dict['red'], color_dict['white'], color_dict['grey']], 1),
    'V': SquareSymbol('V', [color_dict['grey'], color_dict['white'], color_dict['white'], color_dict['red'], color_dict['grey']], 1),
    'W': SquareSymbol('W', [color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['red'], color_dict['grey']], 2),
    'X': SquareSymbol('X', [color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['white'], color_dict['grey']], 2),
    'Y': SquareSymbol('Y', [color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['white'], color_dict['red']], 2),
    'Z': SquareSymbol('Z', [color_dict['grey'], color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['red']], 2),
    '0': SquareSymbol('0', [color_dict['white'], color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['red']], 2),
    '1': SquareSymbol('1', [color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['grey'], color_dict['red']], 2),
    '2': SquareSymbol('2', [color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['grey'], color_dict['red']], 2),
    '3': SquareSymbol('3', [color_dict['red'], color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['white']], 2),
    '4': SquareSymbol('4', [color_dict['grey'], color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['white']], 2),
    '5': SquareSymbol('5', [color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['red'], color_dict['white']], 2),
    '6': SquareSymbol('6', [color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['red'], color_dict['grey']], 2),
    '7': SquareSymbol('7', [color_dict['white'], color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['grey']], 2),
    '8': SquareSymbol('8', [color_dict['red'], color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['grey']], 2),
    '9': SquareSymbol('9', [color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['white'], color_dict['grey']], 2),

    '.': SquareSymbol('-', [color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['red'], color_dict['white']], 3),
    ',': SquareSymbol(',', [color_dict['white'], color_dict['red'], color_dict['white'], color_dict['red'], color_dict['grey']], 3),
    '?': SquareSymbol('?', [color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['red'], color_dict['grey']], 3),
    '!': SquareSymbol('!', [color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['white'], color_dict['grey']], 3),
    '\'': SquareSymbol('\'', [color_dict['grey'], color_dict['white'], color_dict['grey'], color_dict['white'], color_dict['red']], 3),
    '\"': SquareSymbol('\"', [color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['white'], color_dict['red']], 3),
    '-': SquareSymbol('-', [color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['grey'], color_dict['red']], 3),
    '/': SquareSymbol('/', [color_dict['red'], color_dict['grey'], color_dict['red'], color_dict['grey'], color_dict['white']], 3),
    ':': SquareSymbol(':', [color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['grey'], color_dict['white']], 3),
    ';': SquareSymbol(';', [color_dict['white'], color_dict['red'], color_dict['red'], color_dict['grey'], color_dict['white']], 4),
    '(': SquareSymbol('(', [color_dict['grey'], color_dict['red'], color_dict['red'], color_dict['white'], color_dict['grey']], 4),
    ')': SquareSymbol(')', [color_dict['grey'], color_dict['white'], color_dict['white'], color_dict['red'], color_dict['grey']], 4),
    '&': SquareSymbol('&', [color_dict['red'], color_dict['white'], color_dict['white'], color_dict['grey'], color_dict['red']], 4),
    '@': SquareSymbol('@', [color_dict['red'], color_dict['grey'], color_dict['grey'], color_dict['white'], color_dict['red']], 4),
    '\\': SquareSymbol('\\', [color_dict['white'], color_dict['grey'], color_dict['grey'], color_dict['red'], color_dict['white']], 4),
    '[': SquareSymbol('[', [color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['red'], color_dict['white']], 4),
    ']': SquareSymbol(']', [color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['red'], color_dict['grey']], 4),
    '{': SquareSymbol('{', [color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['red'], color_dict['white']], 4),
    '}': SquareSymbol('}', [color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['red'], color_dict['grey']], 4),
    '<': SquareSymbol('<', [color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['white'], color_dict['grey']], 4),
    '>': SquareSymbol('>', [color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['white'], color_dict['red']], 4),
    '#': SquareSymbol('#', [color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['white'], color_dict['grey']], 4),
    '%': SquareSymbol('%', [color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['white'], color_dict['red']], 4),
    '_': SquareSymbol('_', [color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['grey'], color_dict['red']], 4),
    '*': SquareSymbol('*', [color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['grey'], color_dict['white']], 4),
    '+': SquareSymbol('+', [color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['grey'], color_dict['red']], 4),
    '=': SquareSymbol('=', [color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['grey'], color_dict['white']], 4),

    'moon': SquareSymbol('moon', [color_dict['grey'], color_dict['red'], color_dict['grey'], color_dict['red'], color_dict['white']], 3),
    'circumflex': SquareSymbol('circumflex', [color_dict['red'], color_dict['white'], color_dict['red'], color_dict['white'], color_dict['grey']], 3),
    'horn': SquareSymbol('horn', [color_dict['white'], color_dict['grey'], color_dict['white'], color_dict['grey'], color_dict['red']], 3),
    'hard_d': SquareSymbol('hard_d', [color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['red'], color_dict['white']], 3),
    'acute': SquareSymbol('acute', [color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['white'], color_dict['grey']], 3),
    'grave': SquareSymbol('grave', [color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['grey'], color_dict['red']], 3),
    'hook': SquareSymbol('hook', [color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['white'], color_dict['red']], 3),
    'tilde': SquareSymbol('tilde', [color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['grey'], color_dict['white']], 3),
    'dot': SquareSymbol('dot', [color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['red'], color_dict['grey']], 3),
}


decomposition_dict = {
    # Vowels with acute accent
    'Á': ('A', 'acute'), 'á': ('a', 'acute'),
    'É': ('E', 'acute'), 'é': ('e', 'acute'),
    'Í': ('I', 'acute'), 'í': ('i', 'acute'),
    'Ó': ('O', 'acute'), 'ó': ('o', 'acute'),
    'Ú': ('U', 'acute'), 'ú': ('u', 'acute'),
    'Ý': ('Y', 'acute'), 'ý': ('y', 'acute'),

    # Vowels with grave accent
    'À': ('A', 'grave'), 'à': ('a', 'grave'),
    'È': ('E', 'grave'), 'è': ('e', 'grave'),
    'Ì': ('I', 'grave'), 'ì': ('i', 'grave'),
    'Ò': ('O', 'grave'), 'ò': ('o', 'grave'),
    'Ù': ('U', 'grave'), 'ù': ('u', 'grave'),
    'Ỳ': ('Y', 'grave'), 'ỳ': ('y', 'grave'),

    # Vowels with hook above
    'Ả': ('A', 'hook'), 'ả': ('a', 'hook'),
    'Ẻ': ('E', 'hook'), 'ẻ': ('e', 'hook'),
    'Ỉ': ('I', 'hook'), 'ỉ': ('i', 'hook'),
    'Ỏ': ('O', 'hook'), 'ỏ': ('o', 'hook'),
    'Ủ': ('U', 'hook'), 'ủ': ('u', 'hook'),
    'Ỷ': ('Y', 'hook'), 'ỷ': ('y', 'hook'),

    # Vowels with tilde
    'Ã': ('A', 'tilde'), 'ã': ('a', 'tilde'),
    'Ẽ': ('E', 'tilde'), 'ẽ': ('e', 'tilde'),
    'Ĩ': ('I', 'tilde'), 'ĩ': ('i', 'tilde'),
    'Õ': ('O', 'tilde'), 'õ': ('o', 'tilde'),
    'Ũ': ('U', 'tilde'), 'ũ': ('u', 'tilde'),
    'Ỹ': ('Y', 'tilde'), 'ỹ': ('y', 'tilde'),

    # Vowels with dot below
    'Ạ': ('A', 'dot'), 'ạ': ('a', 'dot'),
    'Ẹ': ('E', 'dot'), 'ẹ': ('e', 'dot'),
    'Ị': ('I', 'dot'), 'ị': ('i', 'dot'),
    'Ọ': ('O', 'dot'), 'ọ': ('o', 'dot'),
    'Ụ': ('U', 'dot'), 'ụ': ('u', 'dot'),
    'Ỵ': ('Y', 'dot'), 'ỵ': ('y', 'dot'),

    # Circumflex
    'Â': ('A', 'circumflex'), 'â': ('a', 'circumflex'),
    'Ê': ('E', 'circumflex'), 'ê': ('e', 'circumflex'),
    'Ô': ('O', 'circumflex'), 'ô': ('o', 'circumflex'),

    # Horn
    'Ơ': ('O', 'horn'), 'ơ': ('o', 'horn'),
    'Ư': ('U', 'horn'), 'ư': ('u', 'horn'),

    # Breve
    'Ă': ('A', 'moon'), 'ă': ('a', 'moon'),

    # Special case for D with stroke
    'Đ': ('D', 'hard_d'), 'đ': ('d', 'hard_d'),

    # Combinations with circumflex and acute, grave, hook, tilde, dot
    'Ấ': ('A', 'circumflex', 'acute'), 'ấ': ('a', 'circumflex', 'acute'),
    'Ầ': ('A', 'circumflex', 'grave'), 'ầ': ('a', 'circumflex', 'grave'),
    'Ẩ': ('A', 'circumflex', 'hook'), 'ẩ': ('a', 'circumflex', 'hook'),
    'Ẫ': ('A', 'circumflex', 'tilde'), 'ẫ': ('a', 'circumflex', 'tilde'),
    'Ậ': ('A', 'circumflex', 'dot'), 'ậ': ('a', 'circumflex', 'dot'),

    # Combinations with horn and acute, grave, hook, tilde, dot
    'Ớ': ('O', 'horn', 'acute'), 'ớ': ('o', 'horn', 'acute'),
    'Ờ': ('O', 'horn', 'grave'), 'ờ': ('o', 'horn', 'grave'),
    'Ở': ('O', 'horn', 'hook'), 'ở': ('o', 'horn', 'hook'),
    'Ỡ': ('O', 'horn', 'tilde'), 'ỡ': ('o', 'horn', 'tilde'),
    'Ợ': ('O', 'horn', 'dot'), 'ợ': ('o', 'horn', 'dot'),
    'Ứ': ('U', 'horn', 'acute'), 'ứ': ('u', 'horn', 'acute'),
    'Ừ': ('U', 'horn', 'grave'), 'ừ': ('u', 'horn', 'grave'),
    'Ử': ('U', 'horn', 'hook'), 'ử': ('u', 'horn', 'hook'),
    'Ữ': ('U', 'horn', 'tilde'), 'ữ': ('u', 'horn', 'tilde'),
    'Ự': ('U', 'horn', 'dot'), 'ự': ('u', 'horn', 'dot'),

    # Combinations with moon and acute, grave, hook, tilde, dot
    'Ắ': ('A', 'moon', 'acute'), 'ắ': ('a', 'moon', 'acute'),
    'Ằ': ('A', 'moon', 'grave'), 'ằ': ('a', 'moon', 'grave'),
    'Ẳ': ('A', 'moon', 'hook'), 'ẳ': ('a', 'moon', 'hook'),
    'Ẵ': ('A', 'moon', 'tilde'), 'ẵ': ('a', 'moon', 'tilde'),
    'Ặ': ('A', 'moon', 'dot'), 'ặ': ('a', 'moon', 'dot'),

    # Additional entries can be added for any specific use-cases or missing characters:
    'Ế': ('E', 'circumflex', 'acute'), 'ế': ('e', 'circumflex', 'acute'),
    'Ề': ('E', 'circumflex', 'grave'), 'ề': ('e', 'circumflex', 'grave'),
    'Ể': ('E', 'circumflex', 'hook'), 'ể': ('e', 'circumflex', 'hook'),
    'Ễ': ('E', 'circumflex', 'tilde'), 'ễ': ('e', 'circumflex', 'tilde'),
    'Ệ': ('E', 'circumflex', 'dot'), 'ệ': ('e', 'circumflex', 'dot'),

    'Ố': ('O', 'circumflex', 'acute'), 'ố': ('o', 'circumflex', 'acute'),
    'Ồ': ('O', 'circumflex', 'grave'), 'ồ': ('o', 'circumflex', 'grave'),
    'Ổ': ('O', 'circumflex', 'hook'), 'ổ': ('o', 'circumflex', 'hook'),
    'Ỗ': ('O', 'circumflex', 'tilde'), 'ỗ': ('o', 'circumflex', 'tilde'),
    'Ộ': ('O', 'circumflex', 'dot'), 'ộ': ('o', 'circumflex', 'dot'),

    # Additional diacritics or modified letters could be defined similarly,
    # ensuring all required combinations are covered.
}

# Example usage for a sentence
if __name__ == '__main__':
    sentence = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    sentence2 = ".,?!\'\"-/:;()&@\\[]{}<>#%_*+-ĂÂƠĐÁÀẢÃẠ"
    sentence3 = "ARCHITECTHOÀNGCÔNGHUÂN"
    # Example with 2 rows and 6 columns
    plot_sentence(sentence, 6, 6)
    plot_sentence(sentence2, 6, 6)
    plot_sentence(sentence3, 3, 8)
