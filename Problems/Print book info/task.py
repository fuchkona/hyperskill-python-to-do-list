def print_book_info(title, author=None, year=None):
    result = f'"{title}"'
    if author or year:
        result += ' was written'
    if author:
        result += f' by {author}'
    if year:
        result += f' in {year}'
    print(result)
