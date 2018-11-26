#include "FunctionDef.h"
#include <iostream>

FunctionDef::FunctionDef(std::vector<Variable*> *vars, Term *term):
  _vars(vars), _term(term)
{
}

FunctionDef::~FunctionDef()
{
}

std::vector<Variable*> *FunctionDef::getVariables()
{
  return _vars;
}

Term *FunctionDef::getTerm()
{
  return _term;
}

void FunctionDef::dump(std::string prefix)
{
  // Dump out the list of variables
  std::cout << prefix << "+FunctionDef" << std::endl;
  
  for (std::vector<Variable*>::const_iterator var_it = _vars->begin();
       var_it != _vars->end(); ++var_it) {
    (*var_it)->dump(prefix + "|-");
  }
  
  // Then dump out the term
  _term->dump(prefix + "|-");  
}

