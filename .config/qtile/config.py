# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os


@hook.subscribe.client_new
def make_window_floating_by_title(window):
    floating_titles = ["calc", "volume", "popup-term"]
    if window.name in floating_titles:
        window.toggle_floating()
        window.set_size_floating(1024, 720)


# Wrapper for lsp
def get_terminal() -> str:
    term = guess_terminal()
    return "alacritty" if term is None else term


mod = "mod4"
browser = os.environ.get("BROWSER", "firefox")
terminal = os.environ.get("TERMINAL", get_terminal())


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch focus between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod],
        "tab",
        lazy.group.focus_back(),
        desc="Move focus to previously focused window",
    ),
    # Switch between groups
    Key([mod], "i", lazy.screen.prev_group(), desc="Switch to group on the left"),
    Key([mod], "o", lazy.screen.next_group(), desc="Switch to group on the right"),
    # Switch focus between screens
    Key([mod], "Left", lazy.prev_screen(), desc="Switch to previous screen"),
    Key([mod], "Right", lazy.next_screen(), desc="Switch to next screen"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # For floating layouts: next and previous window
    Key(
        [mod, "control"], "p", lazy.group.prev_window(), desc="Previous window in group"
    ),
    Key([mod, "control"], "n", lazy.group.next_window(), desc="Next window in group"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key( [mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    # Toggle between different layouts as defined below
    Key([mod], "u", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    # Root methods
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # MPC commands
    Key(
        [mod],
        "p",
        lazy.spawn("mpc toggle"),
        desc="MPC play/pause",
    ),
    Key(
        [mod],
        "bracketleft",
        lazy.spawn("mpc seek -10"),
        desc="Backwards 10 sec",
    ),
    Key(
        [mod],
        "bracketright",
        lazy.spawn("mpc seek +10"),
        desc="Forward 10 sec",
    ),
    Key(
        [mod],
        "comma",
        lazy.spawn("mpc prev"),
        desc="Previous song",
    ),
    Key(
        [mod, "shift"],
        "comma",
        lazy.spawn("mpc seek 0%"),
        desc="Jump to beginning of song",
    ),
    Key(
        [mod],
        "period",
        lazy.spawn("mpc next"),
        desc="Next song",
    ),
    # Volume control commands
    Key(
        [mod],
        "minus",
        lazy.spawn("wpctl set-volume @DEFAULT_SINK@ 0.01-"),
        desc="-1 volume",
    ),
    Key(
        [mod, "shift"],
        "minus",
        lazy.spawn("wpctl set-volume @DEFAULT_SINK@ 0.1-"),
        desc="-10 volume",
    ),
    Key(
        [mod],
        "equal",
        lazy.spawn("wpctl set-volume @DEFAULT_SINK@ 0.01+"),
        desc="+1 volume",
    ),
    Key(
        [mod, "shift"],
        "equal",
        lazy.spawn("wpctl set-volume @DEFAULT_SINK@ 0.1+"),
        desc="+10 volume",
    ),
    Key(
        [mod, "shift"],
        "m",
        lazy.spawn("wpctl set-mute @DEFAULT_SINK@ toggle"),
        desc="Toggle sink mute",
    ),
    Key(
        [mod],
        "F9",
        lazy.spawn("wpctl set-mute @DEFAULT_SOURCE@ toggle"),
        desc="Toggle source mute",
    ),
    # Keyboard Layout
    Key(
        [mod],
        "F12",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout.",
    ),
    # Program spawning
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn(terminal + " --title popup-term"),
        desc="Launch terminal",
    ),
    Key([mod], "backspace", lazy.spawn("sysact")),
    Key(
        [mod], "d", lazy.spawn("rofi -show-icons -monitor -1 -show  drun"), desc="drun"
    ),
    Key(
        [mod, "shift"],
        "d",
        lazy.spawn("rofi -show-icons -monitor -1 -show run"),
        desc="run",
    ),
    Key([mod], "m", lazy.spawn(terminal + " -e ncmpcpp")),
    Key([mod], "r", lazy.spawn(terminal + " -e lf")),
    Key([mod, "shift"], "r", lazy.spawn(terminal + " -e htop")),
    Key(
        [mod], "s", lazy.spawn("rofi -show-icons -show window"), desc="Window Switcher"
    ),
    Key([mod], "w", lazy.spawn(browser), desc="Run browser"),
    Key(
        [mod, "shift"],
        "w",
        lazy.spawn(terminal + " -e nmtui"),
        desc="Run Network Manager TUI",
    ),
    KeyChord(
        [mod],
        "x",
        [
            Key([mod], "c", lazy.spawn("localc"), desc="Run Libreoffice Calc"),
            Key(
                [mod], "e", lazy.spawn("emacsclient -c"), desc="Run emacsclient connect"
            ),
            Key([mod], "n", lazy.spawn("neovide"), desc="Run Neovide"),
            Key([mod], "r", lazy.spawn("dolphin"), desc="Run GUI file manager"),
            Key([mod], "w", lazy.spawn("brave"), desc="Run Brave Browser"),
            Key([mod], "x", lazy.spawn("xournalpp"), desc="Run Xournal++"),
        ],
    ),
    Key([mod], "backslash", lazy.spawn(terminal + " --title='calc' -e 'python'")),
    Key([mod], "F4", lazy.spawn(terminal + " --title='volume' -e 'pulsemixer'")),
    Key([], "Print", lazy.spawn("grimss cb")),
    Key([mod], "Print", lazy.spawn("grimss")),
]

group_labels = ["1", "2", "3", "4", "5", "GAME", "VM", "CHAT", "🎶"]
groups = [Group(i, label=group_labels[int(i) - 1]) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key(
            [mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name),
        ),
        # mod1 + shift + letter of group = move focused window to group
        Key(
            [mod, "shift"],
            i.name,
            lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name),
        ),
    ])

catppuccin_frappe = [
    ["#303446", "#303446"],  # bg
    ["#c6d0f5", "#c6d0f5"],  # fg
    ["#e78284", "#e78284"],  # color01 red
    ["#a6d189", "#a6d189"],  # color02 green
    ["#e5c890", "#e5c890"],  # color03 yellow
    ["#8caaee", "#8caaee"],  # color04 blue
    ["#f4b8e4", "#f4b8e4"],  # color05 magenta
    ["#81c8be", "#81c8be"],  # color06 cyan
    ["#a5adce", "#a5adce"],  # color15 white
]

colors = catppuccin_frappe

layout_theme = {
    "border_width": 6,
    "margin": 0,
    "border_focus": colors[1],
    "border_normal": colors[0],
    "border_on_single": True,
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]


widget_defaults = dict(
    font="monospace bold",
    fontsize=10,
    foreground=colors[1][0],
)

extension_defaults = widget_defaults


def init_widgs(is_main=False):
    spacer = widget.Spacer(length=8)

    widgs = [
        spacer,
        widget.CurrentLayout(),
        spacer,
        widget.GroupBox(
            disable_drag=True,
            use_mouse_wheel=False,
            hide_unused=True,
            active=colors[1],
            this_current_screen_border=colors[1],
            urgent_border=colors[2],
        ),
        spacer,
        widget.TaskList(
            border=colors[1],
            urgent_border=colors[2],
            icon_size=16,
            margin=6,
        ),
        spacer,
        widget.CPU(
            format="🔲 {load_percent}%",
        ),
        spacer,
        widget.Memory(
            fmt="💾{}",
        ),
        spacer,
        widget.DF(
            warn_color=colors[2],
            fmt="󰆼 {}",
            visible_on_warn=False,
        ),
        spacer,
        widget.KeyboardLayout(
            configured_keyboards=["us", "es"],
            fmt="⌨ {}",
        ),
        spacer,
        widget.Volume(
            get_volume_command="pamixer --get-volume-human",
            fmt="🔉 {}",
        ),
        spacer,
        widget.Clock(
            format="🗓️ %a %m/%d 🕓 %I:%M:%S",
        ),
        spacer,
    ]

    if os.environ.get("BATTERY_AVAILABLE"):
        battery_widget = widget.Battery(
            format="{char} {percent:2.0%}",
            show_short_text=False,
            empty_char="🪫",
            discharge_char="🔋",
            charge_char="🔌",
            full_char="⚡",
        )
        widgs.insert(-2, battery_widget)

    # Only add systray on main screen
    if is_main:
        systray = widget.Systray()
        widgs.insert(-1, systray)

    return widgs


screens = [
    Screen(
        top=bar.Bar(
            widgets=init_widgs(is_main=True),
            size=32,
            # margin=4,
            background=colors[0][0],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "urgent"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
