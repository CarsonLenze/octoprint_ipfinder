# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import requests

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://en.wikipedia.org/wiki/Hello_world")

	def get_template_vars(self):
        return requests.post(self._settings.get(["url"]), json = {'local': 'testing' })

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
