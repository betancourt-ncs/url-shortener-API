import secrets
from models import ShortURL


# Creating a short code
def create_short_url(db, original_url: str):
    short_code = secrets.token_urlsafe(4)
    short_url = ShortURL(url=original_url, short_code=short_code)
    db.add(short_url)
    db.commit()
    db.refresh(short_url)
    return short_url


# Reading a short code from db
def get_short_url(db, short_code: str):
    result = db.query(ShortURL).filter(
        ShortURL.short_code == short_code).first()
    return result


# Updating the URL in an existing row
def update_short_url(db, short_code: str, new_url: str):
    existing_url = get_short_url(db, short_code)

    if existing_url:
        existing_url.url = new_url
        db.commit()
        db.refresh(existing_url)
        return existing_url
    else:
        return None


# Deleting a row
def delete_short_url(db, short_code: str):
    existing_url = get_short_url(db, short_code)
    if existing_url:
        db.delete(existing_url)
        db.commit()
        return True
    else:
        return None


# Retrieving a row and its access count
def get_url_stats(db, short_code: str):
    return get_short_url(db, short_code)
