CC=g++

all: 	level1 level2 test

level1: term variable consts 

level2: funcapp funcdef

term: Term.cpp
	$(CC) -g -std=c++11 -c -o Term.o Term.cpp

variable:  Variable.cpp Variable.h 
	$(CC) -g -std=c++11 -c -o Variable.o Variable.cpp

consts :  ConstantExprs.cpp ConstantExprs.h
	$(CC) -g -std=c++11 -c -o ConstantExprs.o ConstantExprs.cpp

funcapp : FunctionApp.h FunctionApp.cpp
	$(CC) -g -std=c++11 -c -o FunctionApp.o FunctionApp.cpp

funcdef : FunctionDef.h FunctionDef.cpp
	$(CC) -g -std=c++11 -c -o FunctionDef.o FunctionDef.cpp

test: IRTest.cpp
	$(CC) -g -std=c++11 -o IRTest Variable.o Term.o ConstantExprs.o FunctionApp.o FunctionDef.o IRTest.cpp

clean:
	rm *.o IRTest
