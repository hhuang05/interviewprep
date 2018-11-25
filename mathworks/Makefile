term: Term.h Term.cpp
	clang++ -std=c++11 -c -o Term.o Term.cpp

variable:  Variable.cpp Variable.h Term.o
	clang++ -std=c++11 -c -o Variable.o Term.o Variable.cpp

test: test.cpp
	clang++ -std=c++11 -o a.out Variable.o Term.o test.cpp
