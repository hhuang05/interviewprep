#ifndef VARIABLE_H
#define VARIABLE_H

#include "Terms.h"
#include <string>

class Variable : public Terms
{
	std::string _name;
public:
	Variable(std::string name);
	~Variable();

	std::vector<Term *> *getOperands() {return nullptr};
	void dump();

	std::string getName() {return _name};
};

#endif