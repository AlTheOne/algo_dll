# ALGO Doubly Linked List

Simple toolkit for use doubly linked list.


## Features

- Provide tools for strict dll and partial dll
- Simple and written on Python
- Enforces better architecture


## Installation

```sh
pip install algo_dll
```

## Simple dll

```python
from algo_dll.dll_manager import DllManager
from algo_dll.nodes import Node

node1 = Node(node_id=1)
node2 = Node(node_id=2)
node0 = Node(node_id=0)

dll_manager = DllManager()

dll_manager.set_node(node=node1)
dll_manager.set_node(node=node2)
dll_manager.set_node(node=node0)

dll_manager.move_node(node=node0, next_node=node1)

_node0 = dll_manager.get_node(node_id=0)
assert _node0 == node0

_node1 = _node0.next_node
assert _node1 == node1

_node2 = _node0.next_node.next_node
assert _node2 == node2

_node3 = _node2.next_node
assert _node3 == node3
```
