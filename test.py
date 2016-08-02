#!/usr/bin/python
import numpy
import svgwrite
from dxfwrite import DXFEngine as dxf

from svgtools import path_from_array


svg_filename = 'test.svg'
drawing = {'points': 100 * numpy.array([[1, 1], [3, 1], [3, 4], [1, 3], [0, 4]]),
           'stroke': 'black',
           'fill': 'red'}
def main():
    #test_svgwrite_line()
    test_svgwrite_path()
    #test_svgwrite_polyline()


# svg polyline and path code works on bigpanda, macbook, 2016/07
def test_svgwrite_path():
    dwg = svgwrite.Drawing(svg_filename, profile='tiny')
    stroke = svgwrite.rgb(10, 10, 16, '%')
    path = path_from_array(**drawing)
    dwg.add(path)
    dwg.save()


def test_svgwrite_polyline():
    dwg = svgwrite.Drawing(svg_filename, profile='tiny')
    stroke = svgwrite.rgb(10, 10, 16, '%')
    polyline = svgwrite.shapes.Polyline(**drawing)
    dwg.add(polyline)
    dwg.save()
        

def test_svgwrite_line():
    dwg = svgwrite.Drawing(svg_filename, profile='tiny')
    stroke = svgwrite.rgb(10, 10, 16, '%')
    line = svgwrite.shapes.Line((0, 0), (10, 0), stroke=stroke)
    text = dwg.text('Test', insert=(0, 0.2), fill='red')
    dwg.add(line)
    dwg.add(text)
    dwg.save()


def test_dxfwrite_line():
    drawing = dxf.drawing('test.dxf')
    drawing.add(dxf.line((0, 0), (10, 0), color=7))
    drawing.add_layer('TEXTLAYER', color=2)
    drawing.add(dxf.text('Test', insert=(0, 0.2), layer='TEXTLAYER'))
    drawing.save()


def test_sdxf_line():
    import sdxf
    d = sdxf.Drawing()
    d.append(sdxf.Text('Hello World!', point=(3, 0, 1)))
    d.append(sdxf.Line(points=[(0, 0, 0), (1, 1, 1)]))
    d.saveas('hello_world.dxf')    




if __name__ == '__main__':
    main()
