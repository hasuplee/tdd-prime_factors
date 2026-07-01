import pytest
from prime_factors import PrimeFactor

def test_prime():
    prime_factor = PrimeFactor()
    assert prime_factor.of(1) == []