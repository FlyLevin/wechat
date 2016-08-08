from django.db import models

class QuerySet(models.QuerySet):
    def first(self):
        """
        Returns the first object of a query, returns None if no match is found.
        """
        objects = list((self if self.ordered else self.order_by('pk'))[:1])
        if objects:
            return objects[0]
        return None

    def last(self):
        """
        Returns the last object of a query, returns None if no match is found.
        """
        objects = list((self.reverse() if self.ordered else self.order_by('-pk'))[:1])
        if objects:
            return objects[0]
        return None
