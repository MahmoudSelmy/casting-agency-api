ITEMS_PER_PAGE = 10


def paginate_items(page_number, items):
    n = len(items)
    start = (page_number - 1) * ITEMS_PER_PAGE
    end = min(start + ITEMS_PER_PAGE, n)
    if start >= n:
        return []
    items = items[start:end]
    return items
