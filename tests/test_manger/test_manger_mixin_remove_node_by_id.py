import pytest

from algo_dll.exceptions import NodeDoesNotExistException
from algo_dll.manager import DllManager
from algo_dll.nodes import Node


class TestDllManagerMixinRemoveNodeById:

    def test_delete_first_node_by_id(
            self,
            dll_manager_filled: DllManager,
    ) -> None:
        node1 = dll_manager_filled.get_node(node_id=1)
        node2 = dll_manager_filled.get_node(node_id=2)
        node3 = dll_manager_filled.get_node(node_id=3)

        dll_manager_filled.remove_node_by_id(node_id=node1.id)

        # Check deleted node...
        assert node1.prev_node is None
        assert node1.next_node is None

        # Check node2...
        assert node2.prev_node is None
        assert node2.next_node == node3

        # Check node3...
        assert node3.prev_node == node2
        assert node3.next_node is None

    def test_delete_last_node_by_id(
            self,
            dll_manager_filled: DllManager,
    ) -> None:
        node1 = dll_manager_filled.get_node(node_id=1)
        node2 = dll_manager_filled.get_node(node_id=2)
        node3 = dll_manager_filled.get_node(node_id=3)

        dll_manager_filled.remove_node_by_id(node_id=node3.id)

        # Check deleted node...
        assert node1.prev_node is None
        assert node1.next_node == node2

        # Check node2...
        assert node2.prev_node == node1
        assert node2.next_node is None

        # Check node3...
        assert node3.prev_node is None
        assert node3.next_node is None

    def test_delete_middle_node_by_id(
            self,
            dll_manager_filled: DllManager,
    ) -> None:
        node1 = dll_manager_filled.get_node(node_id=1)
        node2 = dll_manager_filled.get_node(node_id=2)
        node3 = dll_manager_filled.get_node(node_id=3)

        dll_manager_filled.remove_node_by_id(node_id=node2.id)

        # Check deleted node...
        assert node1.prev_node is None
        assert node1.next_node == node3

        # Check node2...
        assert node2.prev_node is None
        assert node2.next_node is None

        # Check node3...
        assert node3.prev_node == node1
        assert node3.next_node is None

    def test_delete_single_node_by_id(
            self,
            dll_manager_with_single_node: DllManager,
    ) -> None:
        node1 = dll_manager_with_single_node.get_node(node_id=1)
        dll_manager_with_single_node.remove_node_by_id(node_id=node1.id)

        assert not dll_manager_with_single_node.node_map

        assert node1.prev_node is None
        assert node1.next_node is None

    def test_delete_does_not_exists_node_by_id(
            self,
            dll_manager_filled: DllManager,
    ) -> None:
        node1 = dll_manager_filled.get_node(node_id=1)
        node2 = dll_manager_filled.get_node(node_id=2)
        node3 = dll_manager_filled.get_node(node_id=3)

        node0 = Node(node_id=0)

        with pytest.raises(NodeDoesNotExistException):
            dll_manager_filled.remove_node_by_id(node_id=node0.id)

        # Check deleted node...
        assert node1.prev_node is None
        assert node1.next_node == node2

        # Check node2...
        assert node2.prev_node == node1
        assert node2.next_node == node3

        # Check node3...
        assert node3.prev_node == node2
        assert node3.next_node is None

    def test_delete_from_emptry_dll_by_id(
            self,
            dll_manager_empty: DllManager,
    ) -> None:
        with pytest.raises(NodeDoesNotExistException):
            dll_manager_empty.remove_node_by_id(node_id=1) is None
