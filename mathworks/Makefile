term: Term.cpp
	clang++ -std=c++11 -c -o Term.o Term.cpp

variable:  Variable.cpp Variable.h 
	clang++ -std=c++11 -c -o Variable.o Variable.cpp

consts :  ConstantExprs.cpp ConstantExprs.h
	clang++ -std=c++11 -c -o ConstantExprs.o ConstantExprs.cpp

test: test.cpp
	clang++ -std=c++11 -o a.out Variable.o Term.o test.cpp
