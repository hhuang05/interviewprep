#ifndef TERM_H
#define TERM_H

#include <vector>

#define Abs(x)    ((x) < 0 ? -(x) : (x))
#define Max(a, b) ((a) > (b) ? (a) : (b))

/* Term: Abstract base class of all concrete terms
 * 
 */
class Term
{

public:
  static bool IsIsomorphic(Term *a, Term *b);

  // Gets operands for those subclasses which have operands
  virtual std::vector<Term *> *getOperands() = 0;

  // Prints each specific term to stdout
  virtual void dump() = 0;
};

#endif
