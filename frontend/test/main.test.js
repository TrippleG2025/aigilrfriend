import { beforeEach, expect, it } from 'vitest'
import { JSDOM } from 'jsdom'

beforeEach(() => {
  const dom = new JSDOM('<div id="app"></div>')
  global.document = dom.window.document
  global.window = dom.window
})

it('renders heading into #app', async () => {
  await import('../src/main.js')
  const app = document.querySelector('#app')
  expect(app.innerHTML).toContain('aigilrfriend MVP')
})
