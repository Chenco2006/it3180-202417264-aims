def search_by_category(dvds, category):
    """Search DVDs by category."""
    keyword = category.lower()

    return [
        dvd for dvd in dvds
        if keyword in dvd.category.lower()
    ]


def search_by_title(dvds, title):
    """Tìm các DVD có tiêu đề chứa từ khóa."""
    keyword = title.lower()

    return [
        dvd for dvd in dvds
        if keyword in dvd.title.lower()
    ]