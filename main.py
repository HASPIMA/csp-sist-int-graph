from mermaid.flowchart import FlowChart
from mermaid.flowchart.link import Link, LinkHead, LinkShape
from mermaid.flowchart.node import Node

from checks import BaseCheck

'''
NOTE: This may be useful for the implementation of the flowchart
(Normal nodes) id: should be of the form ".F_0.X3_0.X2_0.X1_0.U_6.R_5.W_4.T_3.O_9" where the numbers are the iteration number/value and . is the separator for variables
(Error nodes) id: should contain a hash of the error message and the depth in the tree, still don't know how to do it lmao. Problem for future Harrison


Build FlowChart after all nodes and links have been associated
'''


def generate_diagram() -> FlowChart:
    title: str = 'Constraint Satisfaction Problem'
    nodes: list[Node] = []
    links: list[Link] = []

    error_nodes: dict[str, Node] = {}

    return FlowChart(title, nodes, links)


def update_fail_states(
    nodes: list[Node],
    links: list[Link],
    error_nodes: dict[str, Node],
    branch: int,
    curr_node: Node,
    failed_constraints: list[BaseCheck],
) -> tuple[list[Node], list[Link], dict[str, Node]]:
    curr_error: BaseCheck = failed_constraints[0]
    curr_node_id = curr_node.id_

    # Error node id is depth on the tree and a hash of the constraint type
    h = hash(curr_error.check)
    tmp_err_id = f'{curr_node_id[:-1]}.err_{h}'

    #

    error_node: Node

    if tmp_err_id not in error_nodes:
        error_nodes[tmp_err_id] = Node(
            tmp_err_id,
            content=str(curr_error),
            shape='round-edge',
        )

        # Append the error node if it's the first time we've seen it
        nodes.append(error_nodes[tmp_err_id])

    error_node = error_nodes[tmp_err_id]

    # Append the link to the error node from the F node
    links.append(
        Link(
            curr_node,
            error_node,
            shape=LinkShape.NORMAL,
            head_left=LinkHead.NONE,
            head_right=LinkHead.ARROW,
            message=str(branch),
        )
    )

    return nodes, links, error_nodes
