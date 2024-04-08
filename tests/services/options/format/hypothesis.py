from hypothesis import strategies as st

lists_of_dicts = st.lists(
    st.dictionaries(
        keys=st.text().filter(lambda x: x != "" and x.isalnum),
        values=st.one_of(st.text().filter(lambda x: x != "" and x.isalnum), st.floats()),
        min_size=1,
        max_size=5,
    ),
    min_size=1,
    max_size=5,
)
