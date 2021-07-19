from ulauncher.utils.SortedCollection import SortedCollection
from ulauncher.utils.fuzzy_search import get_score


class SortedList:
    """
    List maintains result items in a sorted order
    (sorted by a score, which is a similarity between item's name and a query)
    and limited to a number `limit` passed into the constructor
    """

    def __init__(self, query, min_score=30, limit=9):
        self._query = query.lower().strip()
        self._min_score = min_score
        self._limit = limit
        self._items = SortedCollection(key=lambda i: i.score)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, i):
        return self._items[i]

    def __iter__(self):
        return iter(self._items)

    def __reversed__(self):
        return reversed(self._items)

    def __repr__(self):
        return '%s(%r, min_score=%s, limit=%s)' % (
            self.__class__.__name__,
            self._items,
            self._min_score,
            self._limit
        )

    def __contains__(self, item):
        return item in self._items

    def extend(self, items):
        for item in items:
            self.append(item)

    def append(self, result_item):
        # get_search_name() returns a string with the app display name, but it may contain a
        # set of 4 extra lines with metadata to improve search
        name, *meta_fields = result_item.get_search_name().split("\n")

        score = get_score(self._query, name)
        if len(meta_fields) == 4:
            [exec, comment, keywords, description] = meta_fields
            exec_score = get_score(self._query, exec)
            comment_score = get_score(self._query, comment)
            keywords_score = get_score(self._query, keywords)
            description_score = get_score(self._query, description)
            # Weight the extra fields lower. This is just a naive first implementation
            # Keywords should probably be split up and mached individually
            score = max(score, exec_score * .8, comment_score * .8, keywords_score * .8, description_score * .8)
        if score >= self._min_score:
            result_item.score = -score  # use negative to sort by score in desc. order
            self._items.insert(result_item)
            while len(self._items) > self._limit:
                self._items.pop()  # remove items with the lowest score to maintain limited number of items
