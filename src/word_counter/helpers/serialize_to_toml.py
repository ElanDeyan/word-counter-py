import toml


def format_to_toml(data_to_dump: list[dict[str, object]]) -> str:
    wrapped_data = {"data": data_to_dump}

    return toml.dumps(wrapped_data)
