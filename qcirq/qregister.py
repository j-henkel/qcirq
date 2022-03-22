import numpy as np


class QRegister:
    #TODO docs
    
    def __init__(self, state: np.ndarray):
        max_qbits = 10
        state = state
        #TODO make sure state is of dim 2**n, n<10
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