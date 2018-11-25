#include "Variable.h"
#include "Term.h"
#include <iostream>

bool Term::IsIsomorphic(Term *a, Term *b)
{
  if (Variable *v1 = dynamic_cast<Variable*>(a)) {
    if (Variable *v2 = dynamic_cast<Variable*>(b)) {
      return true;
    }
  } else {
    std::cout << "Both terms do not agree" << std::endl;
  }
  
  return false;
}

int main()
{
  Variable *x1 = new Variable("x");
  Variable *y1 = new Variable("y");
  x1->dump();

  Term::IsIsomorphic(x1, y1);
}
