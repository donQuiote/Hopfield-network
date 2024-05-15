import numpy as np
import Utilities as ut
import random as rd
import timeit
import math


def generate_patterns(num_patterns, pattern_size):
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
    return np.reshape(np.random.choice([1, -1], size = (num_patterns,pattern_size)),(num_patterns,pattern_size))


def perturb_pattern(pattern, num_perturb):
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


def pattern_match(memorized_patterns, pattern):
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


def dynamics(state, weights, max_iter):
    """
    @summary: dynamics runs the dynamical system from an initial state until convergence or max steps
            using the update function.
    @param state: a pattern (array)
    @param weights: a square matrix (array of array) of same size as the state
    @param max_iter: the maximum number of iteration the function is going to do (int)
    @return: a list composed of each pattern (array) the state went through each time it got updated
    @note: uses update()
    @note: creates a copy of the received state otherwise it is modified during the process
    """
    state_history = []
    current_state = state.copy()
    iter = 0
    previous_state = np.zeros(np.size(current_state))
    while iter < max_iter and np.any(current_state != previous_state):
        previous_state = current_state.copy()
        state_history.append(current_state)
        current_state = update(current_state, weights)
        iter += 1
    return state_history


def dynamics_async(state, weights, max_iter, convergence_num_iter):
    """
    @summary: dynamics_async runs the dynamical system from an initial state until max steps reached
            using the update_async function. This function iterates on one component at a time.
    @param state: a pattern (array)
    @param weights: a square matrix (array of array) of same size as the state
    @param max_iter: the maximum number of iteration the function is going to do (int) if this number is reached the
                                function stops
    @param convergence_num_iter: the number of time the states must not change (int) if this number is reached the
                                function stops
    @return: a list composed of each pattern (array) the state went through each time it got updated
    @note: uses update_async()
    """
    current_state = state.copy()
    state_history = []
    convergence_streak = 0
    last_converged = False
    for i in range(max_iter):
        previous_state = current_state.copy()
        state_history.append(current_state)
        current_state = update_async(current_state, weights)
        if last_converged:
            if np.all(current_state == previous_state):
                convergence_streak += 1
            else:
                convergence_streak = 0
                last_converged = False
        elif np.all(current_state == previous_state):
            last_converged = True
            convergence_streak += 1
        if convergence_num_iter == convergence_streak:
            return state_history
    return state_history
