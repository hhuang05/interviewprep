#include "Variable.h"
#include <iostream>

Variable::Variable(std::string name) :
	_name(name)
{
}

~Variable::Variable()
{
	delete _name;
}

Variable::dump()
{
	std::cout << "Variable : " << _name << std::endl;
}