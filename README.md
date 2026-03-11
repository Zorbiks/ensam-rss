# ENSAM RSS

A minimal Python tool to generate an RSS feed from ENSAM Casablanca announcements.

## Features

- Scrapes announcements (title, link, image) from ENSAM Casablanca.  
- Generates a valid RSS feed (`feed.xml`).  
- Optional FastAPI server to serve the feed over HTTP.  

## Usage

1. Clone the repo:
```bash
git clone https://github.com/Zorbiks/ensam-rss.git
cd ensam-rss
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Generate the feed:

```bash
python app/generate_feed.py
```

4. (Optional) Run API server:

```bash
uvicorn app.server:app --reload --host 0.0.0.0 --port 8000
```

Access the feed at:

```
http://localhost:8000/feed.xml
```

## Docker

### Pull prebuilt image

```bash
docker pull zorbiks/ensam-rss:latest
```

Docker Hub: [https://hub.docker.com/r/zorbiks/ensam-rss](https://hub.docker.com/r/zorbiks/ensam-rss)

## Notes

* Depends on the ENSAM Casablanca homepage structure; may break if the site changes.
* Images are included in the RSS feed when available.

