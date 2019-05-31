#include "Variable.h"
#include <iostream>

Variable::Variable(std::string name) :
  _name(name)
{
}

Variable::~Variable()
{
}

std::string Variable::getName()
{
  return _name;
}

void Variable::dump(std::string prefix)
{
  std::cout << prefix << "Variable: " << _name << std::endl;
}
