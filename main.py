from mermaid.flowchart.node import Node, NODE_SHAPES
from mermaid.flowchart.link import Link, LinkShape, LinkHead
from mermaid.flowchart import FlowChart

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

    return FlowChart(title, nodes, links)
