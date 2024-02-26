from typing import Any, Optional

__all__ = [
    'Node',
]


class Node:

    def __init__(
        self,
        node_id: Any,
        prev_node: Optional['Node'] = None,
        next_node: Optional['Node'] = None,
        value: Any = None,
    ) -> None:
        self.id = node_id
        self._value = value
        self._prev_node = prev_node
        self._next_node = next_node

    @property
    def prev_node(self) -> Optional['Node']:
        return self._prev_node

    @prev_node.setter
    def prev_node(
        self,
        value: Optional['Node'],
    ) -> None:
        self._prev_node = value

    @prev_node.deleter
    def prev_node(self) -> None:
        self._prev_node = None

    @property
    def next_node(self) -> Optional['Node']:
        return self._next_node

    @next_node.setter
    def next_node(
        self,
        value: Optional['Node'],
    ) -> None:
        self._next_node = value

    @next_node.deleter
    def next_node(self) -> None:
        self._next_node = None

    def reset(self) -> None:
        del self.prev_node
        del self.next_node
