from posthog.plugins import PluginBaseClass, PosthogEvent


class ExamplePlugin(PluginBaseClass):
    def team_init(self):
        raise Exception("Something fishy in this team")
