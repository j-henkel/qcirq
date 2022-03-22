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

