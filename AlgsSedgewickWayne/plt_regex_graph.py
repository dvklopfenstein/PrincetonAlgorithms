"""Create plot of regex NFA state machine and write into a png file"""

import pydot

def plt_nfa(fout_png, nfa):
    """Create plot of regex NFA state machine and write into a png file"""
    digraph = nfa.digraph
    regexp = nfa.regexp
    # 1. Create/initialize Graph
    dotgraph = pydot.Dot(graph_type='digraph',
                        label=f'{regexp} [{len(regexp)}]',
                        rankdir='LR')
    # 2. Create Nodes
    regchrs = list(regexp) + ['MATCH',]
    assert len(regchrs) == len(digraph.keys)
    #nodes = [pydot.Node(src_v, label=f'{src_v}\n{a}') for a, src_v in zip(regchrs, digraph.keys)]
    #nodes = [pydot.Node(src_v, label=f'{src_v} ??') for src_v in digraph.keys]
    # 3. Add nodes to Graph
    prev_i = -1
    prev_chr = -1
    rngs = [('a', 'z'), ('A', 'Z'), ('0', '9')]
    az09 = set(chr(i) for a, z in rngs for i in range(ord(a), ord(z) + 1))
    ## print('ALPHANUMERIC CHRS:', sorted(az09))
    for reg_i, reg_chr in enumerate(regexp):
        node = pydot.Node(reg_i, label=f'{reg_i}\n{reg_chr}')
        dotgraph.add_node(node)
        if prev_chr in az09:
            dotgraph.add_edge(pydot.Edge(prev_i, reg_i, color='black'))
        prev_i = reg_i
        prev_chr = reg_chr
    #for node in nodes:
    #    dotgraph.add_node(node)
    # 4. Add Edges between Nodes to Graph
    for src_v, dst_w in digraph.get_edges():
        if src_v != dst_w: # Print only edges from one node to another (not to self)
            #print(f'{src_v} {dst_w}')
            dotgraph.add_edge(pydot.Edge(src_v, dst_w, color='red'))
    # Add invisible edge to line up states in order in plot
    for src_v, src_vp1 in zip(digraph.keys[:-1], digraph.keys[1:-2]):
        dotgraph.add_edge(pydot.Edge(src_v, src_vp1, color='blue', style='invis'))#'dotted'))
    dotgraph.write_png(fout_png)
    print(f"  WROTE: {fout_png}")
