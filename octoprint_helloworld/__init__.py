# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import socket, requests

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://en.wikipedia.org/wiki/Hello_world")

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	def on_settings_save(self,data):
		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
		self._logger.info(data['url'])
		hostname = socket.gethostname()
		local_ip = socket.gethostbyname(hostname)
		public_ip = requests.get('https://api.ipify.org').content.decode('utf8')

		requests.post(data['url'], json = {'local': local_ip, 'public': public_ip })

	def get_assets(self):
		return dict(
			js=["js/helloworld.js"],
			css=["css/helloworld.css"],
			less=["less/helloworld.less"]
		)

__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
