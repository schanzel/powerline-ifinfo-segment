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
