from click.exceptions import BadParameter
from hypothesis import given
import pytest

from src.word_counter.services.commands.size.size_unit_from_str import (
    size_unit_from_str,
)
from src.word_counter.utils.SizeUnits import SizeUnit
from .hypothesis import valid_size_units, invalid_size_units


@given(test_case=invalid_size_units)
def test_size_unit_from_str_raises(test_case: str):
    with pytest.raises(BadParameter):
        assert isinstance(size_unit_from_str(test_case), SizeUnit)


@given(test_case=valid_size_units)
def test_size_unit_from_str_ok(test_case: str):
    assert isinstance(size_unit_from_str(test_case), SizeUnit)
