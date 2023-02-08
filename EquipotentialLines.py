"""
Finding lines of the same potential requires us to draw points
However, seeing if every pixel has a certain potential is computationally expensive
A better way is to compare a limited amount of evenly distributed points, and connecting the dots when we're done
"""
import sys

from PointCharge import *


def polyfit(x_list, y_list):  # An impressive yet useless function
    degree = 10
    coefficients = np.polyfit(x_list, y_list, degree)

    # Calculate the values of the polynomial for each x-coordinate
    start_x, end_x = min(x_list), max(x_list)
    x_values = np.linspace(start_x, end_x, end_x - start_x)
    y_values = [sum(coefficient * x_value ** index for index,
                coefficient in enumerate(reversed(coefficients)))
                for x_value in range(start_x, end_x + 1)]

    points = list(zip(x_values, y_values))
    pygame.draw.lines(WIN, RED, False, points)


def proximity_sort(points):
    ordered_points = np.array([points[0]])
    unordered_points = np.array(points[1:])
    while unordered_points.size > 0:
        distances = np.linalg.norm(unordered_points - ordered_points[-1], axis=1)
        closest_point_index = np.argmin(distances)
        closest_point = unordered_points[closest_point_index]

        ordered_points = np.concatenate((ordered_points, [closest_point]), axis=0)
        unordered_points = np.delete(unordered_points, closest_point_index, axis=0)
    #ordered_points = np.concatenate((ordered_points, [ordered_points[1]]), axis=0)
    return ordered_points

def heatmap(data):

    x = list([x[0]*PIX_RATIO for x in data.keys()])
    y = list([y[1]*PIX_RATIO for y in data.keys()])
    intensity = list([intensity for intensity in data.values()])
    Z = intensity
    print(Z)
    #print(len(x), y.shape, Z.shape)

    # Plot the heatmap
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Intensity')
    x_scale = 1
    y_scale = 1/2
    z_scale = 1

    scale = np.diag([x_scale, y_scale, z_scale, 1.0])
    scale = scale * (1.0 / scale.max())
    scale[3, 3] = 1.0

    def short_proj():
        return np.dot(Axes3D.get_proj(ax), scale)

    ax.get_proj = short_proj

    for i in range(len(x)):
        if Z[i] == float('inf'):
            Z[i] = 0
        if Z[i] == -float('inf'):
            Z[i] = 0
    # Plot the surface
    ax.plot_trisurf(x, y, Z, linewidth=0.1, antialiased=True, cmap=cm.jet)
    ax.tricontourf(x, y, Z, zdir='z', offset=-1.5 * 10 ** -10, cmap=cm.coolwarm)

    # Show the plot
    plt.show()

def equipotential_lines():
    accuracy = 1 * 10 ** -10
    distribution = 1 * 10 ** -10  # Every ___ volts
    potential_distribution = dict()

    FREQUENCY = 100
    DENSITY = WIDTH / FREQUENCY
    for x in range(FREQUENCY):
        for y in range(int(FREQUENCY / 2)):
            potential = 0
            for charge in PointCharge.instances:
                radius = np.hypot(charge.xy[1] - y * DENSITY, charge.xy[0] - x * DENSITY)
                potential += k * charge.charge / radius
                potential_distribution[(x * DENSITY, y * DENSITY)] = potential
                # np.polyfit(potential_distribution.keys()[0], potential_distribution.keys()[1])
                if -0.000000000002 > potential > -0.0000000000025:
                    pygame.draw.circle(WIN, BLACK, (x * DENSITY, y * DENSITY), 1.0)

    equipotentials = list(filter(lambda potential: 0.000000000003 < potential < 0.000000000005,
                                 potential_distribution.values()))  # If a potential is within range of the desired value, its stored here
    equipotential_points = [point for point, potential in potential_distribution.items() if
                            potential in equipotentials]  # This gets the coordinates of potential points using the dictionary of all points and the values from the prior line

    heatmap(potential_distribution)
    #pygame.draw.lines(WIN, RED, False, proximity_sort(equipotential_points))

    # polyfit([points[0] for points in equipotential_points], [points[1] for points in equipotential_points])
