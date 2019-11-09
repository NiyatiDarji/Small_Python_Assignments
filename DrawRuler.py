# Draw a 12'' ruler with inch marks using graphics library
from graphics import *

def main():
    win = GraphWin("My Ruler",1500,500)
    rectangle = Rectangle(Point(0,0),Point(1300,200))
    rectangle.draw(win)

    for index in range(0,1300,100):
        line = Line(Point(index,0),Point(index,50))
        line.draw(win)
        measurement = Text(Point(index,60),int(index/100))
        measurement.draw(win)
    for quater_index in range(0,1200,25):
        quater_line = Line(Point(quater_index,0),Point(quater_index,40))
        quater_line.draw(win)
    win.getMouse()
    win.close()

main()
