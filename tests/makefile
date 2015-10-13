
PKG := test_WeightedQUF_state_pics
FNC := test_wk1_ex_166199

run:
	python -c 'import $(PKG); $(PKG).$(FNC)()'

ssst:
	echo "a b c d e f g" | test_SequentialSearchST.py

schst:
	echo "M=5 S E A R C H E X A M P L E" | test_SeparateChainingHashST.py

lphst:
	echo "M=5 S E A R C H E X A M P L E" | test_LinearProbingHashST.py

clobber:
	rm -f ./work/*.png
	rm -f *.png
