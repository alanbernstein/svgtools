import svgwrite
import re


def bezier_path(knots, close=False, **kwargs):
    # TODO: implement
    pass


def fix_svg_file_for_laser(svgfile, unit, width):
    """add units to svg file, change stroke-width"""
    # default stroke width is .5 - this causes "no data in document" error
    # ideally, need a hairline width, but this is a corel concept, not explicitly available in svg.
    # width=.387 -> fail
    # width=.384 -> success
    # the boundary is just about .004", for whatever reason...
    # just use 0.1

    with open(svgfile, 'r') as f:
        lines = f.readlines()

    with open(svgfile, 'w') as f:
        for line in lines:
            line = re.sub('width="([0-9]*)"', 'width="\\1%s"' % unit, line)
            line = re.sub('height="([0-9]*)"', 'height="\\1%s"' % unit, line)
            line = re.sub('stroke-width="0.5"', 'stroke-width="%0.1f"' % width, line)
            f.write(line)
            # print(line)


def path_from_array(points, close=False, **kwargs):
    # M 25,-25 L -25,-25 L -25,25 L 25,25 z
    # M x y  # move to x, y (start path)
    # L x y  # line from current point to x, y (add segment)
    # z      # close current subpath
    path_data = ''
    cmd = 'M'
    for p in points:
        path_data += '%s %f,%f ' % (cmd, p[0], p[1])
        cmd = 'L'
    if close:
        path_data += 'z'

    path = svgwrite.path.Path(d=path_data, **kwargs)
    return path


def write_paths_to_file(paths, fname, svg_scale=100):
    dwg = svgwrite.Drawing(fname, profile='tiny')
    for path in paths:
        print(path)
        polyline = svgwrite.shapes.Polyline(points=path * svg_scale,
                                            stroke='black',
                                            fill='white',
                                            stroke_width=0.1)
        dwg.add(polyline)
    dwg.save()
