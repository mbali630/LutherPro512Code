import requests

def fetch_book_by_isbn_openlib(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            # Get author info
            author_name = ''
            authors = data.get('authors', [])
            if authors:
                author_key = authors[0].get('key', '')
                if author_key:
                    author_response = requests.get(f"https://openlibrary.org{author_key}.json")
                    if author_response.status_code == 200:
                        author_data = author_response.json()
                        author_name = author_data.get('name', '')

            # Safely extract publication year
            publication_year = None
            publish_date = data.get('publish_date', '')
            if publish_date and publish_date[-4:].isdigit():
                publication_year = int(publish_date[-4:])

            # Handle description (can be dict or string)
            description = data.get('description', '')
            if isinstance(description, dict):
                description = description.get('value', '')

            # Handle language
            language = 'en'
            if data.get('languages'):
                lang_key = data['languages'][0].get('key', '')
                if lang_key:
                    language = lang_key.split('/')[-1]

            return {
                'title': data.get('title', ''),
                'author': author_name,
                'publisher': ', '.join(data.get('publishers', [])),
                'publication_year': publication_year,
                'description': description,
                'page_count': data.get('number_of_pages', 0),
                'language': language,
                'cover_image_url': f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg",
                'category': ', '.join(data.get('subjects', []))
            }
    except Exception as e:
        print(f"Open Library API error: {e}")
    return None