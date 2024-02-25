import pytest

from src.exceptions import NodeAlreadyExistException
from src.manager import DllManager
from src.nodes import Node


class TestDllManagerSetNode:

    def test_dll_filled_when_set_first_node(
            self,
            dll_manager_filled: DllManager,
    ) -> None:
        node1 = dll_manager_filled.get_node(node_id=1)
        node2 = dll_manager_filled.get_node(node_id=2)
        node3 = dll_manager_filled.get_node(node_id=3)

        node0 = Node(node_id=0)

        dll_manager_filled.set_node(node=node0, next_node=node1)

        # Check node0...
        assert node0.prev_node is None
        assert node0.next_node == node1

        # Check node1...
        assert node1.prev_node == node0
        assert node1.next_node == node2

        # Check node2...
        assert node2.prev_node == node1
        assert node2.next_node == node3

        # Check node3...
        assert node3.prev_node == node2
        assert node3.next_node is None

    def test_dll_filled_when_set_last_node(
            self,
            dll_manager_filled: DllManager,
    ) -> None:
        node1 = dll_manager_filled.get_node(node_id=1)
        node2 = dll_manager_filled.get_node(node_id=2)
        node3 = dll_manager_filled.get_node(node_id=3)

        node4 = Node(node_id=4)

        dll_manager_filled.set_node(node=node4)

        # Check node1...
        assert node1.prev_node is None
        assert node1.next_node == node2

        # Check node2...
        assert node2.prev_node == node1
        assert node2.next_node == node3

        # Check node3...
        assert node3.prev_node == node2
        assert node3.next_node == node4

        # Check node4...
        assert node4.prev_node == node3
        assert node4.next_node is None

    def test_dll_filled_when_set_middle_node(
            self,
            dll_manager_filled: DllManager,
    ) -> None:
        node1 = dll_manager_filled.get_node(node_id=1)
        node2 = dll_manager_filled.get_node(node_id=2)
        node3 = dll_manager_filled.get_node(node_id=3)

        node1_5 = Node(node_id=1.5)

        dll_manager_filled.set_node(node=node1_5, next_node=node2)

        # Check node1...
        assert node1.prev_node is None
        assert node1.next_node == node1_5

        # Check node1_5...
        assert node1_5.prev_node == node1
        assert node1_5.next_node == node2

        # Check node2...
        assert node2.prev_node == node1_5
        assert node2.next_node == node3

        # Check node3...
        assert node3.prev_node == node2
        assert node3.next_node is None

    def test_dll_with_single_node_when_set_first_node(
            self,
            dll_manager_with_single_node: DllManager,
    ) -> None:
        node0 = Node(node_id=0)
        node1 = dll_manager_with_single_node.get_node(node_id=1)

        dll_manager_with_single_node.set_node(node=node0, next_node=node1)

        assert len(dll_manager_with_single_node.node_map) == 2

        # Check node0...
        assert node0.prev_node is None
        assert node0.next_node == node1

        # Check node1...
        assert node1.prev_node == node0
        assert node1.next_node is None

    def test_dll_with_single_node_when_set_last_node(
            self,
            dll_manager_with_single_node: DllManager,
    ) -> None:
        node2 = Node(node_id=2)
        node1 = dll_manager_with_single_node.get_node(node_id=1)

        dll_manager_with_single_node.set_node(node=node2)

        assert len(dll_manager_with_single_node.node_map) == 2

        # Check node1...
        assert node1.prev_node is None
        assert node1.next_node == node2

        # Check node0...
        assert node2.prev_node == node1
        assert node2.next_node is None

    def test_dll_empty_when_set_node(
            self,
            dll_manager_empty: DllManager,
    ) -> None:
        node1 = Node(node_id=1)

        dll_manager_empty.set_node(node=node1)

        assert dll_manager_empty.node_map

        assert node1.prev_node is None
        assert node1.next_node is None

    def test_dll_when_set_node_to_self(
            self,
            dll_manager_with_single_node: DllManager,
    ) -> None:
        node1 = dll_manager_with_single_node.get_node(node_id=1)

        with pytest.raises(NodeAlreadyExistException):
            dll_manager_with_single_node.set_node(node=node1, next_node=node1)
