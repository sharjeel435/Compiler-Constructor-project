# MathScript Grammar (BNF Notation)

## Production Rules:

<program> ::= <statement>

<statement> ::= <assignment> | <expression>

<assignment> ::= <identifier> "=" <expression>

<expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>

<term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>

<factor> ::= <number> | <identifier> | "(" <expression> ")"

<identifier> ::= <letter> | <identifier> <letter> | <identifier> <digit>

<number> ::= <digit>+ | <digit>+ "." <digit>+

<letter> ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"

<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"