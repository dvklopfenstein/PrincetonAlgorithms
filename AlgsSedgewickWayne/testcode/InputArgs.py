"""Get input from STDIN or from text"""

import sys
import os
import fileinput
import re


def cli_get_array(seqstr=None):
    """Command-line interface: reads data from arg, stdin, stream, or files."""
    # Example: print(cli_get_array("9 1 6 3 8 5 2"))
    num_args = len(sys.argv)
    if seqstr is not None and num_args == 1:
        if isinstance(seqstr, int):
            return seqstr
        if os.path.isfile(seqstr):
            return cli_get_fin(seqstr)
        return arr_int_str(seqstr.split(" "))
    # >>> [file.py] "A B C D E F"
    # >>> [file.py] "1 2 3 4 5 6"
    if num_args == 2 and not os.path.isfile(sys.argv[1]):
        arg = arr_int_str(sys.argv[1].split(" "))
        if arg is not None:
            return arg
    # >>> echo "A B C D E F" | [file.py]
    # >>> echo "1 2 3 4 5 6" | [file.py]
    # >>> [file.py] # And then enter elems 1 at arg time on stdin. End with two ctrl-Ds
    arg = [w.strip(" \n\r") for t in fileinput.input() for w in t.splitlines()]
    if len(arg) == 1 and re.search(r'[(\S+\s+)]+', arg[0]):
        return arr_int_str(arg[0].split(" "))
    # >>> test_Quick.py ../thirdparty/1Kints.txt
    return arr_int_str(arg) if arg is not None else None

def cli_get_fin(fin):
    """Get array from file"""
    with open(fin) as ifstrm:
        arg = []
        for line in ifstrm:
            line = line.strip(" \n\r")
            if line:
                #flds = line.split(" ")
                flds = re.findall(r'(\S+)', line)
                elem = arr_int_str(flds)
                arg.append(elem[0] if len(elem) == 1 else elem)
        # If all input is on one line...
        if len(arg) == 1: # Ex: [['she', 'sells', 'sea', 'shells', ...]]
            return arg[0] # Return ['she', 'sells', 'sea', 'shells', ...]
    return arg

def arr_int_str(arg):
    """Return an array of ints or strs."""
    isdigit = True
    for elem in arg:
        mtch = re.search(r'^([0-9.\-eE ]+)$', elem)
        if not mtch:
            isdigit = False
            break
    if not isdigit:
        return arg
    if isdigit:
        return conv_num(arg)
    return None

def conv_num(arr):
    """Convert digits stored as strings to numbers"""
    #  GET: ['13', '13', '0 5', '4 3', ...
    #  RET: [ 13,   13,  [0, 5], [4, 3], ...
    nums = []
    #### conv = lambda s: float(s) if "." in s or 'e' in s.lower() else int(s)
    for elem in arr:
        elem = elem.strip() # strip leading/trailing whitespace
        if ' ' not in elem:
            nums.append(_conv(elem))
        else:
            nums.append([_conv(e) for e in re.findall(r'(\S+)', elem)])
    return nums

def _conv(txt):
    """Convert string to float, int, or return a string"""
    if '.' in txt:
        return float(txt)
    if 'e' in txt.lower():
        return float(txt)
    if txt.isdigit():
        return int(txt)
    return txt

def _prt_usage_msg(default_seq="a f b d g e c"):
    import inspect
    # Get the name of the calling script (or module, i.e. mod)
    frm = inspect.stack()[2]
    mod = inspect.getmodule(frm[0])
    # Let the user know that they can provide a sequence at run-time.
    print("""
      You may provide a list of elements on the command line.  For example:

        {CMD} "{SEQ}"

    """.format(CMD=mod.__file__, SEQ=default_seq))
