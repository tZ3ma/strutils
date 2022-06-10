# tests/test_api.py
"""Test core API."""
import pytest

import strutils


# -------------- strutils.sos_on ------------------
@pytest.mark.parametrize(
    ("cstring", "using", "expected_result"),
    [
        (
            "variable_cost",
            str.capitalize,
            [
                "variable_cost",
                "variable_Cost",
                "Variable_cost",
                "Variable_Cost",
            ],
        ),
    ],
)
def test_sos_on(cstring, using, expected_result):
    """Test correct strutils.sos_on functionaility."""
    assert list(strutils.sos_on(cstring, using)) == expected_result


# -------------- strutils.premute_splits ------------------
@pytest.mark.parametrize(
    ("strings", "stitch_with", "split_at", "expected_result"),
    [
        (
            ["variable_cost", "Variable_cost"],
            "_",
            "_",
            [
                "variable_cost",
                "cost_variable",
                "Variable_cost",
                "cost_Variable",
            ],
        ),  # test use case behaviour
        (
            "variable_cost",
            "_",
            "_",
            [
                "variable_cost",
                "cost_variable",
            ],
        ),  # test one compound string behaviour
        (
            "variable",
            "_",
            "_",
            [
                "variable",
            ],
        ),  # test one NON-compound string behaviour
    ],
)
def test_permute_splits(strings, stitch_with, split_at, expected_result):
    """Test correct strutils.sos_on functionaility."""
    permuted_splits = strutils.permute_splits(strings, stitch_with, split_at)
    assert list(permuted_splits) == expected_result


# -------------- strutils.variate_compounds ------------------
@pytest.mark.parametrize(
    (
        "cstring",
        "using",
        "permutate",
        "split_at",
        "stitch_with",
        "expected_result",
    ),
    [
        (
            "variable_cost",
            str.capitalize,
            True,
            "_",
            "_",
            [
                "variable_cost",
                "cost_variable",
                "variable_Cost",
                "Cost_variable",
                "Variable_cost",
                "cost_Variable",
                "Variable_Cost",
                "Cost_Variable",
            ],
        ),  # test design case
        (
            "variable_cost",
            str.capitalize,
            False,
            "_",
            "_",
            [
                "variable_cost",
                "variable_Cost",
                "Variable_cost",
                "Variable_Cost",
            ],
        ),  # test not permutating
    ],
)
def test_variate_compounds(
    cstring,
    using,
    permutate,
    split_at,
    stitch_with,
    expected_result,
):
    """Test correct strutils.variate_compounds functionaility."""
    # pylint: disable=too-many-arguments
    variated_compounds = strutils.variate_compounds(
        cstring,
        using,
        permutate,
        split_at,
        stitch_with,
    )

    assert list(variated_compounds) == expected_result
