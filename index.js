/* global module */
/* eslint no-undef: "error" */

// Some internal library function
async function getRandomNumber() {
    return 4
}

// Plugin method that runs on plugin load
async function setupPlugin({ config }) {
    console.log(config.greeting)
}

// Plugin method that processes event
async function processEvent(event, { config, cache }) {
    if (!event.properties) event.properties = {}
    event.properties['greeting'] = config.greeting
    event.properties['random_number'] = await getRandomNumber()
    return event
}

// The plugin itself
module.exports = {
    setupPlugin,
    processEvent
}
