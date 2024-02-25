from typing import Any, Callable

from src.exceptions import NodeDoesNotExistException
from src.nodes import Node


class ManagerByIdMixin:

    node_map: dict[Any, Node]

    get_node: Callable[[Any], Node | None]
    set_node: Callable[[Node, Node | None], None]
    remove_node: Callable[[Node], None]
    move_node: Callable[[Node, Node | None], None]

    def has_node_by_id(
            self,
            node_id: Any,
    ) -> bool:
        return node_id in self.node_map

    def set_node_by_id(
        self,
        node: Node,
        next_node_id: Any | None = None,
    ) -> None:
        next_node = None
        if next_node_id is not None:
            next_node = self.node_map[next_node_id]
            if next_node is None:
                raise NodeDoesNotExistException

        return self.set_node(node, next_node)

    def remove_node_by_id(
        self,
        node_id: Any,
    ) -> None:
        node = self.get_node(node_id)
        if node is None:
            raise NodeDoesNotExistException

        self.remove_node(node)

    def move_node_by_id(
        self,
        node_id: Any,
        next_node_id: Any | None = None,
    ) -> None:
        node = self.get_node(node_id)
        if node is None:
            raise NodeDoesNotExistException

        next_node = None
        if next_node_id is not None:
            next_node = self.get_node(next_node_id)
            if next_node is None:
                raise NodeDoesNotExistException

        self.move_node(node, next_node)
