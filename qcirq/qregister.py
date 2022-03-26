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
        qbits = np.log2(len(state))
        norm = np.linalg.norm(state, 2)
        max_norm_deviation = 1e-9
        assert 1.0 - max_norm_deviation <= norm <= 1.0 + max_norm_deviation, \
                                                            "not normalized"
        assert qbits == int(qbits), "len(state) should be 2**N"
        assert 0 < qbits <= max_qbits, "too many qbits"

        self.qbits = int(qbits)
        self.state = state

    def inspect_entanglement(self):
        """
        Inspects in beween which bits the register is separable.
        
        Returns
        -------
        separable: np.ndarray(bool)
            if separable[i] is True, then the register is separable in between
            qbit i and i+1
            if separable[i] is False, then the register containing qbits 
            0 to i and the register containing qbits i+1 to n are entangled
        """
        #TODO docs
        separable = np.zeros(self.qbits-1)
        register = self.state.copy()

        if self.qbits == 1:
            return False

        for i in range(1, self.qbits):
            m = register.reshape(2**i, int(len(register)/(2**i)))
            rank = np.linalg.matrix_rank(m)
            separable[i-1] = not (rank > 1)

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