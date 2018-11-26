#include "FunctionApp.h"
#include <iostream>

FunctionApp::FunctionApp(Term *op, std::vector<Term*> *operands):
  _op(op), _operands(operands)
{
}

FunctionApp::~FunctionApp()
{
}

std::vector<Term *> *FunctionApp::getOperands()
{
  return _operands;
}

Term *FunctionApp::getOp()
{
  return _op;
}

void FunctionApp::dump(std::string prefix)
{
  std::cout << prefix << "+FunctionApp" << std::endl;
  _op->dump(prefix + "|-");
  
  for (std::vector<Term *>::const_iterator c_it = _operands->begin();
       c_it != _operands->end(); ++c_it) {  
    (*c_it)->dump(prefix + "|-");
  }
}
