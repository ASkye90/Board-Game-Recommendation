import re

from playwright.sync_api import sync_playwright

BLOCK_RESOURCE_TYPES = [
    'image',
    'media',
    'font',
]

def block_resources(route):
    if route.request.resource_type in BLOCK_RESOURCE_TYPES:
        return route.abort()
    else:
        return route.continue_()

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.route("**/*", block_resources)
    with page.expect_response('**/174430/*') as response:
        page.goto("https://boardgamegeek.com/boardgame/174430")

    print (response.value.url)
    page.goto(page.url + '/recommendations')

    recommendation_titles = page.locator('a.rec').all()

    for recommendation in recommendation_titles:
        url = recommendation.get_attribute('href')
        test = re.search(r'/.[0-9]*/', url).group(0)[1:-1]
    page.wait_for_timeout(120000)
