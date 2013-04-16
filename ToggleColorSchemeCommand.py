# Copy this file to ~/Library/Application Support/Sublime Text 2/Packages/User/

import sublime, sublime_plugin

class ToggleColorSchemeCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):
        light_scheme = args["light_color_scheme"]
        dark_scheme  = args["dark_color_scheme"]

        light_theme  = args["light_theme"]
        dark_theme   = args["dark_theme"]

        settings = sublime.load_settings('Preferences.sublime-settings')
        current_scheme = settings.get('color_scheme')

        if current_scheme == light_scheme:
            settings.set('color_scheme', dark_scheme)
            settings.set('theme', dark_theme)
        else:
            settings.set('color_scheme', light_scheme)
            settings.set('theme', light_theme)

        sublime.save_settings('Preferences.sublime-settings')
