# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"                             # My terminal of choice

keys = [

	### The essentials
	 Key([mod], "Return",
		 lazy.spawn(myTerm),
		 desc='Launches My Terminal'
		 ), 
	 Key([], "Print",
		 lazy.spawn("flameshot gui"),
		 desc='Launches Screen Capture software'
		 ),
	 Key(["mod1"], "Tab",
	 	 lazy.screen.next_group(),
	 	 desc='Toggle to next group'
	  	 ),
	 Key(["mod1", "shift"], "Tab",
	 	 lazy.screen.prev_group(),
	 	 desc='Toggle to prev group'
	  	 ),
	 Key([mod], "Tab",
		 lazy.next_layout(),
		 desc='Toggle through layouts'
		 ),
	 Key([mod], "Escape",
		 lazy.window.kill(),
		 desc='Kill active window'
		 ),
	 Key([mod, "control"], "r", 
		 lazy.restart(),
		 desc="Restart Qtile"),
	 Key([mod, "control", "shift"], "Escape",
		 lazy.shutdown(),
		 desc="Shutdown Qtile"),
    
	 #this is going to be the LAUNCHER
	 Key([mod], "r", 
		lazy.spawn("rofi -combi-modi window,drun,ssh -show combi"),
        desc="Spawn a command using a prompt widget"),
        
	 ### Switch focus to specific monitor (out of three)
	 # Future Proofing
	 Key([mod, "shift"], "w",
		 lazy.to_screen(0),
		 desc='Keyboard focus to monitor 1'
		 ),
	
	 Key([mod, "shift"], "e",
		 lazy.to_screen(1),
		 desc='Keyboard focus to monitor 2'
		 ),
	 Key([mod, "shift"], "r",
		 lazy.to_screen(2),
		 desc='Keyboard focus to monitor 3'
		 ),

	### Treetab controls
	  Key([mod], "h",
		 lazy.layout.move_left(),
		 desc='Move up a section in treetab'
		 ),
	 Key([mod], "l",
		 lazy.layout.move_right(),
		 desc='Move down a section in treetab'
		 ),
	 ### Window controls
	 Key([mod], "j",
		 lazy.layout.down(),
		 desc='Move focus down in current stack pane'
		 ),
	 Key([mod], "k",
		 lazy.layout.up(),
		 desc='Move focus up in current stack pane'
		 ),
	 Key([mod], "h",
		 lazy.layout.left(),
		 desc='Move focus down in current stack pane'
		 ),
	 Key([mod], "l",
		 lazy.layout.right(),
		 desc='Move focus up in current stack pane'
		 ),
	 Key([mod, "shift"], "j",
		 lazy.layout.shuffle_down(),
		 lazy.layout.section_down(),
		 desc='Move windows down in current stack'
		 ),
	 Key([mod, "shift"], "h",
		 lazy.layout.shuffle_up(),
		 lazy.layout.section_up(),
		 desc='Move windows up in current stack'
		 ),
	 Key([mod, "shift"], "h",
		 lazy.layout.shuffle_left(),
		 lazy.layout.section_left(),
		 desc='Move windows down in current stack'
		 ),
	 Key([mod, "shift"], "l",
		 lazy.layout.shuffle_right(),
		 lazy.layout.section_righ(),
		 desc='Move windows up in current stack'
		 ),
	 Key([mod], "Down",
		 lazy.layout.shrink(),
		 lazy.layout.decrease_nmaster(),
		 desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
		 ),
	 Key([mod], "Up",
		 lazy.layout.grow(),
		 lazy.layout.increase_nmaster(),
		 desc='Expand window (MonadTall), increase number in master pane (Tile)'
		 ),
	 Key([mod], "n",
		 lazy.layout.normalize(),
		 desc='normalize window size ratios'
		 ),
	 Key([mod], "m",
		 lazy.layout.maximize(),
		 desc='toggle window between minimum and maximum sizes'
		 ),
	 Key([mod, "shift"], "f",
		 lazy.window.toggle_floating(),
		 desc='toggle floating'
		 ),
	 Key([mod], "f",
		 lazy.window.toggle_fullscreen(),
		 desc='toggle fullscreen'
		 ),
		 
	 ### Stack controls
	 #Key([mod, "shift"], "Right",
	 #	 lazy.layout.rotate(),
	 #	 lazy.layout.flip(),
	 #	 desc='Switch which side main pane occupies (XmonadTall)'
	 #	 ),
	 #Key([mod], "space",
	 #	 lazy.layout.next(),
	 #	 desc='Switch window focus to other pane(s) of stack'
	 #	 ),
	 #Key([mod, "shift"], "space",
	 #	 lazy.layout.toggle_split(),
	 #   desc='Toggle between split and unsplit sides of stack'
	# 	 ),

]

group_names = [("1", {'layout': 'monadtall'}), # Web
               ("2", {'layout': 'monadtall'}), # Dev
               ("3", {'layout': 'monadtall'}), # Sys
               ("4", {'layout': 'monadtall'}), # Docs
               ("5", {'layout': 'monadtall'}), # Music
               ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 1,
                "margin": 15,
                "border_focus": "fabd2f",
                "border_normal": "fb4934"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    #layout.TreeTab(
    #     font = "Noto Color Emoji",
    #     fontsize = 10,
    #     sections = ["1", "2", "3", "4"],
    #     section_fontsize = 10,
    #     border_width = 2,
    #     bg_color = "32302f",
    #     active_bg = "fe8019",
    #     active_fg = "3c3836",
    #     inactive_bg = "83a598",
    #     inactive_fg = "3c3836",
    #     padding_left = 0,
    #     padding_x = 0,
    #     padding_y = 5,
    #     section_top = 10,
    #     section_bottom = 20,
    #     level_shift = 8,
    #     vspace = 3,
    #     panel_width = 200
    #     ),
    layout.Floating(**layout_theme)
]

colors = []
          

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Fira Code",
    fontsize = 12,
    padding = 2,
    background=["#282828", "#282828"]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = ["#dbcdac", "#dbcdac"],
                       background = ["#282828CC", "#282828CC"]
                       ),
              widget.CurrentLayout(
                       foreground = ["#ac7947", "#ac7947"],
                       background = ["#282828CC", "#282828CC"],
                       padding = 5
                       ),
              widget.TextBox(
					   font = "Noto", # this is to properly display the character         
                       text = " | ",
                       fontsize = 10,
                       foreground = ["#dbcdac", "#dbcdac"],
                       background = ["#282828CC", "#282828CC"],
                       padding = 0,
                       ),
              widget.GroupBox(
                       font = "Roboto Bold",
                       fontsize = 12,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = ["#8bbd87", "#8bbd87"],  #text color of active group
                       inactive = ["#89837d", "#89837d"], #text color of inactive group
                       rounded = False,
                       highlight_color = ["#3c3835aa", "#3c3835aa"], # bg of the active group
                       highlight_method = "line",
                       this_current_screen_border = ["#eebd4f"], 
                       this_screen_border = ["#eebd4f"],
                       #other_current_screen_border = colors[6],
                       #other_screen_border = colors[4],
                       foreground = ["#dbcdac", "#dbcdac"],
                       background = ["#282828CC", "#282828CC"]
                       ),
              widget.TextBox(
					   font = "Noto", # this is to properly display the character         
                       text = " | ",
                       fontsize = 10,
                       foreground = ["#dbcdac", "#dbcdac"],
                       background = ["#282828CC", "#282828CC"],
                       padding = 0,
                       ),
              widget.TaskList(
		               margin = 4, 
                       foreground = ["#dbcdac", "#dbcdac"],
                       background = ["#282828CC", "#282828CC"],
                       rounded = True,
                       max_title_width = 100,
                       border = ["#282828CC", "#282828CC"],
			  ),
              widget.Spacer(
                       background =["#282828CC", "#282828CC"]
                       ),
              widget.TextBox(
					   font = "Noto", # this is to properly display the character         
                       text = " | ",
                       fontsize = 10,
                       foreground = ["#ec4e49", "#ec4e49"],
                       background = ["#282828CC", "#282828CC"],
                       padding = 0,
                       ),
              widget.Net(
                       interface = 'wlp5s0',
                       format = "{down} ↓↑ {up}",
                       foreground = ["#ed802e", "#ed802e"],
                       background = ["#282828CC", "#282828CC"],
                       ),
              widget.TextBox(
					   font = "Noto", # this is to properly display the character         
                       text = " | ",
                       fontsize = 10,
                       foreground = ["#ec4e49", "#ec4e49"],
                       background = ["#282828CC", "#282828CC"],
                       padding = 0,
                       ),
              widget.Memory(
                       padding = 0,
                       format = ' {MemUsed:0.0f} MiB ',
                       foreground = ["#ed802e", "#ed802e"],
                       background = ["#282828CC", "#282828CC"],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + 'bpytop')},
                       ),
              widget.TextBox(
					   font = "Noto", # this is to properly display the character         
                       text = " | ",
                       fontsize = 10,
                       foreground = ["#ec4e49", "#ec4e49"],
                       background = ["#282828CC", "#282828CC"],
                       padding = 0,
                       ),
              widget.Clock(
					   padding = 5,
                       foreground = ["#eebd4f", "#eebd4f"],
                       background = ["#282828CC", "#282828CC"],
                       format = "%a | %B %d, %Y | %H:%M"
                       ),
              widget.TextBox(
					   font = "Noto", # this is to properly display the character         
                       text = " | ",
                       fontsize = 10,
                       foreground = ["#ec4e49", "#ec4e49"],
                       background = ["#282828CC", "#282828CC"],
                       padding = 0,
                       ),
              widget.Systray(
					   iconsize = 12,
                       background = ["#282828CC", "#282828CC"],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = ["#dbcdac", "#dbcdac"],
                       background = ["#282828CC", "#282828CC"]
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), margin = [15,200,0,200], opacity=1.0, size=25)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), margin = [15,200,0,200], opacity=1.0, size=25)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), margin = [15,200,0,200], opacity=1.0, size=25))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = "floating_only"
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
    Match(wm_class='steam'), 		  # steam
    Match(wm_class='Origin'), 		  # steam
    Match(title='Origin'),      # tastyworks exit box
    Match(wm_class='CopyQ'), 		  # CopyQ
], border_focus="#fabd2f",
   border_width=2,
   border_normal="#fb4934")
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

