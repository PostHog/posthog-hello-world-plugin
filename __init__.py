from posthog.plugins import PluginBaseClass, PosthogEvent


class ExamplePlugin(PluginBaseClass):
    def process_event(self, event: PosthogEvent):
        print(event)
        return event
