from posthog.plugins import PluginBaseClass, PosthogEvent


class ExamplePlugin(PluginBaseClass):
    @staticmethod
    def instance_init():
        raise Exception("Something fishy")
