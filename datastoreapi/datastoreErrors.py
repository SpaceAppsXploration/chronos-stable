__author__ = 'lorenzo'


class DocumentExistNot(Exception):
    """
    Custom exception: trying to fetch a non-existant Document from the Mongo instance
    """
    pass


class DocumentExists(Exception):
    """
    Custom exception: Document already exists in the Mongo instance
    """
    pass


class ValueExistsInList(Exception):
    """
    Custom exception: the script is trying to append to list of values an object that is already in the list
    """
    pass