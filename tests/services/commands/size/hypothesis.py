from hypothesis import strategies as st

all_size_units = [
    "b",
    "B",
    "kb",
    "kB",
    "Kb",
    "KB",
    "mb",
    "mB",
    "Mb",
    "MB",
    "gb",
    "gB",
    "Gb",
    "GB",
    "tb",
    "tB",
    "Tb",
    "TB",
]

valid_size_units = st.sampled_from(all_size_units)

invalid_size_units = st.text().filter(lambda x: x not in all_size_units)

size_unit_test_cases = st.one_of(valid_size_units, invalid_size_units)
