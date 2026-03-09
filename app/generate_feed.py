from feedgen.feed import FeedGenerator
from scraper import get_announcements


def generate():

    items = get_announcements()

    fg = FeedGenerator()
    fg.title("ENSAM Casablanca Announcements")
    fg.link(href="https://ensam-casa.ma/")
    fg.description("Latest announcemnts from ENSAM Casablanca")
    # fg.language("fr")

    for item in items:
        entry = fg.add_entry()
        entry.title(item["title"])
        
        # If link is missing, fallback to main site
        entry.link(href=item["link"] if item["link"] else "https://ensam-casa.ma/")

        # Optionally include the image
        if item.get("image"):
            entry.enclosure(item["image"], 0, "image/jpeg")

    # saves to feed.xml
    fg.rss_file("feed.xml")
    print("RSS feed generated as feed.xml")


if __name__ == "__main__":
    generate()