import { PostHogEvent, Webhook } from '@posthog/plugin-scaffold'

const { composeWebhook } = require('./index')

test('creates the correct webhook body', async () => {
    const event: PostHogEvent = {
        uuid: '123',
        team_id: 1,
        distinct_id: 'alice',
        event: 'pageview',
        timestamp: new Date('2023-01-01T00:00:00.000Z'),
        properties: {
            prop: 'value',
        },
    }
    const webhook: Webhook = composeWebhook(event, { config: { webhook_url: 'https://example.com' } })
    expect(webhook).toEqual({
        url: 'https://example.com',
        body: '{"uuid":"123","team_id":1,"distinct_id":"alice","event":"pageview","timestamp":"2023-01-01T00:00:00.000Z","properties":{"prop":"value"}}',
        headers: {
            'Content-Type': 'application/json',
        },
        method: 'POST',
    })
})
