import string
import numpy as np
import matplotlib.pyplot as plt


class Grapher:

    def __init__(self, range1 = -10, range2 = 10, accuracy = 0.01):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.grid(True)
        ax.spines['left'].set_position(('data', 0.0))
        ax.spines['bottom'].set_position(('data', 0.0))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        self.range1 = range1
        self.range2 = range2
        self.accuracy = accuracy

    def __del__(self):
        print('a')
        self.show()

    def func(self, function: string):
        x = np.arange(float(self.range1), float(self.range2) , float(self.accuracy))

        y = eval(function)

        plt.plot(x, y)

    def point(self, p: tuple):
        x, y = p
        plt.scatter(x,y)

    def line(self, p1 : tuple, p2 : tuple, show_points = True):
        """draws the straight line connects 2 points

        Parameters
        ----------
        p1 : tuple <x,y>
            First point of line with coordinates as a tuple of form (x,y).
        p2 : tuple <x,y>
            Second point of line with coordinates as a tuple of form (x,y).
        show_points : bool
            whether to mark the points on the line or not. Defaults to True.

        Returns
        -------
        None

        """
        x1, y1 = p1
        x2, y2 = p2
        if show_points:
            plt.scatter(x1,y1)
            plt.scatter(x2,y2)
        try:
            m = (y2-y1)/(x2-x1)
        except ZeroDivisionError:
            y = np.arange(float(self.range1), float(self.range2) , float(self.accuracy))
            x = np.full_like(y, x1)
        else:
            x = np.arange(float(self.range1), float(self.range2) , float(self.accuracy))
            y = m*(x-x1) + y1

        plt.plot(x, y)

    def linesegment(self, p1, p2, show_points = True):
        """Same as line() except it does not extend indefinitely.

        Parameters
        ----------
        p1 : tuple <x,y>
            First point of line with coordinates as a tuple of form (x,y).
        p2 : tuple <x,y>
            Second point of line with coordinates as a tuple of form (x,y).
        show_points : bool
            whether to mark the points on the line or not. Defaults to True.

        Returns
        -------
        None

        """
        x1, y1 = p1
        x2, y2 = p2

        if show_points:
            plt.scatter(x1,y1)
            plt.scatter(x2,y2)

        plt.plot([x1,x2],[y1,y2])

    def circle(self, r, cen : tuple = (0,0), show_centre = True):
        """Plots a circle with given radius

        Parameters
        ----------
        r : float
            Radius of Circle.
        cen : tuple <x,y>
            centre of circle with coordinates as a tuple of form (x,y). Defaults to the origin.
        show_centre : bool
            whether to plot the centre on the graph or not. Defaults to True.

        Returns
        -------
        None

        """
        h, k = cen

        if show_centre: plt.scatter(h,k)

        x = np.arange(float(self.range1), float(self.range2) , float(self.accuracy))

        root = np.sqrt(r**2-(x-h)**2)
        if np.isnan(root.all()):
            print("circle is not real")
            return 0

        y = root + k
        plt.plot(x, y)

        y = k - root
        plt.plot(x, y)

    def parabola(self, a=0.25, vertex = (0,0), vertical = True, is_positive = True, show_focus = True):
        """
        Plots a parabola.
        With no parameters, plots y = x**2.

        Parameters
        ----------
        a : float
            distance of focus from vertex. defaults to 0.25.
        vertex : tuple <x,y>
            Vertex of the parabola. Defaults to Origin.
        vertical : bool
            Describes the vertical orientation. True for upward facing, False for downward. Defaults to True.
        is_positive : type
            Describes the  orientation. True for vertical, False for horizontal. Defaults to True.
        show_focus : type
            whether to show the focus on the graph or not. Defaults to True.

        Returns
        -------
        None


        """
        h, k = vertex
        sign = (1 if is_positive else -1)
        if vertical:
            x = np.arange(float(self.range1), float(self.range2) , float(self.accuracy))
            y = 4*sign*a*((x-h)**2) + k
            focus = h, (k+a)
        else:
            y = np.arange(float(self.range1), float(self.range2) , float(self.accuracy))
            x = 4*sign*a*((y-k)**2) + h
            focus = (h+a),k
        x_f, y_f = focus
        if show_focus: plt.scatter(x_f,y_f)
        plt.plot(x,y)

    def eccentricity(a,b):
        """returns eccentricity of a conic with both axes given.

        Parameters
        ----------
        a : float
            length of horizontal axis.
        b : float
            length of vertical axis.

        Returns
        -------
        float

        """
        return np.sqrt(abs(1-(b/a**2)))

    def conic(self, a, e = 1, vertex = (0,0)):
        """Plots a conic section.

        Parameters
        ----------
        a : float
            length of horizontal axis
        e : float
            eccentricity. Defaults to 1.
        vertex : tuple <x,y>
            centre of conic section. Defaults to origin.

        Returns
        -------
        None

        """
        h, k = vertex
        if e == 1:
            self.parabola(a,vertex)
            return None
        x = np.arange(float(self.range1), float(self.range2) , float(self.accuracy))
        y = np.sqrt((a**2-(x-h)**2)*(1-e**2)) + k

        plt.plot(x,y)

        y = -(np.sqrt((a**2-(x-h)**2)*(1-e**2))) + k
        plt.plot(x,y)

    def polygon(*vertices):
        pass

    def clear(self):
        """clears the plot

        Returns
        -------
        None

        """
        fig = plt.figure()
        fig.clear(True)

    def show(self):
        """shows the plot.

        Returns
        -------
        None

        """
        plt.show()
