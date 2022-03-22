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

        self.qbits = qbits
        self.state = state

        return

    def inspect_entanglement(self):
        """check wether the register is entangled"""
        #TODO implement test_for_entanglement()
        return

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