from algo_dll.nodes import Node
from algo_dll.partial_manager import PartialManager


class TestPartialManagerMoveNode:

    def test_move_from_last_to_first(self) -> None:
        node1: Node = Node(node_id=1)
        node4: Node = Node(node_id=4)
        node0: Node = Node(node_id=0)

        # Prepare node1...
        fake_node2 = Node(node_id='fake_node2')
        node1.next_node = fake_node2

        # Prepare node3...
        fake_node3 = Node(node_id='fake_node3')
        node4.prev_node = fake_node3
        node4.next_node = node0

        # Prepare node0...
        node0.prev_node = node4

        dll_manager = PartialManager()

        # Prepare dll...
        dll_manager.set_prepared_node(node=node1)
        dll_manager.set_prepared_node(node=node4)
        dll_manager.set_prepared_node(node=node0)

        dll_manager.last_node = node0

        # Action...
        dll_manager.move_node(node=node0, next_node=node1)

        # Check node0...
        assert node0.prev_node is None
        assert node0.next_node == node1

        # Check node1...
        assert node1.prev_node == node0
        assert node1.next_node == fake_node2

        # Check node3...
        assert node4.prev_node == fake_node3
        assert node4.next_node is None

        # # Check dll...
        # assert dll_manager.last_node == node4

    def test_move_from_first_to_last(self) -> None:
        node6: Node = Node(node_id=4)
        node1: Node = Node(node_id=1)
        node5: Node = Node(node_id=5)

        # Prepare node4...
        node6.next_node = node1

        # Prepare node1...
        node1.prev_node = node6
        fake_node2 = Node(node_id='fake_node2')
        node1.next_node = fake_node2

        # Prepare node3...
        fake_node4 = Node(node_id='fake_node4')
        node5.prev_node = fake_node4

        dll_manager = PartialManager()

        dll_manager.set_prepared_node(node=node6)
        dll_manager.set_prepared_node(node=node1)
        dll_manager.set_prepared_node(node=node5)

        # Prepare dll...
        dll_manager.last_node = node5

        dll_manager.move_node(node=node6)

        # Check node1...
        assert node1.prev_node is None
        assert node1.next_node == fake_node2

        # Check node5...
        assert node5.prev_node == fake_node4
        assert node5.next_node == node6

        # Check node6...
        assert node6.prev_node == node5
        assert node6.next_node is None

        # Check dll...
        assert dll_manager.last_node == node6

    def test_move_from_last_to_middle(self) -> None:
        """
        From: [node1, node3, ... , node10, node2]
        To: [node1, node2, node3, ... , node10]
        """

        node1: Node = Node(node_id=1)
        node3: Node = Node(node_id=3)
        node10: Node = Node(node_id=10)
        node2: Node = Node(node_id=2)

        # Prepare node1...
        node1.next_node = node3

        # Prepare node3...
        node3.prev_node = node1
        fake_node4 = Node(node_id='fake_node4')
        node3.next_node = fake_node4

        # Prepare node10...
        fake_node9 = Node(node_id='fake_node9')
        node10.prev_node = fake_node9
        node10.next_node = node2

        # Prepare node2...
        node2.prev_node = node10

        dll_manager = PartialManager()

        # Prepare dll...
        dll_manager.set_prepared_node(node=node1)
        dll_manager.set_prepared_node(node=node3)
        dll_manager.set_prepared_node(node=node10)
        dll_manager.set_prepared_node(node=node2)

        # Prepare dll...
        dll_manager.last_node = node2

        # Action...
        dll_manager.move_node(node=node2, next_node=node3)

        # Check node1...
        assert node1.prev_node is None
        assert node1.next_node == node2

        # Check node2...
        assert node2.prev_node == node1
        assert node2.next_node == node3

        # Check node3...
        assert node3.prev_node == node2
        assert node3.next_node == fake_node4

        # Check node10...
        assert node10.prev_node == fake_node9
        assert node10.next_node is None

        # # Check dll...
        # assert dll_manager.last_node == node10

    def test_move_from_first_to_middle(self) -> None:
        """
        From: [node9, node1, ... , node8, node10]
        To: [node1, ... , node8, node9, node10]
        """
        node9: Node = Node(node_id=9)
        node1: Node = Node(node_id=1)
        node8: Node = Node(node_id=8)
        node10: Node = Node(node_id=10)

        # Prepare node1...
        node9.next_node = node1

        # Prepare node2...
        node1.prev_node = node9
        fake_node2 = Node(node_id='fake_node2')
        node1.next_node = fake_node2

        # Prepare node8...
        fake_node7 = Node(node_id='fake_node7')
        node8.prev_node = fake_node7
        node8.next_node = node10

        # Prepare node10...
        node10.prev_node = node8

        dll_manager = PartialManager()

        # Prepare dll...
        dll_manager.set_prepared_node(node=node9)
        dll_manager.set_prepared_node(node=node1)
        dll_manager.set_prepared_node(node=node8)
        dll_manager.set_prepared_node(node=node10)

        # Prepare dll...
        dll_manager.last_node = node10

        # Action...
        dll_manager.move_node(node=node9, next_node=node10)

        # Check node1...
        assert node1.prev_node is None
        assert node1.next_node == fake_node2

        # Check node8...
        assert node8.prev_node == fake_node7
        assert node8.next_node == node9

        # Check node9...
        assert node9.prev_node == node8
        assert node9.next_node == node10

        # Check node10...
        assert node10.prev_node == node9
        assert node10.next_node is None

        # # Check dll...
        # assert dll_manager.last_node == node10

    def test_move_from_middle_to_middle(self) -> None:
        """
        From: [node1, node9, node2, ... , node8, node10]
        To: [node1, node2, ... , node8, node9, node10]
        """
        node1: Node = Node(node_id=1)
        node9: Node = Node(node_id=9)
        node2: Node = Node(node_id=2)
        node8: Node = Node(node_id=8)
        node10: Node = Node(node_id=10)

        # Prepare node1...
        node1.next_node = node9

        # Prepare node9...
        node9.prev_node = node1
        node9.next_node = node2

        # Prepare node2...
        node2.prev_node = node9
        fake_node3 = Node(node_id='fake_node3')
        node2.next_node = fake_node3

        # Prepare node8...
        fake_node7 = Node(node_id='fake_node7')
        node8.prev_node = fake_node7
        node8.next_node = node10

        # Prepare node10...
        node10.prev_node = node8

        dll_manager = PartialManager()

        # Prepare dll...
        dll_manager.set_prepared_node(node=node1)
        dll_manager.set_prepared_node(node=node9)
        dll_manager.set_prepared_node(node=node2)
        dll_manager.set_prepared_node(node=node8)
        dll_manager.set_prepared_node(node=node10)

        # Prepare dll...
        dll_manager.last_node = node10

        # Action...
        dll_manager.move_node(node=node9, next_node=node10)

        # Check node1...
        assert node1.prev_node is None
        assert node1.next_node == node2

        # Check node2...
        assert node2.prev_node == node1
        assert node2.next_node == fake_node3

        # Check node8...
        assert node8.prev_node == fake_node7
        assert node8.next_node == node9

        # Check node9...
        assert node9.prev_node == node8
        assert node9.next_node == node10

        # Check node10...
        assert node10.prev_node == node9
        assert node10.next_node is None
