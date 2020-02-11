# Jingle Roadmap. Last updated: (10th February 2020)

## Lexer
  - [x] Move away from ANTLR as a lexer generator
  - [x] Use Lark as a lexer generator
  - [x] Recognise all keywords
  - [x] User tests written and passing
  - [ ] Units tests written and passing
  
## Parser
  - [x] Move away from ANTLR as a parser generator
  - [x] Use Lark as a parser generator
  - [x] Move from LL(*) - ANTLR's algorithm - to LALR(1), Lark's algorithm
  - [ ] Language Features successfully parsing
    - [x] Variables
      - [x] Variables
      - [x] Constants
      - [x] Let Variables
      - [x] Type Binding
      - [x] Type Annotations
    - [x] Runtime Objects
      - [x] Functions
      - [x] Classes
      - [x] Traits

Proposed changes to the language:

- Delimit blocks with colons (python) and 'end' (ruby) keywords
- Retain var, const and let declaration keywords
- Encourage 3 main paradigms: object-oriented, functional, imperative
- Replace comment styles:
  - Single-line comments replace `//` with `#`
  - Remove block comments for now, change to `--` to open and close in future
- Add switch/case/otherwise blocks
  - Instead of `default`, use keyword `otherwise`
