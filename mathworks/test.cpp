#include "FunctionDef.h"
#include "FunctionApp.h"
#include "ConstantExprs.h"
#include "Variable.h"
#include "Term.h"
#include <iostream>
#include <vector>

/* getFirstTerm - Gets the first term by replacing variable names
 * 
 */
Term *getFirstTerm(std::string varName)
{  
  // First term: 'f'(f 1.0 2.0)
  Variable *v1 = new Variable(varName);
  Float *f1 = new Float(1.00);
  Float *f2 = new Float(2.00);
  
  std::vector<Term*> *operands1 = new std::vector<Term*>();
  operands1->push_back(f1);
  operands1->push_back(f2);

  std::vector<Variable*> *vars1 = new std::vector<Variable*>();
  vars1->push_back(v1);
  
  FunctionApp *fn1 = new FunctionApp(v1, operands1);
  FunctionDef *fndef1 = new FunctionDef(vars1, fn1);
  
  return fndef1;
}

/* getSecondTerm - Gets the first term by replacing variable names
 * 
 */
Term *getSecondTerm(std::string var1, std::string var2)
{
  // Second term
  Variable *v1 = new Variable(var1);
  Variable *v2 = new Variable(var2);
  Operator *op2 = new Operator("+");
  
  std::vector<Term*> *operands2 = new std::vector<Term*>();
  operands2->push_back(v1);
  operands2->push_back(v2);

  FunctionApp *fn2 = new FunctionApp(op2, operands2);
  
  std::vector<Variable*> *vars2 = new std::vector<Variable*>();
  vars2->push_back(v1);
  vars2->push_back(v2);
  
  FunctionDef *fndef2 = new FunctionDef(vars2, fn2);
  return fndef2;
}

/* getSecondTermFlip - Gets the first term by replacing variable names
 * 
 */
Term *getSecondTermFlip(std::string var1, std::string var2)
{
  // Second term
  Variable *v1 = new Variable(var1);
  Variable *v2 = new Variable(var2);
  Operator *op2 = new Operator("+");
  
  std::vector<Term*> *operands2 = new std::vector<Term*>();
  operands2->push_back(v2);
  operands2->push_back(v1);

  FunctionApp *fn2 = new FunctionApp(op2, operands2);
  
  std::vector<Variable*> *vars2 = new std::vector<Variable*>();
  vars2->push_back(v1);
  vars2->push_back(v2);
  
  FunctionDef *fndef2 = new FunctionDef(vars2, fn2);
  return fndef2;
}

bool test_Variables()
{
  Variable *v1 = new Variable("x");
  Variable *v2 = new Variable("y");

  return Term::IsIsomorphic(v1, v2);
}

bool test_Floats()
{
  Float *v1 = new Float(1.00);
  Float *v2 = new Float(1.00);

  return Term::IsIsomorphic(v1, v2);
}

bool test_FunctionApp()
{
  Variable *v1 = new Variable("x");
  Variable *v2 = new Variable("y");
  Operator *op1 = new Operator("+");
  
  std::vector<Term*> *operands1 = new std::vector<Term*>();
  operands1->push_back(v1);
  operands1->push_back(v2);
  FunctionApp *fn1 = new FunctionApp(op1, operands1);

  Variable *v3 = new Variable("a");
  Variable *v4 = new Variable("b");
  Operator *op2 = new Operator("+");
  
  std::vector<Term*> *operands2 = new std::vector<Term*>();
  operands2->push_back(v3);
  operands2->push_back(v4);
  FunctionApp *fn2 = new FunctionApp(op2, operands2);
  
  return Term::IsIsomorphic(fn1, fn2);
}

bool test_FunctionDef()
{
  Term *xy_term = getSecondTerm("x", "y");
  Term *ab_term = getSecondTerm("a", "b");

  return Term::IsIsomorphic(xy_term, ab_term);
}

// Expect to pass
bool test_IsomorphicPass()
{
  Term *f_term = getFirstTerm("f");
  Term *xy_term = getSecondTerm("x", "y");

  Term *g_term = getFirstTerm("g");  
  Term *ab_term = getSecondTerm("a", "b");

  f_term->dump();
  g_term->dump();
  bool firstTermR = Term::IsIsomorphic(f_term, g_term);
  std::cout << "First :" << firstTermR << std::endl;
  
  std::vector<Term*> ops1 {xy_term};
  std::vector<Term*> ops2 {ab_term};
  
  FunctionApp *newFn1 = new FunctionApp(f_term, &ops1);
  FunctionApp *newFn2 = new FunctionApp(g_term, &ops2);
  
  return firstTermR;
}

// Expect to NOT be isomorphic since order of variables changed
bool test_VarOrderChanged()
{
  Term *f_term = getFirstTerm("f");
  Term *xy_term = getSecondTerm("x", "y");

  Term *g_term = getFirstTerm("g");  
  Term *ab_term = getSecondTermFlip("a", "b");

  std::vector<Term*> ops1 {xy_term};
  std::vector<Term*> ops2 {ab_term};
  
  FunctionApp *newFn1 = new FunctionApp(f_term, &ops1);
  FunctionApp *newFn2 = new FunctionApp(g_term, &ops2);

  newFn1->dump();
  newFn2->dump();
  
  return Term::IsIsomorphic(newFn1, newFn2);
}

int main()
{
  bool variables = test_Variables();
  bool floats = test_Floats();
  bool funcApp = test_FunctionApp();
  bool funcDef = test_FunctionDef();
  bool varIsIsomorphic = test_IsomorphicPass();
  bool varOrderResult = test_VarOrderChanged();
  
  std::cout << "Test Results         | Expected | Actual " << std::endl;
  std::cout << "test_Variables       | 1        | " << variables << "      " << std::endl;
  std::cout << "test_Floats          | 1        | " << floats << "      " << std::endl;
  std::cout << "test_FuncApp         | 1        | " << funcApp << "      " << std::endl;
  std::cout << "test_FuncDef         | 1        | " << funcDef << "      " << std::endl;
  std::cout << "test_IsIsomorphic    | 1        | " << varIsIsomorphic << "      " << std::endl;
  std::cout << "test_VarOrderChanged | 0        | " << varOrderResult << "      " << std::endl;
  
}
