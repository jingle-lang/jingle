<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://raw.githubusercontent.com/exedys/jingle-lang/master/jingle%20logo.png" alt="Jingle Logo"></a>
</p>

<h3 align="center">Jingle Lang 2020 v0.01-rc1</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg?style=for-the-badge)](https://github.com/jingle-lang/jingle/blob/master/CHANGELOG.md)
  [![GitHub Issues](https://img.shields.io/github/issues/jingle-lang/jingle?style=for-the-badge)](https://github.com/jingle-lang/jingle/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/jingle-lang/jingle?style=for-the-badge)](https://github.com/jingle-lang/jingle/pulls)

</div>

---

<p align="center"> Jingle is a statically-typed, multi-paradigm programming language designed for humans and machines on the LLVM.
    <br> 
</p>

<details>
<summary>📝 Table of Contents</summary>
<br />
  
- [About](#about)
- [Examples](https://github.com/jingle-lang/jingle/tree/master/examples)
- [Getting Started](#getting_started)
- [Documentation](#docs)
- [Coming Soon](../master/docs/COMING_SOON.md)
- [Contributing](../master/docs/CONTRIBUTING.md)
- [Changelog](../master/docs/CHANGELOG.md)
- [Code of Conduct](../master/docs/CODE_OF_CONDUCT.md)
</details>

## 📜 About <a name = "about"></a>
Jingle is a statically-typed programming language currently in development. Code in Jingle is fast to run and compile while still retaining small source files and binaries. It compiles to machine code via the LLVM using the LLVMlite library but it can also use its bytecode virtual machine to run files at slower speeds but without the need of the large LLVM dependency.

Here is an example that calculates the Fibonacci numbers to give you a quick look at the language:
```elixir
let count = 30

fn fibonacci(n: Int) -> Int:
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    end else:
        return 1
    end
end

fn main() -> Int:
    var n: Int = 0
    while n < count:
        echo fibonacci(n)
        n = n + 1
     end
     return 0
end
```

## Getting Started <a name = "getting_started"></a>
CLI tools are coming soon.

Installation:
  1. Clone project or download a release binary
  2. Install dependencies with `pip -r requirements.txt`
  
Compile to a native executable
  1. Run the following command `python3 -m compiler.compile <filename>`
  2. Run the generated executable

Generate LLVM bytecode
  1. Run the following command `python3 -m compiler.llvmgen <filename>`
  2. LLVM bytecode will be printed out

Execute in an LLVM JIT
  1. Run the following command `python3 -m compiler.run <filename>`
  2. Result will be printed

Execute a file on the virtual machine
  1. Run the following command `python3 -m compiler.vm <filename>`
  2. Result will be printed

## Documentation <a name = "docs"></a>
https://midoublelo.gitbook.io/jingle-docs/
