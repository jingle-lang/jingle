Jingle CLI/REPL Commands:
- `jingle build` - AOT compile Jingle code.
  - `-o` - Output raw LLVM IR.
  - `-t` - Choose compile target
    - `--exec` - Native executable compile
    - `--wasm` - Compile to WebAssembly
    - `--js` - Compile to JavaScript
- `jingle run` - JIT compile Jingle code and run immediately.
- `jingle version`
