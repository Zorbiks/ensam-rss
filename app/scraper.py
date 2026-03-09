import requests
from bs4 import BeautifulSoup

URL = "https://ensam-casa.ma/"

def get_announcements():
    """
    Scrape the latest announcements from the first carousel on the ENSAM Casablanca homepage.

    Returns:
        list[dict]: A list of dictionaries, each containing:
            - 'title' (str or None): The announcement text from the `h1` tag.
            - 'link' (str or None): The hyperlink associated with the announcement.
            - 'image' (str or None): The URL of the image in the slide.
            If the carousel is not found, returns an empty list.
    """

    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")

    results = []

    # get the first .owl-carousel
    carousel = soup.find("div", class_="owl-carousel")
    if not carousel:
        print("No carousel found")
        return results

    # find all direct slide divs inside the carousel
    slides = carousel.find_all("div", recursive=False)

    for slide in slides:
        h1_tag = slide.find("h1")
        a_tag = slide.find("a")
        img_tag = slide.find("img")

        title = h1_tag.get_text(strip=True) if h1_tag else None
        link = a_tag["href"] if a_tag and a_tag.has_attr("href") else None
        image = img_tag["src"] if img_tag and img_tag.has_attr("src") else None

        results.append({
            "title": title,
            "link": link,
            "image": image
        })

    return results


