def to_cli_flag(v, *args, **kw):
    flag = list(v)[0]
    value = list(v.values())[0]
    
    def _cli_flag(flag):
        return f"--{flag}"

    if value is not None:
        if isinstance(value, list):
            return [f"{_cli_flag(flag)}={str(v)}" for v in value]
        return f"{_cli_flag(flag)}={str(value)}"
    return f"{_cli_flag(flag)}"


class FilterModule(object):
    filter_map = {
        'cliflag': to_cli_flag,
    }

    def filters(self):
        return self.filter_map
