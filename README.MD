<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://raw.githubusercontent.com/exedys/jingle-lang/master/jingle%20logo.png" alt="Jingle Lang"></a>
</p>

<h3 align="center">Jingle Lang 2019.00.0-rc1</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg?style=for-the-badge)](https://github.com/jingle-lang/jingle/blob/master/CHANGELOG.md)
  [![GitHub Issues](https://img.shields.io/github/issues/jingle-lang/jingle?style=for-the-badge)](https://github.com/jingle-lang/jingle/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/jingle-lang/jingle?style=for-the-badge)](https://github.com/jingle-lang/jingle/pulls)

</div>

---

<p align="center"> Jingle is a new & simple programming language for modern-day programming.
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Development](#development)
- [Examples](#examples)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)
- [Coming Soon](../master/docs/COMING_SOON.md)
- [Contributing](../master/docs/CONTRIBUTING.md)
- [Changelog](../master/docs/CHANGELOG.md)
- [Code of Conduct](../master/docs/CODE_OF_CONDUCT.md)

## 📜 About <a name = "about"></a>
Jingle is a high-level general-purpose programming language currently in development. It is statically-typed, inferred and structural. "So why would I use this?", I hear you ask. Well, Jingle is written in very simple syntax. This makes it much easier for beginners without adding complexity or removing functionality for advanced programmers. It also has an interpreter with an experimental JVM target.

## 🖥️ Development <a name = "development"></a>
Jingle uses many open source tools such as ANTLR for its lexer & parser, LLVM for its compiler and the JVM for its interpreter. We use Go & Python for most of the language. We decided to use these 2 as Python is much easier to read and program in but Go is a lot faster to run so we use a combination of the both. The compiler utilises mostly the official Go bindings but also some parts are in LLVMlite, the best unofficial Python bindings for LLVM.

## 📔 Examples <a name = "examples"></a>
Alright, let's look at how this all works. Here are 2 Hello World applications written in both Java & Jingle, with Java being on top and Jingle being on bottom.

```java

public class HelloWorld {

  public static void main(String[] args) {
      System.out.println("Hello, World");
  }
  
}
```
`display: ("Hello World")`

As you can see, Jingle is a lot simpler and in this case, just makes more sense. Its syntax is more similar to scripting languages and lines that you would enter into a command prompt, rather than convoluted solutions to incredibly simple tasks. View more examples [here](https://github.com/jingle-lang/jingle/wiki/Syntax-Examples-and-Reference).

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

We recommend usage of a IDE or text editor that supports Jingle. Main ones that are supported are:
* Eclipse 
* IntelliJ IDEA
* Visual Studio Code
* Sublime Text *(Coming Soon)*
* Atom *(Coming Soon)*

### Installing

You can get Jingle through our Jingle Packs at getjingle.org. These will include the binaries, offline documentation, examples and Jingle's package manager, JinglePkg. The Jingle Pack will also create a PATH variable so you can use Jingle straight from the Command Prompt straight away. Check if your installation succeeded by running `jingle` into the console. This should show the following:
```
Jingle Lang v1.x - (c) Exedys Synergies/ Millo Evers 2019
run "jingle help" for commands
``` 

## 🎈 Usage <a name="usage"></a>
As Jingle is a general-purpose programming language, its intended usage is to be up to the user and for them to use it for whatever they need it for. However, because it is still a very new language, Jingle cannot be used for as many things other languages can be used for. This is mostly because other languages have a lot of frameworks, libraries, plugins, extensions, etc... that allow developers do what they want. However for most plain/raw usage it should suffice. The language targets the JVM however which will help it support pre-existing libraries.

## 🚀 Deployment <a name = "deployment"></a>
Please read the Jingle documentation for information about deployment & compiliation.

## ✍️ Authors <a name = "authors"></a>
- [@midoublelo/Millo Evers](https://github.com/midoublelo) - Creator of Jingle

See also the list of [contributors](https://github.com/jingle-lang/jingle/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
*  My fellow computer science students for helping me test the language out
* Marc-André Cournoyer for his [excellent book](http://createyourproglang.com/) that started off Cascade which led to Jingle.
