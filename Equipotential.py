"""
Finding lines of the same potential requires us to draw points
However, seeing if every pixel has a certain potential is computationally expensive
A better way is to compare a limited amount of evenly distributed points, and connecting the dots when we're done
"""
import sys

from PointCharge import *

color = cm.YlOrRd

def heatmap(data):
    x = list([x[0]*PIX_RATIO for x in data.keys()])
    y = list([y[1]*PIX_RATIO for y in data.keys()])
    intensity = list([intensity for intensity in data.values()])
    Z = intensity
    #print(len(x), y.shape, Z.shape)

    # Plot the heatmap
    fig = plt.figure(frameon=False)
    fig.set_size_inches(10, 5)
    ax = fig.gca(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Intensity')

    # Scaling
    x_scale = 1
    y_scale = 1/2
    z_scale = 1

    scale = np.diag([x_scale, y_scale, z_scale, 1.0])
    scale = scale * (1.0 / scale.max())
    scale[3, 3] = 1.0

    # Camera Adjustments
    ax.view_init(elev=90, azim=90)

    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)


    def short_proj():
        return np.dot(Axes3D.get_proj(ax), scale)

    ax.get_proj = short_proj

    maximum = max(list(value for value in Z if abs(value) != float('inf')))
    minimum = min(list(value for value in Z if abs(value) != float('inf')))


    for i in range(len(x)):
        if Z[i] == float('inf'):
            Z[i] = maximum
        if Z[i] == -float('inf'):
            Z[i] = minimum

    # Plot the surface
    ax.tricontourf(x, y, Z, zdir='z', offset=-1.5 * 10 ** -10, cmap=color)

    plt.gca().invert_yaxis()
    fig.savefig("heatmap.png")
    plt.close()

def heatmap3D(data):

    x = list([x[0]*PIX_RATIO for x in data.keys()])
    y = list([y[1]*PIX_RATIO for y in data.keys()])
    intensity = list([intensity for intensity in data.values()])
    Z = intensity
    #print(len(x), y.shape, Z.shape)

    # Plot the heatmap
    fig = plt.figure(frameon=False)
    ax = fig.gca(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Intensity')

    # Scaling
    x_scale = 1
    y_scale = 1/2
    z_scale = 1

    scale = np.diag([x_scale, y_scale, z_scale, 1.0])
    scale = scale * (1.0 / scale.max())
    scale[3, 3] = 1.0


    def short_proj():
        return np.dot(Axes3D.get_proj(ax), scale)

    ax.get_proj = short_proj

    maximum = max(list(value for value in Z if abs(value) != float('inf')))
    minimum = min(list(value for value in Z if abs(value) != float('inf')))

    for i in range(len(x)):
        if Z[i] == float('inf'):
            Z[i] = maximum
        if Z[i] == -float('inf'):
            Z[i] = minimum

    # Plot the surface
    ax.tricontourf(x, y, Z, zdir='z', offset=-1.5 * 10 ** -10, cmap=color)

    ############################
    fig_data = go.Scatter3d(
    x= x,
    y= y,
    z= Z,
    mode='markers',
    marker=dict(
         size=3,
         colorscale='reds',  
         opacity=0.8
    )
    )
    fig_layout = go.Layout(
    scene = dict(
        xaxis = dict(title="X"),
        yaxis = dict(title="Y"),
        zaxis = dict(title="Potential"),
        aspectratio=dict(x=2, y=1, z=2)
        )
    )
    fig = go.Figure(data=[fig_data], layout=fig_layout)

    # tight layout
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.write_html("heatmap3D.html") #Modifiy the html file

    plt.close()
    

def potential_distribution():
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
    # Calculate the 90th percentile of the data
    max_threshold = np.percentile(list(potential_distribution.values()), 95)
    min_threshold = np.percentile(list(potential_distribution.values()), 5)

    # Filter out any values above/below the threshold
    cut_potential_distribution = {coord: volt for coord, volt in potential_distribution.items() if min_threshold <= volt <= max_threshold}
    return cut_potential_distribution
