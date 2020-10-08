from posthog.plugins import PluginBaseClass


class ExamplePlugin(PluginBaseClass):
    def process_event(self, event):
        print(event)
        return event
