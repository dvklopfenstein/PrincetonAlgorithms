"""Brute-force substring search using the alternate brute-force implementation.

i points to end of sequence of already-matched chars in text
j stores # of already-matched chars (end of sequence in pattern

# i j i+j 0 1 2 3 4 5 6 7 8 9 10
# -|-|---|----------------------
#  | |   |A B A C A D A B R A C
# 7|3|  7|        A D A C
# 5|0|  4|          A

"""

def search(pat, txt):
    """Brute-force substring search using the alternate brute-force implementation"""
    len_txt = len(txt)
    len_pat = len(pat)
    txt_i = 0  # points to end of sequence of already-matched chars in text
    pat_j = 0  # stores # of already-matched chars (end of sequence in pattern
    while txt_i < len_txt:
        ##print(f'{txt_i:2} {pat_j:2} TXT({txt[txt_i]}) PAT({pat[pat_j]})')
        if txt[txt_i] == pat[pat_j]:
            pat_j += 1
        else:
            txt_i -= pat_j  # <-------------------- backup
            pat_j = 0
        if pat_j == len_pat:
            break
        txt_i += 1
    if pat_j == len_pat:
        return txt_i - len_pat + 1  # index in text where pattern starts
    return -1  # pattern not found in text (orig return = len_txt)
