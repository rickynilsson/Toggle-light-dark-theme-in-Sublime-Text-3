# Copy this file to ~/Library/Application Support/Sublime Text 3/Packages/User/

import sublime, sublime_plugin

class ToggleColorSchemeCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):
        light_scheme = args["light_color_scheme"]
        dark_scheme  = args["dark_color_scheme"]

        light_theme  = args["light_theme"]
        dark_theme   = args["dark_theme"]

        light_theme_font  = args["light_theme_font"]
        dark_theme_font   = args["dark_theme_font"]

        settings = sublime.load_settings('Preferences.sublime-settings')
        current_scheme = settings.get('color_scheme')

        if current_scheme == light_scheme:
            settings.set('color_scheme', dark_scheme)
            settings.set('theme', dark_theme)
            settings.set('font_face', dark_theme_font)
        else:
            settings.set('color_scheme', light_scheme)
            settings.set('theme', light_theme)
            settings.set('font_face', light_theme_font)

        sublime.save_settings('Preferences.sublime-settings')