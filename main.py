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

    # FIXME: Tree looks wrong when rendered idky

    for f in range(2):
        F_id = f'.f_'
        id_so_far: str = F_id

        # Create and append the F node
        f_node = Node(F_id, content='F', shape='circle')
        nodes.append(f_node)

        f_valid, f_errors = make_assertions(F=f, should_print=False)
        if f_valid:
            for x3 in range(2):
                parent_node: Node
                curr_node: Node

                parent_node = f_node
                x3_id = f'{parent_node.id_}{f}.x3_'
                id_so_far = x3_id

                curr_node, nodes, node_ids = create_or_get_node(
                    nodes,
                    node_ids,
                    id_so_far,
                )

                x3_node = curr_node

                links, link_ids = update_links(
                    links=links,
                    link_ids=link_ids,
                    branch=f,
                    id_so_far=id_so_far,
                    parent_node=parent_node,
                    curr_node=curr_node,
                )

                x3_valid, x3_errors = make_assertions(
                    F=f,
                    x3=x3,
                    should_print=False,
                )
                if x3_valid:
                    for x2 in range(2):
                        parent_node = x3_node
                        x2_id = f'{parent_node.id_}{x3}.x2_'
                        id_so_far = x2_id

                        curr_node, nodes, node_ids = create_or_get_node(
                            nodes,
                            node_ids,
                            id_so_far,
                        )

                        x2_node = curr_node

                        links, link_ids = update_links(
                            links=links,
                            link_ids=link_ids,
                            branch=x3,
                            id_so_far=id_so_far,
                            parent_node=parent_node,
                            curr_node=curr_node,
                        )

                        x2_valid, x2_errors = make_assertions(
                            F=f,
                            x3=x3,
                            x2=x2,
                            should_print=False,
                        )

                        if x2_valid:
                            for x1 in range(2):
                                parent_node = x2_node
                                x1_id = f'{parent_node.id_}{x2}.x1_'
                                id_so_far = x1_id

                                curr_node, nodes, node_ids = create_or_get_node(
                                    nodes,
                                    node_ids,
                                    id_so_far,
                                )

                                x1_node = curr_node

                                links, link_ids = update_links(
                                    links=links,
                                    link_ids=link_ids,
                                    branch=x2,
                                    id_so_far=id_so_far,
                                    parent_node=parent_node,
                                    curr_node=curr_node,
                                )

                                x1_valid, x1_errors = make_assertions(
                                    F=f,
                                    x3=x3,
                                    x2=x2,
                                    x1=x1,
                                    should_print=False,
                                )

                                if x1_valid:
                                    for u in range(10):
                                        parent_node = x1_node
                                        u_id = f'{parent_node.id_}{x1}.u_'
                                        id_so_far = u_id

                                        curr_node, nodes, node_ids = create_or_get_node(
                                            nodes,
                                            node_ids,
                                            id_so_far,
                                        )

                                        u_node = curr_node

                                        links, link_ids = update_links(
                                            links=links,
                                            link_ids=link_ids,
                                            branch=x1,
                                            id_so_far=id_so_far,
                                            parent_node=parent_node,
                                            curr_node=curr_node,
                                        )

                                        u_valid, u_errors = make_assertions(
                                            F=f,
                                            x3=x3,
                                            x2=x2,
                                            x1=x1,
                                            U=u,
                                            should_print=False,
                                        )

                                        if u_valid:
                                            for r in range(10):
                                                parent_node = u_node
                                                r_id = f'{parent_node.id_}{u}.r_'
                                                id_so_far = r_id

                                                curr_node, nodes, node_ids = create_or_get_node(
                                                    nodes,
                                                    node_ids,
                                                    id_so_far,
                                                )

                                                r_node = curr_node

                                                links, link_ids = update_links(
                                                    links=links,
                                                    link_ids=link_ids,
                                                    branch=u,
                                                    id_so_far=id_so_far,
                                                    parent_node=parent_node,
                                                    curr_node=curr_node,
                                                )

                                                r_valid, r_errors = make_assertions(
                                                    F=f,
                                                    x3=x3,
                                                    x2=x2,
                                                    x1=x1,
                                                    U=u,
                                                    R=r,
                                                    should_print=False,
                                                )

                                                if r_valid:
                                                    for w in range(10):
                                                        parent_node = r_node
                                                        w_id = f'{parent_node.id_}{r}.w_'
                                                        id_so_far = w_id

                                                        curr_node, nodes, node_ids = create_or_get_node(
                                                            nodes,
                                                            node_ids,
                                                            id_so_far,
                                                        )

                                                        w_node = curr_node

                                                        links, link_ids = update_links(
                                                            links=links,
                                                            link_ids=link_ids,
                                                            branch=w,
                                                            id_so_far=id_so_far,
                                                            parent_node=parent_node,
                                                            curr_node=curr_node,
                                                        )

                                                        w_valid, w_errors = make_assertions(
                                                            F=f,
                                                            x3=x3,
                                                            x2=x2,
                                                            x1=x1,
                                                            U=u,
                                                            R=r,
                                                            W=w,
                                                            should_print=False,
                                                        )

                                                        if w_valid:
                                                            # TODO: Keep traversing the search space
                                                            # TODO: Do an early return, no need to keep traversing the search space lol
                                                            nodes.append(
                                                                valid_state
                                                            )
                                                            links.append(
                                                                Link(
                                                                    curr_node,
                                                                    valid_state,
                                                                    shape=LinkShape.NORMAL,
                                                                    head_left=LinkHead.NONE,
                                                                    head_right=LinkHead.ARROW,
                                                                    message=str(
                                                                        w),
                                                                )
                                                            )
                                                        elif len(w_errors) > 0:
                                                            nodes, links, error_nodes = update_fail_states(
                                                                nodes,
                                                                links,
                                                                error_nodes,
                                                                branch=w,
                                                                curr_node=curr_node,
                                                                failed_constraints=w_errors,
                                                            )
                                                        else:
                                                            raise ValueError(
                                                                'This should not happen, w is not valid and has no errors'
                                                            )
                                                elif len(r_errors) > 0:
                                                    nodes, links, error_nodes = update_fail_states(
                                                        nodes,
                                                        links,
                                                        error_nodes,
                                                        branch=r,
                                                        curr_node=curr_node,
                                                        failed_constraints=r_errors,
                                                    )
                                                else:
                                                    raise ValueError(
                                                        'This should not happen, r is not valid and has no errors'
                                                    )
                                        elif len(u_errors) > 0:
                                            nodes, links, error_nodes = update_fail_states(
                                                nodes,
                                                links,
                                                error_nodes,
                                                branch=u,
                                                curr_node=curr_node,
                                                failed_constraints=u_errors,
                                            )
                                        else:
                                            raise ValueError(
                                                'This should not happen, x1 is not valid and has no errors'
                                            )
                                elif len(x1_errors) > 0:
                                    nodes, links, error_nodes = update_fail_states(
                                        nodes,
                                        links,
                                        error_nodes,
                                        branch=x1,
                                        curr_node=curr_node,
                                        failed_constraints=x1_errors,
                                    )
                                else:
                                    raise ValueError(
                                        'This should not happen, x1 is not valid and has no errors'
                                    )
                        elif len(x2_errors) > 0:
                            nodes, links, error_nodes = update_fail_states(
                                nodes,
                                links,
                                error_nodes,
                                branch=x2,
                                curr_node=curr_node,
                                failed_constraints=x2_errors,
                            )
                        else:
                            raise ValueError(
                                'This should not happen, x2 is not valid and has no errors'
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
                f,
                f_node,
                f_errors,
            )

        else:
            raise ValueError(
                'This should not happen, F is not valid and has no errors'
            )

    return FlowChart(title, nodes, links)


def update_links(
    links: list[Link],
    link_ids: set[str],
    branch: int,
    id_so_far: str,
    parent_node: Node,
    curr_node: Node,
) -> tuple[list[Link], set[str]]:
    if id_so_far not in link_ids:
        link_ids.add(id_so_far)
        link = Link(
            parent_node,
            curr_node,
            shape=LinkShape.NORMAL,
            head_left=LinkHead.NONE,
            head_right=LinkHead.ARROW,
            message=str(branch),
        )

        links.insert(
            0,
            link,
        )

    return links, link_ids


def create_or_get_node(
    nodes: list[Node],
    node_ids: set[str],
    node_id: str,
) -> tuple[Node, list[Node], set[str]]:
    curr_node: Node

    # Get the last variable and ignore its branch value
    content: str = node_id.split('.')[-1].split('_')[0]

    # Create and append the x3 node
    if node_id not in node_ids:
        node_ids.add(node_id)
        curr_node = Node(node_id, content=content, shape='circle')
        nodes.insert(0, curr_node)
    else:
        # NOTE: This works because I modified the internal of `Node`, BE WEARY OF THIS
        # Basically I removed the conversion to snake case of the id_
        curr_node, *_ = [node for node in nodes if node.id_ == node_id]

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
