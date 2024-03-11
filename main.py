from mermaid.flowchart import FlowChart
from mermaid.flowchart.link import Link, LinkHead, LinkShape
from mermaid.flowchart.node import Node

from checks import BaseCheck
from utils import make_assertions

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
    link_ids: set[str] = set()
    node_ids: set[str] = set()

    error_nodes: dict[str, Node] = {}

    valid_state = Node('valid', content='Valid State', shape='round-edge')

    for F in range(10):
        F_id = f'.F_'
        id_so_far = F_id

        # Create and append the F node
        f_node = Node(F_id, content='F', shape='circle')
        nodes.append(f_node)

        f_valid, f_errors = make_assertions(F=F, should_print=False)
        if f_valid:
            for x3 in range(10):
                x3_id = f'{id_so_far}{F}.x3_'
                id_so_far = x3_id

                parent_node: Node
                curr_node: Node

                parent_node = f_node
                curr_node, nodes, node_ids = create_or_get_node(
                    nodes,
                    node_ids,
                    id_so_far,
                )

                if id_so_far not in link_ids:
                    link_ids.add(id_so_far)
                    link = Link(
                        parent_node,
                        curr_node,
                        shape=LinkShape.NORMAL,
                        head_left=LinkHead.NONE,
                        head_right=LinkHead.ARROW,
                        message=str(F),
                    )

                    links.insert(
                        0,
                        link
                    )

                x3_valid, x3_errors = make_assertions(
                    F=F,
                    x3=x3,
                    should_print=False,
                )
                if x3_valid:
                    # TODO: Keep traversing the search space
                    # TODO: Do an early return, no need to keep traversing the search space lol
                    nodes.append(valid_state)
                    links.append(
                        Link(
                            curr_node,
                            valid_state,
                            shape=LinkShape.NORMAL,
                            head_left=LinkHead.NONE,
                            head_right=LinkHead.ARROW,
                            message=str(x3),
                        )
                    )
                elif len(x3_errors) > 0:
                    nodes, links, error_nodes = update_fail_states(
                        nodes,
                        links,
                        error_nodes,
                        branch=x3,
                        curr_node=curr_node,
                        failed_constraints=x3_errors,
                    )
                else:
                    raise ValueError(
                        'This should not happen, x3 is not valid and has no errors'
                    )

        elif len(f_errors) > 0:
            nodes, links, error_nodes = update_fail_states(
                nodes,
                links,
                error_nodes,
                F,
                f_node,
                f_errors,
            )

        else:
            raise ValueError(
                'This should not happen, F is not valid and has no errors'
            )

    return FlowChart(title, nodes, links)


def create_or_get_node(
    nodes: list[Node],
    node_ids: set[str],
    id_so_far: str,
) -> tuple[Node, list[Node], set[str]]:
    curr_node: Node

    # Create and append the x3 node
    if id_so_far not in node_ids:
        node_ids.add(id_so_far)
        curr_node = Node(id_so_far, content='x3', shape='circle')
        nodes.insert(0, curr_node)
    else:
        # NOTE: This works because I modified the internal of `Node`, BE WEARY OF THIS
        # Basically I removed the conversion to snake case of the id_
        curr_node, *_ = [node for node in nodes if node.id_ == id_so_far]

    return curr_node, nodes, node_ids


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


if __name__ == '__main__':
    chart = generate_diagram()
    chart.save()
