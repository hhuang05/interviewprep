#include "Variable.h"
#include <iostream>

Variable::Variable(std::string name) :
	_name(name)
{
}

Variable::~Variable()
{
}

void Variable::dump()
{
	std::cout << "Variable : " << _name << std::endl;
}
