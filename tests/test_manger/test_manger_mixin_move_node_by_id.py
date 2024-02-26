import pytest

from algo_dll.exceptions import InvalidNextIdException
from algo_dll.manager import DllManager
from algo_dll.nodes import Node


class TestDllManagerMixinMoveNodeById:

    def test_dll_filled_when_move_last_node_to_first_by_id(
            self,
            dll_manager_empty: DllManager,
    ) -> None:
        node1: Node = Node(node_id=1)
        node2: Node = Node(node_id=2)
        node3: Node = Node(node_id=3)
        node0: Node = Node(node_id=0)

        dll_manager_empty.set_node(node=node1)
        dll_manager_empty.set_node(node=node2)
        dll_manager_empty.set_node(node=node3)
        dll_manager_empty.set_node(node=node0)

        dll_manager_empty.move_node_by_id(
            node_id=node0.id,
            next_node_id=node1.id,
        )

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

    def test_dll_filled_when_move_first_node_to_last_by_id(
            self,
            dll_manager_empty: DllManager,
    ) -> None:
        node4: Node = Node(node_id=4)
        node1: Node = Node(node_id=1)
        node2: Node = Node(node_id=2)
        node3: Node = Node(node_id=3)

        dll_manager_empty.set_node(node=node4)
        dll_manager_empty.set_node(node=node1)
        dll_manager_empty.set_node(node=node2)
        dll_manager_empty.set_node(node=node3)

        dll_manager_empty.move_node_by_id(node_id=node4.id)

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

    def test_dll_filled_when_move_first_node_to_middle_by_id(
            self,
            dll_manager_empty: DllManager,
    ) -> None:
        node3: Node = Node(node_id=3)
        node1: Node = Node(node_id=1)
        node2: Node = Node(node_id=2)
        node4: Node = Node(node_id=4)

        dll_manager_empty.set_node(node=node3)
        dll_manager_empty.set_node(node=node1)
        dll_manager_empty.set_node(node=node2)
        dll_manager_empty.set_node(node=node4)

        dll_manager_empty.move_node_by_id(
            node_id=node3.id,
            next_node_id=node4.id,
        )

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

    def test_dll_filled_when_move_last_node_to_middle_by_id(
            self,
            dll_manager_empty: DllManager,
    ) -> None:
        node1: Node = Node(node_id=1)
        node3: Node = Node(node_id=3)
        node4: Node = Node(node_id=4)
        node2: Node = Node(node_id=2)

        dll_manager_empty.set_node(node=node1)
        dll_manager_empty.set_node(node=node3)
        dll_manager_empty.set_node(node=node4)
        dll_manager_empty.set_node(node=node2)

        dll_manager_empty.move_node_by_id(
            node_id=node2.id,
            next_node_id=node3.id,
        )

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

    def test_dll_filled_when_move_middle_node_to_middle_by_id(
            self,
            dll_manager_empty: DllManager,
    ) -> None:
        node1: Node = Node(node_id=1)
        node3: Node = Node(node_id=3)
        node2: Node = Node(node_id=2)
        node4: Node = Node(node_id=4)

        dll_manager_empty.set_node(node=node1)
        dll_manager_empty.set_node(node=node3)
        dll_manager_empty.set_node(node=node2)
        dll_manager_empty.set_node(node=node4)

        dll_manager_empty.move_node_by_id(
            node_id=node2.id,
            next_node_id=node3.id,
        )

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

    def test_dll_when_two_node_replaced_by_id(
            self,
            dll_manager_empty: DllManager,
    ) -> None:
        node2: Node = Node(node_id=2)
        node1: Node = Node(node_id=1)

        dll_manager_empty.set_node(node=node2)
        dll_manager_empty.set_node(node=node1)

        dll_manager_empty.move_node_by_id(node_id=node2.id)

        # Check node1...
        assert node1.prev_node is None
        assert node1.next_node == node2

        # Check node2...
        assert node2.prev_node == node1
        assert node2.next_node is None

    def test_dll_when_move_node_to_self_by_id(
            self,
            dll_manager_empty: DllManager,
    ) -> None:
        node1: Node = Node(node_id=1)
        node2: Node = Node(node_id=2)

        dll_manager_empty.set_node(node=node1)
        dll_manager_empty.set_node(node=node2)

        with pytest.raises(InvalidNextIdException):
            dll_manager_empty.move_node_by_id(
                node_id=node2.id,
                next_node_id=node2.id,
            )

        # Check node1...
        assert node1.prev_node is None
        assert node1.next_node == node2

        # Check node2...
        assert node2.prev_node == node1
        assert node2.next_node is None
