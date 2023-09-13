"""Brute-force substring search using brute-force.

"Fine in many contexts and actually is the one Java's indexOf uses
 but the problem is it can be slow if there is a lot of repeatitive
 characters in the text and the pattern"

# Check for pattern starting at each text position

# i j i+j 0 1 2 3 4 5 6 7 8 9 10
# -|-|---|----------------------
#  | |   |A B A C A D A B R A C
# 4|3|  7|        A D A C
# 5|0|  4|          A

"""

def search(pat, txt):
    """Search text for a pattern using brute-force"""
    # Worst case (repetitive characters) ~MN
    len_txt = len(txt)
    len_pat = len(pat)
    for txt_i in range(len_txt - len_pat + 1):
        pat_match = True
        for pat_j in range(len_pat):
            #print(f'{txt_i:2} {pat_j:2} TXT({txt[txt_i + pat_j]}) PAT({pat[pat_j]})')
            if txt[txt_i + pat_j] != pat[pat_j]:
                pat_match = False
                break
        if pat_match:
            return txt_i  # index in text where pattern starts
    return -1  # pattern not found in text (orig return = len_txt)
