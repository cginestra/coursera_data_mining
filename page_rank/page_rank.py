__author__ = 'carlos.ginestra'

import numpy
from numpy.linalg import norm

class PageRank():

    @staticmethod
    def calculate_PR_from_M(M, beta):
        maxiter=1000
        tol = 0.01
        Nrows = M.shape[0]
        Ncols = M.shape[1]
        rold = numpy.ones((Nrows,1)) #/Nrows
        r0 = numpy.ones((Nrows,1))/Nrows

        for i in xrange(maxiter):
            r = beta * M * rold + (1-beta) * r0
            print "Iteration " + str(i)
            print r
            dif = norm(r-rold)
            # print dif
            if dif < tol:
                return r
            rold = r

        print "Max iterations reached"
        return r

    @staticmethod
    def check_M(M):
        col_sum = numpy.sum(M,axis=0)
        if (col_sum == numpy.ones(M.shape[0])).all():
            return True
        else:
            print("Invalid matrix M")
            raise BaseException

if __name__ == "__main__":

    M = numpy.matrix([[0., 0., 1],[1/2., 0, 0],[1/2., 1, 0]])
    print M
    PageRank.check_M(M)
    beta = 1
    escala = 1

    solution = PageRank.calculate_PR_from_M(M, beta)
    solution = escala*solution
    print "Limit solution:"
    print solution

