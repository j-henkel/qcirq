import numpy as np
from ..qregister import QRegister
import pytest


class TestQRegister:

    def test_init_raise_exception(self):
        with pytest.raises(AssertionError):
            x = QRegister(np.array([1, 0, 0]))
        with pytest.raises(AssertionError):
            state = np.zeros(2**11)
            state[0] = 1
            x = QRegister(state)
        for i in range(1, 11):
            state = np.zeros(2**i)
            state[0] = 1
            try:
                x = QRegister(state)
            except AssertionError:
                assert False
        with pytest.raises(AssertionError):
            x = QRegister(np.array([2, 1]))
        try: 
            s = 1/np.sqrt(2)
            x = QRegister(np.array([s, s]))
        except AssertionError:
            assert False

    def test_entanglement(self):
        #TODO edge cases like one single qbit
        isqr2 = 1/np.sqrt(2)
        entangled2 = np.array([isqr2, 0, 0, isqr2])
        unentangled = np.array([isqr2, isqr2])
        qreg = QRegister(entangled2)
        result = qreg.inspect_entanglement()
        assert (result == np.array([False])).all()
        qreg = QRegister(np.kron(entangled2, unentangled))
        result = qreg.inspect_entanglement()
        assert (result == np.array([False, True])).all()
        qreg = QRegister(np.kron(entangled2, entangled2))
        result = qreg.inspect_entanglement()
        assert (result == np.array([False, True, False])).all()
        qreg = QRegister(np.kron(unentangled, entangled2))
        result = qreg.inspect_entanglement()
        assert (result == np.array([True, False])).all()
        x = np.kron(entangled2, unentangled)
        x = np.kron(x, entangled2)
        qreg = QRegister(x)
        result = qreg.inspect_entanglement()
        assert (result == np.array([False, True, True, False])).all()
