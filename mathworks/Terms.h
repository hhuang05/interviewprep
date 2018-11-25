#ifndef TERMS_H
#define TERMS_H

#include <vector>

/* Term: Abstract base class of all concrete terms
 * 
 */
class Term
{

public:
	bool IsIsomorphic(Term *a, Term *b);
	std::vector<Term *> *getOperands();

	// Prints each specific term to stdout
	void dump() = 0;

};

#endif
