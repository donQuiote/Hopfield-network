import numpy as np
from Main_classes import Utilities as ut

Ut = ut.Utilities()

class HopfieldNetwork:
    """
    @class: HopfieldNetwork modelizes a Hopfield network from a set of patterns and a given learning rule.
    @note: The learning rules accepted are 'hebbian' and 'storkey'.
    """

    def __init__(self, patterns, rule='hebbian'):
        """
        @note: Two attributes are given to the HopfieldNetwork object upon initialization: patterns and weights
        """
        self.rule = rule
        self.size = np.shape(patterns) #(M,N)
        self.patterns = patterns
        if rule == 'hebbian':
            self.weights = self.hebbian_weights(patterns)
        elif rule == 'storkey':
            self.weights = self.storkey_weights(patterns)
        else:
            raise NameError("The possible rules are only 'hebbian' or 'storkey'")

    def hebbian_weights(self, patterns):
        """
        @summary: hebbian_weights executes the hebbian rule to the patterns received creating the weight matrix of the patterns
        @param patterns: a matrix where each row represents a pattern (array)
        @return: the weight matrix of the patterns the matrix is the size of the row
        @note: is optimized through the fact that this matrix is symmetric
        """
        if not np.all([[y == 1 or y == -1 for y in a_pattern] for a_pattern in patterns]):
            raise ValueError("the patterns do not have all of their elements equal to 1 or -1")
        Pattern_matrix = np.zeros((self.size[1], self.size[1]))
        for i in range(self.size[0]):
            Pattern_matrix += np.outer(patterns[i], patterns[i])
        return (1.0/self.size[0])*Pattern_matrix - np.diag(np.ones(self.size[1]))

    def storkey_weights(self, patterns):
        """
        @summary: storkey_weights executes the storkey rule to the patterns received creating the weight matrix of the patterns
        @param patterns: A pattern in the form of an array.
        @return: The weights matrix of connections computed according to the Storkey rule.
        """
        if not np.all([[y == 1 or y == -1 for y in a_pattern] for a_pattern in patterns]):
            raise ValueError("the patterns do not have all of their elements equal to 1 or -1")
        W = np.zeros((self.size[1], self.size[1]))
        inverse_n = 1.0 / self.size[1]
        for u in range(self.size[0]):
            pattern_u = patterns[u]
            diag_W = np.diag(W).copy()
            # test the three next lines with the commented line
            # use np fill to take the diag out
            H = np.zeros((self.size[1], self.size[1]))
            H += np.reshape(np.dot(W,pattern_u)-diag_W*pattern_u,(self.size[1],1))
            H -= W*pattern_u - np.diag(diag_W)*pattern_u
            # compute the new weight matrix for the u th pattern
            W = (W + inverse_n * (np.outer(pattern_u, pattern_u) - H * pattern_u - np.transpose(H * pattern_u))).copy()
        return W

    def update(self, state):
        """
        @summary: update updates a given state through the update rule, using the weights matrix
        @param state: a pattern (array)
        @return: the updated state (array)
        @note: perhaps faster with the lambda???
        """
        return np.array([Ut.sigma_function(y) for y in (np.dot(self.weights, state))])

    def update_async(self, state):
        """
        @summary: update_async updates one of the components of a given state
        @param state: a pattern (array)
        @return: the same pattern with only one component altered (array)
        @note : copy needed since we want to modify the received state
        """
        cp_state = state.copy()
        x = np.random.randint(0, self.size[1])
        cp_state[x] = Ut.sigma_function((np.dot(self.weights[x], cp_state)))
        return cp_state

    def dynamics(self, state, saver, max_iter=20):
        """
        @summary: dynamics runs the dynamical system from an initial state until convergence or max steps
                using the update function.
        @param state: a pattern (array)
        @param weights: a square matrix (array of array) of same size as the state
        @param max_iter: the maximum number of iteration the function is going to do (int)
        @note: uses update()
        """
        current_state = state.copy()
        iter = 0
        previous_state = np.zeros(self.size[1])
        while iter < max_iter and np.any(current_state != previous_state):
            previous_state = current_state.copy()
            saver.store_iter(current_state, self.weights)
            current_state = self.update(current_state)
            iter += 1

    def dynamics_async(self, state, saver, max_iter=1000, convergence_num_iter=100, skip=10):
        """
        @summary: dynamics_async runs the dynamical system from an initial state until max steps reached
                using the update_async function. This function iterates on one component at a time.
        @param state: a pattern (array)
        @param weights: a square matrix (array of array) of same size as the state
        @param max_iter: the maximum number of iteration the function is going to do (int) if this number is reached the
                                    function stops
        @param convergence_num_iter: the number of time the states must not change (int) if this number is reached the
                                    function stops
        @note: uses update_async()
        """
        current_state = state.copy()
        convergence_streak = 0
        last_converged = False
        i = 0
        while i < max_iter and convergence_num_iter > convergence_streak:
            previous_state = current_state.copy()
            if i % skip == 0:
                 saver.store_iter(current_state, self.weights)
            current_state = self.update_async(current_state)
            if last_converged:
                if np.array_equal(current_state,previous_state):
                    convergence_streak += 1
                else:
                    convergence_streak = 0
                    last_converged = False
            elif np.array_equal(current_state,previous_state):
                last_converged = True
                convergence_streak += 1
            i += 1

    def reset_patterns(self, pattern_index, pattern):
        if pattern_index < 0 or pattern_index >= self.size[0]:
            raise IndexError("The index isn't possible, values can't be negative nor exceed the size of the patterns")
        elif len(pattern) != self.size[1]:
            raise ValueError("The length of the given pattern isn't correct, it has to be the same size as the number of columns in the patterns")
        else:
            self.patterns[pattern_index] = pattern.copy()
            self.__init__(self.patterns, self.rule)

    def __del__(self):
        del self
