from django.core.paginator import (
     Paginator,
     Page,
     EmptyPage,
     PageNotAnInteger)


def get_page_obj_for_page_number(page_number: int, per_page: int, object_list)->Page:
    """Return page object (Page) for given page number

    Args:
        page_number (int): page number
        per_page (int): the maximum number of items to include on a page
        object_list (iterables): items to display

    Returns:
        Page: Page object
    """
    paginator = Paginator(object_list, per_page)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj
