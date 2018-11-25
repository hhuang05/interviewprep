#include "FunctionApp.h"
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

  Float *f1 = new Float(1.00);
  Float *f2 = new Float(1.01);

  std::vector<Term*> *operands1 = new std::vector<Term*>();
  operands1->push_back(x1);
  operands1->push_back(f1);

  std::vector<Term*> *operands2 = new std::vector<Term*>();
  operands2->push_back(a1);
  operands2->push_back(f2);
  
  Operator *op1 = new Operator("+");
  Operator *op2 = new Operator("+");

  FunctionApp *fn1 = new FunctionApp(op1, operands1);
  FunctionApp *fn2 = new FunctionApp(op2, operands2);
  
  fn1->dump();
  fn2->dump();
  
  // Term::IsIsomorphic(op1, op2);
}
