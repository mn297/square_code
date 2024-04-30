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


# def generate_alphabet_square(ax, square_symbol_obj):
#     """
#     Generate a square in a given axes for a single symbol.
#     :param ax: The axes to draw the symbol in.
#     :param square_symbol_obj: SquareSymbol object containing symbol text, colors, and case number.
#     """
#     # Define a single case as an example
#     case = [
#         np.array([[0, 0], [0, 1], [0.3, 1], [0.3, 0.3]]),
#         np.array([[0.3, 0.3], [0.3, 1], [1, 1]]),
#         np.array([[0, 0], [0.3, 0], [0.3, 0.3]]),
#         np.array([[0.3, 0], [0.3, 0.3], [0.7, 0.7], [0.7, 0]]),
#         np.array([[0.7, 0], [0.7, 0.7], [1, 1], [1, 0]])
#     ]

#     colors = square_symbol_obj.get_color_lst()
#     for polygon, color in zip(case, colors):
#         ax.add_patch(Patches.Polygon(polygon, fill=True,
#                      edgecolor='black', facecolor=color, linewidth=1))

#     ax.set_aspect('equal')
#     ax.axis('off')
#     ax.set_xlim(0, 1)
#     ax.set_ylim(0, 1)
#     ax.set_title(f'{square_symbol_obj.symbol_txt}')


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

    # Loop through symbols and plot them with offset
    for idx, symbol in enumerate(sentence.upper()):
        accent = get_accent_type(sentence, accents_dict)
        if symbol in symbols_dict:
            # Calculate offset based on index
            # Horizontal offset (left to right)
            offset_col = (idx % col_num) * 3
            # Vertical offset (top to bottom)
            offset_row = (idx // col_num) * 3
            # Generate square with offset
            if accent:
                generate_alphabet_square(
                    ax, symbols_dict[accent], offset_x=offset_col, offset_y=offset_row)
            else:
                generate_alphabet_square(
                    ax, symbols_dict[symbol], offset_x=offset_col, offset_y=offset_row)

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


}


# Assume color_dict and SquareSymbol are defined elsewhere
color_patterns = {
    'moon': [color_dict['grey'], color_dict['red'], color_dict['grey'], color_dict['red'], color_dict['white']],
    'circumflex': [color_dict['red'], color_dict['white'], color_dict['red'], color_dict['white'], color_dict['grey']],
    'horn': [color_dict['white'], color_dict['grey'], color_dict['white'], color_dict['grey'], color_dict['red']],
    'hard_d': [color_dict['white'], color_dict['grey'], color_dict['red'], color_dict['red'], color_dict['white']],
    'acute': [color_dict['grey'], color_dict['red'], color_dict['white'], color_dict['white'], color_dict['grey']],
    'grave': [color_dict['red'], color_dict['white'], color_dict['grey'], color_dict['grey'], color_dict['red']],
    'hook': [color_dict['red'], color_dict['grey'], color_dict['white'], color_dict['white'], color_dict['red']],
    'tilde': [color_dict['white'], color_dict['red'], color_dict['grey'], color_dict['grey'], color_dict['white']],
    'dot': [color_dict['grey'], color_dict['white'], color_dict['red'], color_dict['red'], color_dict['grey']],
}

# Populate symbols_dict with all Vietnamese characters for each accent type
base_chars = 'AEIOUYaeiouy'
accents_dict = {
    'moon': (
        'Ăă'  # Lune
    ),
    'circumflex': (
        'ÂâÊêÔô'  # Circumflex
    ),
    'horn': (
        'ƠơƯư'  # Horn
    ),
    'hard_d': (
        'Đđ'  # Hard d
    ),
    'acute': (
        'ÁáẮắẤấÉéẾếÍíÓóỚớỐốÚúỨứÝý'  # Acute accent
        'ỚớỨứ'  # Acute with horn
    ),
    'grave': (
        'ÀàẰằẦầÈèỀềÌìÒòỜờỒồÙùỪừỲỳ'  # Grave accent
        'ỜờỪừ'  # Grave with horn
    ),
    'hook': (
        'ẢảẲẳẨẩẺẻỂểỈỉỎỏỞởỔổỦủỬửỶỷ'  # Hook above
        'ỞởỬử'  # Hook with horn
    ),
    'tilde': (
        'ÃãẴẵẪẫẼẽỄễĨĩÕõỠỡỖỗŨũỮữỸỹ'  # Tilde
        'ỠỡỮữ'  # Tilde with horn
    ),
    'dot': (
        'ẠạẶặẬậẸẹỆệỊịỌọỢợỤụỰựỴỵ'  # Dot below
        'ỢợỰự'  # Dot with horn
    ),
}

# # Expand accents_dict to include circumflex
# accents_dict = {
#     'acute': 'ÁáẮắẤấÉéẾếÍíÓóỚớỐốÚúỨứÝýỚớỨứ',
#     'grave': 'ÀàẰằẦầÈèỀềÌìÒòỜờỒồÙùỪừỲỳỜờỪừ',
#     'hook': 'ẢảẲẳẨẩẺẻỂểỈỉỎỏỞởỔổỦủỬửỶỷỞởỬử',
#     'tilde': 'ÃãẴẵẪẫẼẽỄễĨĩÕõỠỡỖỗŨũỮữỸỹỠỡỮữ',
#     'dot': 'ẠạẶặẬậẸẹỆệỊịỌọỢợỤụỰựỴỵỢợỰự',
#     'horn': 'ƠơƯư',
#     'circumflex': 'ÂâÊêÔô',  # Adding circumflex accent characters
# }

for key, chars in accents_dict.items():
    for char in chars:
        # Assuming all use case number 3
        symbols_dict[char] = SquareSymbol(char, color_patterns[key], 3)
# Now symbols_dict contains a SquareSymbol for every Vietnamese accented character


def get_accent_type(character, accents_dict):
    """
    Returns the type of accent for a given Vietnamese character.

    Args:
    character (str): The character to check.
    accents_dict (dict): A dictionary with accent types as keys and string of characters as values.

    Returns:
    str: The type of accent or None if the character has no accent or is not found.
    """
    for accent_type, chars in accents_dict.items():
        if character in chars:
            return accent_type
    return None  # Return None if the character is not found in any of the accent lists


# Example usage for a sentence
if __name__ == '__main__':
    sentence = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    sentence2 = ".,?!\'\"-/:;()&@\\[]{}<>#%_*+-ĂÂƠĐÁÀẢÃẠ"
    # Example with 2 rows and 6 columns
    plot_sentence(sentence, 6, 6)
    plot_sentence(sentence2, 6, 6)
