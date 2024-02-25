from typing import Any

from src.exceptions import (
    InvalidNextIdException,
    NodeAlreadyExistException,
    NodeDoesNotExistException,
)
from src.manager_by_id_mixin import ManagerByIdMixin
from src.nodes import Node


class DllManager(ManagerByIdMixin):

    def __init__(self) -> None:
        self.node_map: dict[Any, Node] = {}

    def get_node(
            self,
            node_id: Any,
    ) -> Node | None:
        return self.node_map.get(node_id)

    def has_node(
            self,
            node: Node,
    ) -> bool:
        return node.id in self.node_map

    def get_end_node(self) -> Node | None:
        last_node: Node | None = None
        for _node in self.node_map.values():
            if _node.next_node is None:
                last_node = _node
                break

        return last_node

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

    def _set_node_to_end(
        self,
        node: Node,
    ) -> None:
        last_node = self.get_end_node()
        if last_node is not None:
            last_node.next_node = node
            node.prev_node = last_node

    def _set_node(
        self,
        node: Node,
        next_node: Node,
    ) -> None:
        """
        Set node not to end.

        ```
        node_map = [
            <node1>,   # upper than <node>
            <node2>,   # lower than <node>
            <node3>,
        ]
        ```

        Set <node> to node_map
        next_node = <node2>

        =>

        ```
        node_map = [
            <node1>,   # upper than <node>
            <node>,    # set <node>
            <node2>,   # lower than <node>
            <node3>,
        ]
        ```
        """
        _node_lower = next_node
        _node_upper = _node_lower.prev_node

        # Update upper node...
        if _node_upper:
            _node_upper.next_node = node

        # Update lower node...
        if _node_lower:
            _node_lower.prev_node = node

        # Update linked set node...
        node.prev_node = _node_upper
        node.next_node = _node_lower

    def set_node(
        self,
        node: Node,
        next_node: Node | None = None,
    ) -> None:
        if node.id in self.node_map:
            raise NodeAlreadyExistException

        if next_node is not None and next_node.id not in self.node_map:
            raise NodeDoesNotExistException

        if next_node is None:
            self._set_node_to_end(node=node)
        else:
            self._set_node(node=node, next_node=next_node)

        # Set to map...
        self.node_map[node.id] = node

    def remove_node(
        self,
        node: Node,
    ) -> None:
        _node = self.node_map.pop(node.id, None)
        if _node:
            _prev_node = _node.prev_node
            _next_node = _node.next_node

            if _prev_node and _next_node:
                _prev_node.next_node = _next_node
                _next_node.prev_node = _prev_node
            elif _prev_node:
                del _prev_node.next_node
            elif _next_node:
                del _next_node.prev_node

            _node.reset()

    def _move_node_to_end(
        self,
        node: Node,
    ) -> None:
        self.link_nodes(
            prev_node=node.prev_node,
            next_node=node.next_node,
        )

        last_node = self.get_end_node()
        if last_node:
            last_node.next_node = node
            node.prev_node = last_node
            del node.next_node

    def _move_node(
        self,
        node: Node,
        next_node: Node,
    ) -> None:
        if node == next_node:
            raise InvalidNextIdException

        self.link_nodes(
            prev_node=node.prev_node,
            next_node=node.next_node,
        )
        self._set_node(
            node=node,
            next_node=next_node,
        )

    def move_node(
        self,
        node: Node,
        next_node: Node | None = None,
    ) -> None:
        if next_node is None:
            self._move_node_to_end(node=node)
        else:
            self._move_node(
                node=node,
                next_node=next_node,
            )
