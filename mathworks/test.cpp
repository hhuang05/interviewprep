#include "Variable.h"
#include "Term.h"
#include <iostream>

int main()
{
  Variable *x1 = new Variable("x");
  Variable *y1 = new Variable("y");
  x1->dump();

  Term::IsIsomorphic(x1, y1);
}
