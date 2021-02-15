<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://raw.githubusercontent.com/exedys/jingle-lang/master/jingle%20logo.png" alt="Jingle Logo"></a>
</p>

<h3 align="center">Jingle Lang 2021.2</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg?style=for-the-badge)](https://github.com/jingle-lang/jingle/blob/master/CHANGELOG.md)
  [![GitHub Issues](https://img.shields.io/github/issues/jingle-lang/jingle?style=for-the-badge)](https://github.com/jingle-lang/jingle/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/jingle-lang/jingle?style=for-the-badge)](https://github.com/jingle-lang/jingle/pulls)

</div>

---

<p align="center"> Jingle is a dynamically-typed, multi-paradigm programming language designed for humans and machines.
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
Jingle is a dynamically-typed programming language currently in development. Code in Jingle is fast to run and compile while still retaining small source files and binaries. Based off the Crafting Interpreters book with a new syntax and expanded standard library. More base language features are coming soon.

Here is an example that calculates the Fibonacci numbers and times it to give you a quick look at the language:
```elixir
fn fib(n):
  if (n < 2) return n;
  return fib(n - 2) + fib(n - 1);
end

var start = timer();
echo "How many iterations?";
var iter = num(gets());
echo "fib(" + str(iter) + ") = " + str(fib(iter));
echo "Time taken " + str(round(timer() - start, 2)) + "s";
```

## Getting Started <a name = "getting_started"></a>
Tested in Visual Studio 2019 on Windows. Publish build to local folder and run from commandline: `jingle <filename>`