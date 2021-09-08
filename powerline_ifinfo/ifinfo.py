import ifcfg


def interface_up(
    pl,
    interface,
    interface_up="{device} is up",
    interface_down="{device} is down",
):
    interface = ifcfg.interfaces().get(interface, {})
    is_up = (
        interface.get("status", "inactive") == "active" or
        "up" in interface.get("flags", "")
    )

    if is_up:
        contents = interface_up.format(**interface)
    else:
        contents = interface_down.format(**interface)

    return [{
        "contents": contents,
    }]


def default_interface(pl, format="{device} is {status}"):
    interface = ifcfg.default_interface()
    contents = format.format(**interface)

    return [{
        "contents": contents,
    }]
