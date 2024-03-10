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

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.backend.wayland.inputs import InputConfig
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration

import os


mod = "mod4"
browser = os.environ.get("BROWSER", "firefox")
terminal = os.environ.get("TERMINAL", guess_terminal())
wallpaperPath = "~/.local/wp"


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
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key( [mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
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
        lazy.spawn("wpctl set-volume @DEFAULT_SINK@ 0.1-"),
        desc="-10 volume",
    ),
    Key(
        [mod],
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
    # Keyboard Layout
    Key(
        [mod],
        "F12",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout.",
    ),
    # Program spawning
    Key([mod], "backspace", lazy.spawn("sysact")),
    Key([mod], "d", lazy.spawn("rofi -show-icons -show drun"), desc="drun"),
    Key([mod, "shift"], "d", lazy.spawn("rofi -show-icons -show run"), desc="run"),
    Key([mod], "m", lazy.spawn(terminal + " -e ncmpcpp")),
    Key([mod], "r", lazy.spawn(terminal + " -e lf")),
    Key([mod, "shift"], "r", lazy.spawn(terminal + " -e htop")),
    Key([mod], "w", lazy.spawn(browser), desc="Run browser"),
    Key(
        [mod, "shift"],
        "w",
        lazy.spawn(terminal + " -e nmtui"),
        desc="Run Network Manager TUI",
    ),
    Key([mod], "backslash", lazy.spawn(terminal + " -e bc")),
    Key([mod], "F4", lazy.spawn(terminal + " -e pulsemixer")),
    Key([], "Print", lazy.spawn("grimss cb")),
    Key([mod], "Print", lazy.spawn("grimss")),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    match i.name:
        case "6":
            i.label = "GAME"
        case "7":
            i.label = "VM"
        case "8":
            i.label = "CHAT"
        case "9":
            i.label = "🎶"

    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            # Key(
            #     [mod, "shift"],
            #     i.name,
            #     lazy.window.togroup(i.name, switch_group=True),
            #     desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

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
    "border_width": 4,
    "margin": 8,
    "border_focus": colors[1],
    "border_normal": colors[0],
    "border_on_single": True,
}

layouts = [
    layout.Columns(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Max(**layout_theme),
]

# Decoration Widgets
underline_deco = [BorderDecoration(border_width=[0, 0, 2, 0], colour=colors[1])]

widget_defaults = dict(
    font="FiraCode Nerd Font Bold",
    fontsize=11,
    margin_x=8,
    background=colors[0],
    foreground=colors[1],
)

extension_defaults = widget_defaults.copy()


def initWidgs():
    spacer = widget.Spacer(length=8)
    widgs = [
        spacer,
        widget.CurrentLayout(
            background=colors[0],
            foreground=colors[1],
            decorations=underline_deco,
        ),
        spacer,
        widget.GroupBox(
            padding_x=4,
            margin_x=0,
            disable_drag=True,
            use_mouse_wheel=False,
            hide_unused=True,
            highlight_color=colors[0],
            highlight_method="line",
            block_highlight_text_color=colors[1],
            active=colors[1],
            this_current_screen_border=colors[1],
            this_screen_border=colors[1],
            other_current_screen_border=colors[5],
            other_screen_border=colors[5],
        ),
        spacer,
        widget.WindowName(
            fmt="🪟 {}",
            empty_group_string="No window :D",
            foreground=colors[1],
        ),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.Systray(),
        # widget.StatusNotifier(),
        spacer,
        widget.CPU(
            background=colors[0],
            foreground=colors[1],
            format="🔲 {load_percent}%",
            decorations=underline_deco,
        ),
        spacer,
        widget.Memory(
            background=colors[0],
            foreground=colors[1],
            fmt="💾{}",
            decorations=underline_deco,
        ),
        spacer,
        widget.KeyboardLayout(
            configured_keyboards=["us", "es"],
            fmt="⌨ {}",
            background=colors[0],
            foreground=colors[1],
            decorations=underline_deco,
        ),
        spacer,
        # widget.Battery(
        #     format="{char} {percent:2.0%}",
        #     show_short_text=False,
        #     empty_char="🪫",
        #     discharge_char="🔋",
        #     charge_char="🔌",
        #     full_char="⚡",
        #     background=colors[0],
        #     foreground=colors[1],
        #     decorations=underline_deco,
        #     ),
        # spacer,
        widget.Clock(
            format="🗓️ %a %m/%d 🕓 %I:%M:%S",
            background=colors[0],
            foreground=colors[1],
            decorations=underline_deco,
        ),
        spacer,
    ]
    return widgs


bar_settings = {
    "widgets": initWidgs(),
    "size": 36,
}
screens = [
    Screen(
        wallpaper=wallpaperPath,
        wallpaper_mode="fill",
        top=bar.Bar(**bar_settings),
    ),
    Screen(
        wallpaper=wallpaperPath,
        wallpaper_mode="fill",
        top=bar.Bar(**bar_settings),
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
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = {
    "type:keyboard": InputConfig(
        # Equivalent of xset r rate 300 50
        kb_repeat_delay=300,
        kb_repeat_rate=50,
    ),
}

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
