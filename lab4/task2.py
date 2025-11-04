"""Centimeters to inches converter.

Provides `convert_cm_to_inches(cm) -> float` with simple input validation,
one-line tests and a small `__main__` demo.
"""

def convert_cm_to_inches(cm) -> float:
    """Convert centimeters to inches.

    Parameters
    ----------
    cm : int | float
        Length in centimeters.

    Returns
    -------
    float
        Length in inches.

    Raises
    ------
    TypeError
        If `cm` is not a number (int or float).
    """
    if not isinstance(cm, (int, float)):
        raise TypeError("cm must be a number (int or float)")
    return cm / 2.54


def _quick_tests():
    # exact conversion for the canonical example
    assert convert_cm_to_inches(2.54) == 1.0
    # zero
    assert convert_cm_to_inches(0) == 0.0
    # float input
    assert abs(convert_cm_to_inches(5.08) - 2.0) < 1e-12


if __name__ == "__main__":
    _quick_tests()
    print("All quick tests passed for convert_cm_to_inches().")
    samples = [2.54, 10.0, 30.48]
    for cm in samples:
        inches = convert_cm_to_inches(cm)
        print(f"{cm} cm -> {inches} in")

                                            