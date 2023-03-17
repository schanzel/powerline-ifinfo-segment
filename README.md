# powerline-ifinfo-segment

A Powerline Segment to Display Network Interface Infos

## Installation

```sh
pip install powerline-ifinfo-segment
```

## Configuration

Define colorschemes to your liking

```
# colorschemes/default.json
{
  "groups": {
    "interface_up":      { "fg": "gray8", "bg": "gray0", "attrs": [] },
    "default_interface": { "fg": "gray8", "bg": "gray0", "attrs": [] },
    ...
}
```

Indicating if a certain interface is up

```
# themes/tmux/default.json
{
  "segments": {
    "right": [
      {
        "function": "powerline_ifinfo.ifinfo.interface_up",
        "args": {
          "interface": "utun3",
          "interface_up": "VPN Up",
          "interface_down": null
        }
      },
      ...
    ]
  }
}
```

Show the current default interface

```
# themes/tmux/default.json
{
  "segments": {
    "right": [
      {
        "function": "powerline_ifinfo.ifinfo.default_interface",
        "args": {
          "format": "{device}"
        }
      },
      ...
    ]
  }
}
```
