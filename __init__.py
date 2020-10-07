from posthog.plugins import PluginBaseClass


class ShitPlugin(PluginBaseClass):
    def process_event(self, event):
        print(event)
        return event
