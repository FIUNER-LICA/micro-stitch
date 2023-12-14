from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from pycallgraph2 import Config


with PyCallGraph(output=GraphvizOutput()):
    graphviz = GraphvizOutput()
    graphviz.output_file = 'large.png'
    config = Config(include_stdlib=False)

    with PyCallGraph(output=graphviz, config=config):
        import test_minimal