"""A module for helping to visualize array sorting."""

# Copyright (C) 2014-2019, DV Klopfenstein
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys
import copy
import collections as cx

from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def run(container, seqstr, expected=None, prt=sys.stdout, prt_details=sys.stdout):
    """Run a sequence of Stack commands."""
    lst = cli_get_array(seqstr)
    result = run_list(container, lst, prt_details)
    if expected is not None:
        passed = result == expected
        pass_fail = "   Pass" if passed else " **FAIL"
        #prt.write("{}: EXP({}) ACTUAL({}) from seq: {}\n".format(
        prt.write("{PF} GIVEN({SEQ}) -> ACTUAL({ACT})".format(
            PF=pass_fail, ACT=result, SEQ=seqstr))
        if not passed:
            prt.write(" EXPECTED({})".format(expected))
        prt.write("\n")

def run_list(container, item_list, prt=sys.stdout):
    """Inserts items in a string into a container. Prints steps. Returns end state."""
    if prt is not None:
        prt.write("\nINPUT: {}\n".format(' '.join([str(item) for item in item_list])))
    result = []
    for item in item_list:
        if item != "-":
            container.push(item)
            if prt is not None:
                prt.write("{:10}   PUSH {:10} +STACK: {}\n".format("", item, container))
        elif not container.isEmpty():
            popped = container.pop()
            result.append(popped)
            if prt is not None:
                prt.write("{:>10} <-POP  {:10} -STACK: {}\n".format(popped, item, container))
    if prt is not None:
        prt.write('({} left on stack)\n'.format(container.size()))
    return ' '.join([str(item) for item in result])

def run_Queue(container, seqstr, prt=sys.stdout):
    """Inserts items in a string into a container."""
    return run_Queue_list(container, cli_get_array(seqstr), prt)

def run_Queue_list(container, item_list, prt=sys.stdout):
    """Inserts items in a string into a container. Prints steps. Returns end state."""
    prt.write("\nINPUT: {}\n".format(' '.join([str(item) for item in item_list])))
    result = []
    for item in item_list:
        if item != "-":
            container.enqueue(item)
            prt.write("{:10}   ENQUEUE {:10} +QUEUE: {}\n".format("", item, container))
        elif not container.isEmpty():
            popped = container.dequeue()
            result.append(popped)
            prt.write("{:>10} <-DEQUQUE {:10} -QUEUE: {}\n".format(popped, item, container))
    prt.write('({} left on stack)\n'.format(container.size()))
    return ' '.join([str(item) for item in result])

def ex_stdin(container, prt=sys.stdout):
    """Read a string sequence from STDIN."""
    result = ""
    while True:
        item = raw_input('TYPE WORDS OR -')
        if not item:
            break
        if item != "-":
            container.push(item)
        elif not container.isEmpty():
            result = ' '.join([result, container.pop()])
    prt.write('(%d left on stack) OUTPUT: %container\n'%(container.size(), result))

def chk(arr0, txt):
    """Check that arrays are equal"""
    arr1 = txt.split()
    return arrays_equal(arr0, arr1)

def arrays_equal(arr0, arr1):
    """TBD: Remove?"""
    len_a = len(arr0)
    return len_a == len(arr1) and len_a == sum([1 for i, j in zip(arr0, arr1) if i == j])

def history_contains(array_history, potential_midpoint):
    """ Tests if a midpoint could have occured sometime during a sort."""
    for arrobj in array_history:
        if arrays_equal(arrobj[0], potential_midpoint):
            return True
    return False

def get_keystr(elem):
    """TBD"""
    if elem is None:
        return "."
    if isinstance(elem, dict):
        if len(elem) == 1:
            return str(elem.keys()[0])
        raise Exception('TIME TO IMPLEMENT MUTIPLE KEYS')
    return elem

def get_elem2num(array_history):
    """ 1 is assigned to smallest element.  len(arr)+1 is assigned to largest element."""
    # In array_history, last array should be the sorted arrayA
    array_sorted = sorted(array_history[-1][0])
    elem2num = {'.': 0} # '.' is a space-holder for an element being "None"
    num = 1
    for elem in array_sorted: # Loop on elements in last sorted array
        elem2num[get_keystr(elem)] = num
        num += 1
    return elem2num

def get_anno(idx, idx2sym):
    """TBD"""
    if idx2sym is None or idx not in idx2sym:
        return ' '
    return idx2sym[idx]

def xor_txt(txt_prev, txt_curr):
    """Xor two strings. Return string w/matches('.') and mismatches('X')"""
    ord_xor = [ord(a) ^ ord(b) for a, b in zip(txt_prev, txt_curr)]
    lst = []
    for match_result, letter in zip(ord_xor, txt_curr):
        if letter == ' ':
            lst.append(' ')
        # characters match
        elif match_result == 0:
            lst.append('.')
        # characters mismatch
        else:
            lst.append('X')
    return ''.join(lst)

class ArrayHistory:
    """Class to manage array history for visualization and learning."""

    def __init__(self):
        self.ntarr = cx.namedtuple("NtArr", "array_st anno")
        self.array_histories = cx.defaultdict(list)
        self.ah_names = []
        self.width = None # Width for printing each array element

    def add_history(self, array, anno, name='a'):
        """Add current array state to array history."""
        if name not in self.ah_names:
            self.ah_names.append(name)
        self.array_histories[name].append(self.ntarr._make([copy.deepcopy(array), anno]))
        # TBD: Remove
        #for name in self.array_histories:
        #  for state in self.array_histories[name]:
        #    print "SSSS", name, state

    def __iter__(self):
        for name in self.ah_names:
            for array_state in self.array_histories[name]:
                yield array_state

    def prt(self, prt=sys.stdout):
        """ Prints array history with spaces between elements."""
        txt_prev = None
        txt_curr = None
        self._set_elem_width()
        for name in self.ah_names:
            for idx, arrobj in enumerate(self.array_histories[name]):
                txt_prev = txt_curr
                txt_curr = self.get_array_str(arrobj.array_st)
                if txt_prev is not None:
                    txt_mtch = xor_txt(txt_prev, txt_curr)
                    prt.write('    {}\n'.format(txt_mtch))
                prt.write('{I:2d}: {STATE} <= {NAME}\n'.format(I=idx, STATE=txt_curr, NAME=name))
            prt.write("\n")


    def prt_intlvd(self, prt=sys.stdout):
        """ Prints array history with spaces between elements."""
        ah_names = self.ah_names
        txt_prev = {name:None for name in ah_names}
        txt_curr = {name:None for name in ah_names}
        self._set_elem_width()
        arrs = [self.array_histories[name] for name in ah_names]
        for incr, ntarrs in enumerate(zip(*arrs)):
            for name, ntarr in zip(ah_names, ntarrs):
                #print incr, name, ntarr, get_array_str(ntarr.array_st)
                txt_prev[name] = txt_curr[name]
                txt_curr[name] = self.get_array_str(ntarr.array_st)
                if ntarr.anno is not None:
                    prt.write('{IDX:2d}: {ANNO} <= {NAME} {DICT}\n'.format(
                        IDX=incr,
                        ANNO=self.get_anno_str(ntarr),
                        NAME=name,
                        DICT=self.get_anno_val_str(ntarr)))
                if txt_prev[name] is not None:
                    txt_mtch = xor_txt(txt_prev[name], txt_curr[name])
                    prt.write('    {DIFF} <= {NAME} compare\n'.format(DIFF=txt_mtch, NAME=name))
                prt.write('{IDX:2d}: {STATE} <= {NAME}\n'.format(
                    IDX=incr, STATE=txt_curr[name], NAME=name))
            prt.write("\n")

    def show(self, desc, prt=sys.stdout):
        """ Print array history plus horizontal histogram bars to help visualize sort."""
        for name in self.ah_names:
            array_history = self.array_histories[name]
            self._show_array_history(array_history, name, desc, prt)
        # TBD: Put array histories side-by-side
        #ahs = cx.OrderedDict([(name, self.array_histories[name]) for name in self.ah_names])
        #for name, ahs in ahs.items():
        #  for array_history in zip(*ahs):
        #    print "LLLL", name, len(array_history)

    @staticmethod
    def _show_array_history(array_history, name, desc, prt):
        """Show array history"""
        if isinstance(array_history, list) and array_history:
            elem2num = get_elem2num(array_history)
            for incr, arrobj in enumerate(array_history):
                astr = [str(item) for item in arrobj.array_st]
                prt.write('{} {:2d} {}: {}\n'.format(name, incr, desc, ' '.join(astr)))
                for idx, elem in enumerate(arrobj.array_st):
                    anno = get_anno(idx, arrobj.anno)
                    prt.write('{} {:2d} {}({:2d}): {}{:2} {}\n'.format(
                        name, incr, desc, idx, anno, elem,
                        ''.join(['*']*elem2num[get_keystr(elem)])))
                prt.write('\n')

    def _set_elem_width(self):
        """Set elem width to str length of largest elem."""
        if self.width is not None:
            return
        width = 1
        for hist_lst in self.array_histories.values():
            for ntarr in hist_lst:
                for elem in ntarr.array_st:
                    if elem is not None:
                        width = max(width, len(str(elem)))
        self.width = width

    def get_array_str(self, array_st):
        """Given: ['E', 'G', None, None], return "E G _ _"."""
        fnc = lambda item: str(item) if item is not None else "_"*self.width
        # Each element is self.width wide
        return ' '.join(["{:{}}".format(fnc(item), self.width) for item in array_st])

    def get_anno_str(self, ntarr):
        """Given an NtArr, return symbols above indices."""
        getval = lambda i: '.'*self.width  if i not in ntarr.anno else ntarr.anno[i]
        valarr = ["{:{}}".format(getval(i), self.width) for i in range(len(ntarr.array_st))]
        return ' '.join(valarr)

    @staticmethod
    def get_anno_val_str(ntarr):
        """Get string representation of array"""
        return ", ".join(["({} {})".format(i, s) for i, s in ntarr.anno.items()])
