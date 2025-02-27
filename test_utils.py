import pytest
import utils

def test_fact():
    assert utils.fact(5)==120

def test_roots():
    assert utils.roots(1,0,1)==None

def test_integrate():
    assert utils.integrate('x ** 2 - 1', -1, 1)==-1.3333333333333335
