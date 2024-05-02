import cairo
import numpy as np


def draw_polygon(ctx, vertices, fill_color):
    vertices = np.array(vertices)  # Ensure vertices are a NumPy array
    ctx.move_to(*vertices[-1])
    for x, y in vertices:
        ctx.line_to(x, y)
    ctx.close_path()
    r, g, b = fill_color
    ctx.set_source_rgb(r, g, b)  # Set the fill color
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)  # Black for the border
    ctx.set_line_width(0.05)
    ctx.stroke()


def main():
    width, height = 600, 400
    surface = cairo.SVGSurface("polygons.svg", width, height)
    ctx = cairo.Context(surface)

    # Define the scaling factor to fit the grid into our canvas size
    scale = 40  # Scale the grid size up to 40 pixels per unit
    # Apply scaling to simplify coordinate calculations
    ctx.scale(scale, scale)

    # Define colors for each case (simple RGB tuples)
    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1)]

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

    # Draw each case at different positions
    for i, case in enumerate(cases):
        x_offset = 3 * (i % 2)  # Shift right every second case
        y_offset = 3 * (i // 2)  # Shift down every two cases
        for j, polygon in enumerate(case):
            # Adjust each vertex by the offset using NumPy for array addition
            adjusted_polygon = polygon + np.array([x_offset, y_offset])
            draw_polygon(ctx, adjusted_polygon, colors[j % len(colors)])

    surface.finish()


if __name__ == "__main__":
    main()
