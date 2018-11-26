#include "FunctionDef.h"
#include "FunctionApp.h"
#include "ConstantExprs.h"
#include "Variable.h"
#include "Term.h"
#include <iostream>
#include <vector>

int main()
{
  Variable *f1 = new Variable("f");
  Variable *x1 = new Variable("x");
  Variable *y1 = new Variable("y");
  Float *f1 = new Float(1.00);
  Float *f2 = new Float(2.00);
  Operator *op1 = new Operator("+");
  std::vector<Term*> *operands1 = new std::vector<Term*>();
  operands1->push_back(x1);
  operands1->push_back(f1);

  std::vector<Variable*> *vars1 = new std::vector<Variable*>();
  vars1->push_back(f1);
  
  FunctionApp *fn1 = new FunctionApp(op1, operands1);
  
  FunctionDef *fndef1 = new FunctionDef(vars1, fn1);

  // Second term
  Variable *g1 = new Variable("g");
  Variable *a1 = new Variable("a");
  Variable *b1 = new Variable("b");
  Float *f3 = new Float(1.00);
  Float *f4 = new Float(2.00);
  Operator *op2 = new Operator("+");
  
  std::vector<Term*> *operands2 = new std::vector<Term*>();
  operands2->push_back(f2);
  operands2->push_back(a1);

  FunctionApp *fn2 = new FunctionApp(op2, operands2);
  

  std::vector<Variable*> *vars2 = new std::vector<Variable*>();
  vars2->push_back(a1);
  
  
  FunctionDef *fndef2 = new FunctionDef(vars2, fn2);

  fndef1->dump("|-");
  fndef2->dump("|-");

  Term::IsIsomorphic(fndef1, fndef2);
}
