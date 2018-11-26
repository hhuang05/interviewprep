term: Term.cpp
	clang++ -g -std=c++11 -c -o Term.o Term.cpp

variable:  Variable.cpp Variable.h 
	clang++ -g -std=c++11 -c -o Variable.o Variable.cpp

consts :  ConstantExprs.cpp ConstantExprs.h
	clang++ -g -std=c++11 -c -o ConstantExprs.o ConstantExprs.cpp

funcapp : FunctionApp.h FunctionApp.cpp
	clang++ -g -std=c++11 -c -o FunctionApp.o FunctionApp.cpp

funcdef : FunctionDef.h FunctionDef.cpp
	clang++ -g -std=c++11 -c -o FunctionDef.o FunctionDef.cpp

level1: term variable consts 

level2: funcapp funcdef

test: test.cpp
	clang++ -g -std=c++11 -o a.out Variable.o Term.o ConstantExprs.o FunctionApp.o FunctionDef.o test.cpp
