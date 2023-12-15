from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from pycallgraph2 import Config



my_output = GraphvizOutput()
my_output.output_file = 'test_minimal.png'
config = Config(include_stdlib=False)

with PyCallGraph(output=my_output, config=config):
    import test_minimal