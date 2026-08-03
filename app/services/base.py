from typing import Generic, TypeVar

T = TypeVar('T')

class BaseService(Generic[T]):
    def __init__(self, repository: T):
        self.repository = repository

