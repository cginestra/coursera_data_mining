import itertools
import numpy

__author__ = 'carlos.ginestra'


class Distances():

    @staticmethod
    def dist_between_points(point1, point2 ,dist_definition):

        if dist_definition == "l1":
            dist = 0
            for item1, item2 in itertools.izip(point1,point2):
                dist += abs(item1 - item2)
            return dist

        if dist_definition == "l2":
            dist = 0
            for item1, item2 in itertools.izip(point1,point2):
                dist += (item1 - item2)*(item1 - item2)
            return numpy.math.sqrt(dist)



    @staticmethod
    def nn_cluster(point,dist_definition):
        dist_to_0_0 = Distances.dist_between_points(point, (0,0), dist_definition)
        dist_to_10_400 = Distances.dist_between_points(point, (100,40), dist_definition)

        if dist_to_0_0 < dist_to_10_400:
            return 0
        elif dist_to_0_0 > dist_to_10_400:
            return 1
        else:
            return 2




if __name__ == "__main__":

    dist_def = ["l1","l2"]
    points = [(66,5), (52,13), (50,18), (57,5)]

    for point in points:
        for dist in dist_def:
            print point,
            print dist,
            print ": ",
            print Distances.nn_cluster(point, dist)