# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import socket, requests

class IPFinderPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		local_ip = s.getsockname()[0]
		s.close()
		public_ip = requests.get('https://api.ipify.org').content.decode('utf8')
		requests.post(self._settings.get(["url"]), json = {'local': local_ip, 'public': public_ip })
		return self._logger.info("IP sent (url: %s)" % self._settings.get(["url"]))

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	def get_settings_defaults(self):
		return dict(url="https://octoprint.carsons.site/")

	def on_settings_save(self,data):
		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		local_ip = s.getsockname()[0]
		s.close()
		public_ip = requests.get('https://api.ipify.org').content.decode('utf8')
		requests.post(data['url'], json = {'local': local_ip, 'public': public_ip })
		return self._logger.info("IP sent (url: %s)" % data['url'])

__plugin_name__ = "IP Finder"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = IPFinderPlugin()
