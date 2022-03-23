import numpy as np


class QRegister:
    #TODO docs
    
    def __init__(self, state: np.ndarray):
        """
        Parameters
        ----------
        state: np.ndarray
            An array containing the measurement probabilities of the base
            states
        """

        max_qbits = 10
        qbits = int(np.log2(len(state)))
        norm = np.linalg.norm(state, 2)
        max_norm_deviation = 1e-9
        assert 1.0 - max_norm_deviation <= norm <= 1.0 + max_norm_deviation, \
                                                            "not normalized"
        assert qbits == int(qbits), "len(state) should be 2**N"
        assert 0 < qbits <= max_qbits, "too many qbits"

        self.qbits = qbits
        self.state = state

        return

    def inspect_entanglement(self):
        """check wether the register is entangled"""
        separable = np.zeros(self.qbits-1)
        register = self.state.copy()

        for i in range(1, self.qbits):
            m = register.reshape(2**i, int(len(register)/(2**i)))
            rank = np.linalg.matrix_rank(m)
            separable[i-1] = not (rank > 1)

        # might struggle with rounding of last digit of float numbers 
        # for example 0.99999999999999 instead of 1.0
        return separable

    def separate(self):
        """if the register is not entangled return the states of the single
        qbits. Or reduce as far as possible?
        """
        #TODO implement separate()
        return

    def measure(self):
        """measure the register with respect to a base"""
        #TODO implement measure()
        return

    def change_of_basis(self):
        """change the basis of the register"""
        #TODO implement change_of_basis()
        return

    def merge(self, reg):
        """return the kronecker tensor product of self and reg"""
        #TODO implement merge()
        return

    def normalize(self):
        """normalize the register"""
        #TODO implement normalize()
        return