from shapely.geometry import Point, MultiPoint
from shapely.geometry.polygon import Polygon
from shapely.ops import triangulate
from figures import BLUE, SIZE, set_limits, plot_coords, color_isvalid

# Only for visualizations
from descartes.patch import PolygonPatch
from matplotlib import pyplot


def point_in_area(point, triangles):
    for triangle in triangles:
        if point.within(triangle):
            return True
    return False

if __name__ == '__main__':
    # Create plot
    fig = pyplot.figure(1, figsize=SIZE, dpi=90)
    ax = fig.add_subplot(121)
    set_limits(ax, 0, 5, 0, 5)

    # Create polygon
    array = [[1, 2], [5, 3], [3, 3], [3, 4]]
    polygon = Polygon(array)


    points = MultiPoint([(1, 2), (5, 3), (3, 3), (3, 4), (1, 4)])
    triangles = triangulate(points)

    # Display triangles
    for triangle in triangles:
        patch = PolygonPatch(triangle, alpha=0.5, zorder=2)
        ax.add_patch(patch)

    # Display polygon
    # patch = PolygonPatch(polygon, alpha=0.5, zorder=2)
    # ax.add_patch(patch)

    # Create and display point
    point1 = Point(2.5, 3)
    ax.scatter(point1.x, point1.y)

    point2 = Point(1, 1)
    ax.scatter(point2.x, point2.y)


    # if polygon.contains(point):
    #     print('Polygon contains point')
    # if point.within(polygon):
    #     print('Point is in the polygon')

    if point_in_area(point1, triangles):
        print('Point1 in area')

    if point_in_area(point2, triangles):
        print('Point2 in area')

    pyplot.show()