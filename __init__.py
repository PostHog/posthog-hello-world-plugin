from posthog.plugins import PluginBaseClass, PosthogEvent


class ExamplePlugin(PluginBaseClass):
    def process_event(self, event: PosthogEvent):
        raise Exception("this is fine")
