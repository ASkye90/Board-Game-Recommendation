import re
import time

from playwright.sync_api import sync_playwright

BLOCK_RESOURCE_TYPES = [
    'image',
    'media',
    'font',
]


def _block_resources(route):
    if route.request.resource_type in BLOCK_RESOURCE_TYPES:
        return route.abort()
    else:
        return route.continue_()

def get_fans_also_like_for(bg_ids):
    bg_dict = {}
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.route("**/*", _block_resources)
        for bg_id in bg_ids:
            bg_dict[bg_id] = []
            page.goto("https://boardgamegeek.com/boardgame/" + str(bg_id))
            page.goto(page.url + '/recommendations')
            page.wait_for_selector('a.rec')
            recommendation_titles = page.locator('a.rec').all()
            for recommendation in recommendation_titles:
                url = recommendation.get_attribute('href')
                similar_bg_id = re.search(r'/.[0-9]*/', url).group(0)[1:-1]
                bg_dict[bg_id].append(similar_bg_id)
            # Sleep to keep compliant with BGG TOS
            # https://boardgamegeek.com/terms#:~:text=the%20Geek%20Websites%3A-,i.%20Don%27t%20slam%20our%20servers%20with%20%22robots%22%20or%20%22spiders%22.,-You%20shall%20not
            time.sleep(2)
    return bg_dict
