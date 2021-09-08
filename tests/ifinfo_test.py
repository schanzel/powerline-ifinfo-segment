from unittest.mock import patch

from powerline_ifinfo import ifinfo


@patch("ifcfg.interfaces")
def test_interface_up(mock_interfaces):
    mock_interfaces.return_value = {
        "en0": {
            "device": "en0",
            "status": "active",
        }
    }
    result = ifinfo.interface_up(None, "en0")
    assert [{"contents": "en0 is up"}] == result

    mock_interfaces.return_value = {
        "en0": {
            "device": "en0",
            "flags": "8863<up,broadcast,smart,running,simplex,multicast>",
        }
    }
    result = ifinfo.interface_up(None, "en0")
    assert [{"contents": "en0 is up"}] == result

    mock_interfaces.return_value = {
        "en0": {
            "device": "en0",
        }
    }
    result = ifinfo.interface_up(None, "en0")
    assert [{"contents": "en0 is down"}] == result

    mock_interfaces.return_value = {
        "en0": {
            "device": "en0",
            "status": "active",
            "foo": "bar"
        }
    }
    result = ifinfo.interface_up(
        None,
        "en0",
        interface_up="{device} {status} {foo}")
    assert [{"contents": "en0 active bar"}] == result

    mock_interfaces.return_value = {
        "en0": {
            "device": "en0",
            "status": "inactive",
            "foo": "bar"
        }
    }
    result = ifinfo.interface_up(
        None,
        "en0",
        interface_down="{device} {status} {foo}")
    assert [{"contents": "en0 inactive bar"}] == result


@patch("ifcfg.default_interface")
def test_default_interface(mock_interface):
    mock_interface.return_value = {
        "device": "en0",
        "status": "up",
        "foo": "bar"
    }

    result = ifinfo.default_interface(None)
    assert [{"contents": "en0 is up"}] == result

    result = ifinfo.default_interface(None, format="{device} {status} {foo}")
    assert [{"contents": "en0 up bar"}] == result
