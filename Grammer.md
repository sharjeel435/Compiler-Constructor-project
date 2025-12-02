<program> ::= <statement>

<statement> ::= <assignment> | <expression>

<assignment> ::= <identifier> "=" <expression>

<expression> ::= <term> <expression-tail>
<expression-tail> ::= "+" <term> <expression-tail>
                    | "-" <term> <expression-tail>
                    | ε

<term> ::= <factor> <term-tail>
<term-tail> ::= "*" <factor> <term-tail>
              | "/" <factor> <term-tail>
              | ε

<factor> ::= <number>
           | <identifier>
           | "(" <expression> ")"

<identifier> ::= <letter> <id-tail>
<id-tail> ::= <letter> <id-tail>
            | <digit> <id-tail>
            | ε

<number> ::= <digit>+ | <digit>+ "." <digit>+