async function setupPlugin({ config, global }) {
    console.log("Setting up the plugin!")
    console.log(config)
    global.setupDone = true
}

async function processEvent(event, { config, cache }) {
    const counter = await cache.get('counter', 0)
    cache.set('counter', counter + 1)

    if (event.properties) {
        event.properties['hello'] = 'world'
        event.properties['bar'] = config.bar
        event.properties['$counter'] = counter
        event.properties['lib_number'] = libFunction(3)
    }

    return event
}

module.exports = {
    setupPlugin,
    processEvent,
}

// Internal library functions below

function libFunction (number) {
    return number * 2;
}
