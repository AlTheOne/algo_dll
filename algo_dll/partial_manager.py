from typing import Any

from algo_dll.exceptions import InvalidNextIdException, NodeAlreadyExistException
from algo_dll.nodes import Node


class PartialManager:

    def __init__(self) -> None:
        self.node_map: dict[Any, Node] = {}
        self.last_node: Node | None = None

    def get_node(
            self,
            node_id: Any,
    ) -> Node | None:
        return self.node_map.get(node_id)

    def link_nodes(
        self,
        prev_node: Node | None,
        next_node: Node | None,
    ) -> None:
        if prev_node and next_node:
            prev_node.next_node = next_node
            next_node.prev_node = prev_node
        elif prev_node:
            del prev_node.next_node
        elif next_node:
            del next_node.prev_node

    def set_prepared_node(
            self,
            node: Node,
    ) -> None:
        if node.id in self.node_map:
            raise NodeAlreadyExistException

        self.node_map[node.id] = node

    def _move_node_to_end(
            self,
            node: Node,
    ) -> None:
        self.link_nodes(
            prev_node=node.prev_node,
            next_node=node.next_node,
        )

        if self.last_node:
            self.last_node.next_node = node
            node.prev_node = self.last_node
            del node.next_node
            self.last_node = node

    def _move_node(
            self,
            node: Node,
            next_node: Node,
    ) -> None:
        self.link_nodes(
            prev_node=node.prev_node,
            next_node=node.next_node,
        )
        self.link_nodes(
            prev_node=next_node.prev_node,
            next_node=node,
        )
        self.link_nodes(
            prev_node=node,
            next_node=next_node,
        )

    def move_node(
            self,
            node: Node,
            next_node: Node | None = None,
    ) -> None:
        if next_node is not None and node.id == next_node.id:
            raise InvalidNextIdException

        if next_node is None:
            self._move_node_to_end(node=node)
        else:
            self._move_node(node=node, next_node=next_node)
