import numpy

__author__ = 'carlos.ginestra'

class MinHash():

    @staticmethod
    def calculate_signature_matrix(input_matrix, hash_functions):
        """

        :param input_matrix: numpy matrix
        :return:
        """
        signature_matrix = 1000*numpy.ones((len(hash_functions),input_matrix.shape[1]))

        for r_ind, row in enumerate(input_matrix):
            hash_row = []
            for hash in hash_functions:
                hash_row.append(hash(r_ind+1))
            for c_ind, column in enumerate(row.getA1()):
                if column == 1:
                    for hash_ind, hash in enumerate(hash_row):
                        if hash < signature_matrix[hash_ind, c_ind]:
                            signature_matrix[hash_ind, c_ind] = hash

        return signature_matrix


if __name__ == "__main__":

    def hash_1(x):
        return x % 5

    def hash_2(x):
        return (2*x + 1) % 5

    input_M = numpy.matrix([[1,0],[0,1],[1,1],[1,0],[0,1]])


    signature = MinHash.calculate_signature_matrix(input_M, [hash_1, hash_2])
    print signature