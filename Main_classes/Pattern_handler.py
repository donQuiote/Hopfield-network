import numpy as np
import random as rd
import math

class Pattern_handler:
    """
    @class: This class can generate patterns of different sizes and can modify them
    @note: This object isn't a number of patterns but rather an interface to interact with them
    """
    def generate_patterns(self,num_patterns, pattern_size):
        """
        @summary: generate_patterns generates a given number of random patterns(arrays of -1 or +1) and stores them inside a matrix
        @param num_patterns: takes an int as the number of random patterns it is going to create
        @param pattern_size: takes an int as the length of one pattern
        @return : a matrix composed of num_patterns rows and each one is composed of
                    a random pattern (array of -1 or +1) of length pattern_size
        """
        if num_patterns < 0 or pattern_size < 0:
            raise ValueError("num_patterns and pattern_size must be >= 0")
        if math.floor(num_patterns) != num_patterns or math.floor(pattern_size) != pattern_size:
            raise ValueError("pattern_size and num_pattern must be exact integers")
        if num_patterns +1 == num_patterns or pattern_size +1 == pattern_size: # catches a value like 1e300
            raise OverflowError("pattern_size and/or num_pattern is too large")
        return np.random.choice([1, -1], size = (num_patterns,pattern_size))



    def perturb_pattern(self, pattern, num_perturb):
        """
        @summary: perturb_pattern randomly changes a given number of components from a given pattern
        @param pattern: takes an array containing -1 or 1 (the pattern)
        @param num_perturb: takes an int as the number of components from the pattern that are going to change
        @return: returns the same array (pattern) with some of its component changed (-1 become 1 and vice versa)
        @note: Never returns twice the same value with rd.sample(range())
        """
        x = rd.sample(range(np.size(pattern)), num_perturb)
        perturbed_pattern = pattern.copy()
        for i in x:
            perturbed_pattern[i] = -perturbed_pattern[i]
        return perturbed_pattern

    def pattern_match(self, memorized_patterns, pattern):
        """
        @summary: pattern_match computes whether the given matrix contains the same given pattern
        @param memorized_patterns: matrix of patterns (array of array)
                    each row represents a pattern
        @param pattern: an array of same size as the number of columns if memorized patterns
        @return: the row of the memorized_patterns containing the corresponding pattern otherwise returns none
        """
        if not np.all([[y == 1 or y == -1 for y in a_pattern] for a_pattern in memorized_patterns]):
            raise ValueError("the memorized_patterns do not have all of their elements equal to 1 or -1")
        M = np.shape(memorized_patterns)[0]
        for i in range(M):
            if np.all(memorized_patterns[i] == pattern):
                return i

    def random_indexer(self, num_patterns):
        """
        @summary: Produces a random index
        @param num_patterns: an integer
        @return: a random number between 0 and num_patterns
        @note: should we test if index is bigger than 0
        """
        return np.random.randint(0, num_patterns)

    def chekerboard_generator(self):
        # creates a checkerboard
        part_line = np.ones(5)
        part_line = np.concatenate((part_line, -part_line))
        line = np.tile(part_line, 25)
        two_line = np.append(line, -line)
        return np.tile(two_line, 5)



