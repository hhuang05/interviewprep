#include "ConstantExprs.h"
#include "Variable.h"
#include "Term.h"
#include <iostream>
#include <vector>

int main()
{
  Variable *x1 = new Variable("x");
  Variable *y1 = new Variable("y");

  Variable *a1 = new Variable("a");
  Variable *b1 = new Variable("b");

  std::vector<Term*> *operands1 = new std::vector<Term*>();
  operands1->push_back(x1);
  operands1->push_back(y1);

  std::vector<Term*> *operands2 = new std::vector<Term*>();
  operands2->push_back(a1);
  operands2->push_back(b1);
  
  Operator *op1 = new Operator("+", operands1);
  Operator *op2 = new Operator("-", operands2);

  op1->dump();
  op2->dump();
  Term::IsIsomorphic(op1, op2);
}
