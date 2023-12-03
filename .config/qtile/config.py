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
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.backend.wayland.inputs import InputConfig
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration


mod = "mod4"
browser = "thorium-browser"
terminal = "alacritty"
wallpaperPath = "~/.local/wp"

keys = [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod],
            "space",
            lazy.layout.next(),
            desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"],
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left"),
        Key([mod, "shift"],
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right"),
        Key([mod, "shift"],
            "j",
            lazy.layout.shuffle_down(),
            desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "control"],
            "h",
            lazy.layout.grow_left(),
            desc="Grow window to the left"),
        Key([mod, "control"],
            "l",
            lazy.layout.grow_right(),
            desc="Grow window to the right"),
        Key([mod, "control"],
            "j",
            lazy.layout.grow_down(),
            desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
            ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
            [mod],
            "f",
            lazy.window.toggle_fullscreen(),
            desc="Toggle fullscreen on the focused window",
            ),
    Key([mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn(terminal + " -e lfcd")),
    Key([mod, "shift"], "r", lazy.spawn(terminal + " -e htop")),
    Key([mod], "d", lazy.spawn("rofi -show-icons -show drun"), desc="drun"),
    Key([mod, "shift"],
        "d",
        lazy.spawn("rofi -show-icons -show run"),
        desc="run"),
    Key([mod], "w", lazy.spawn(browser), desc="Run browser"),
    Key([mod], "F4", lazy.spawn(terminal + " -e pulsemixer")),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
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
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
        ])

layouts = [
        layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
        layout.Max(),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadTall(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
        ]

catppuccinFrappe = [
        ["#303446", "#303446"], # bg
        ["#c6d0f5", "#c6d0f5"], # fg
        ["#e78284", "#e78284"], # color01 red
        ["#a6d189", "#a6d189"], # color02 green
        ["#e5c890", "#e5c890"], # color03 yellow
        ["#8caaee", "#8caaee"], # color04 blue
        ["#f4b8e4", "#f4b8e4"], # color05 magenta
        ["#81c8be", "#81c8be"], # color06 cyan
        ["#a5adce", "#a5adce"]  # color15 white
        ]

colors = catppuccinFrappe
backslashDecor = {
        "decorations": [
            PowerLineDecoration(path="forward_slash")
            ]
        }
forwslashDecor = {
        "decorations": [
            PowerLineDecoration(path="back_slash")
            ]
        }

widget_defaults = dict(
        font="Comic Shanns Mono Nerd Font",
        fontsize=12,
        margin_x=8,
        background=colors[0],
        foreground=colors[1],
        )
extension_defaults = widget_defaults.copy()

screens = [
        Screen(
            wallpaper=wallpaperPath,
            wallpaper_mode="fill",
            top=bar.Bar(
                [
                    widget.CurrentLayout(
                        background=colors[5],
                        foreground=colors[0],
                        **forwslashDecor,
                        ),
                    widget.Spacer(
                        length=16,
                        ),
                    widget.GroupBox(
                        padding_x=4,
                        margin_x=0,
                        active=colors[6],
                        inactive=colors[1],
                        disable_drag=False,
                        highlight_method="line",
                        use_mouse_wheel=False,
                        highlight_color=colors[0],
                        this_current_screen_border=colors[6],
                        this_screen_border=colors[4],
                        ),
                    widget.Spacer( length=16,),
                    widget.WindowName(
                        foreground=colors[6],
                        **backslashDecor,
                        ),
                    # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                    # widget.Systray(),
                    # widget.StatusNotifier(),
                    widget.CheckUpdates(
                        background=colors[5],
                        colour_have_updates=colors[0],
                        colour_no_updates=colors[0],
                        display_format="Updates: {updates}",
                        no_update_string="All good",
                        **backslashDecor,
                        ),
                    widget.TextBox(
                        margin_x=0,
                        background=colors[6],
                        foreground=colors[0],
                        fmt="Net",
                        ),
                    widget.NetGraph(
                        background=colors[6],
                        border_color=colors[0],
                        graph_color=colors[0],
                        fill_color=colors[0],
                        margin_y = 6,
                        margin_x = 0,
                        ),
                    widget.Spacer(length=8,background=colors[6], **backslashDecor),
                    widget.Clock(
                        format="%Y/%m/%d %a %I:%M:%S %p",
                        background=colors[5],
                        foreground=colors[0],
                        ),
                    ],
                36,
                ),
            # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
            # By default we handle these events delayed to already improve performance, however your system might still be struggling
            # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
            # x11_drag_polling_rate = 60,
            ),
        ]

# Drag floating layouts.
mouse = [
        Drag([mod],
             "Button1",
             lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag([mod],
             "Button3",
             lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
        ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
    ])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = {

        # Equivalent of xset r rate 300 50
        "type:keyboard": InputConfig(
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
