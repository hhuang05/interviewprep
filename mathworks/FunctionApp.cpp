#include "FunctionApp.h"
#include <iostream>

FunctionApp::FunctionApp(Term *op, std::vector<Term*> *operands):
  _op(op), _operands(operands)
{
}

FunctionApp::~FunctionApp()
{
}

void FunctionApp::dump()
{
  std::cout << "+FunctionApp" << std::endl;
  std::cout << "|-";
  _op->dump();
  for (std::vector<Term *>::const_iterator c_it = _operands->begin();
       c_it != _operands->end(); ++c_it) {
    std::cout << "|-";
    (*c_it)->dump();
  }
}
