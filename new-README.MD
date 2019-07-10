<h3 align="center">Jingle Lang v0.01</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/exedys/jingle-lang.svg)](https://github.com/exedys/jingle-lang/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/exedys/jingle-lang.svg)](https://github.com/exedys/jingle-lang/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Jingle is the humanized programming language with syntax written in English.
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Examples](#examples)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)
- [Coming Soon](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Changelog](../CHANGELOG.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)

## 📜 About <a name = "about"></a>
Jingle is a (very) high-level general-purpose programming language based off of Java. It is statically-typed, inferred and nominal. "So why would I use this instead of Java?", I hear you ask. Well, Jingle is written in almost plain English. This makes it much easier for beginners without adding complexity or removing functionality for advanced programmers. It is also targets the JVM.

## 📔 Examples <a name = "examples"></a>
Alright, let's look at how this whole "written in English" thing works. Here are 2 Hello World applications written in both Java & Jingle, with Java being on top and Jingle being on bottom.

```java

public class HelloWorld {

  public static void main(String[] args) {
      System.out.println("Hello, World");
  }
  
}
```
`say ("Hello World")`

As you can see, Jingle is a lot simpler and in this case, just makes more sense. Its syntax is more similar to scripting languages and lines that you would enter into a command prompt, rather than convoluted solutions to incredibly simple tasks.

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

You can get Jingle through our Jingle Packs at jingle-lang.org. These will include the binaries, offline documentation, examples and Jingle's package manager, Toll. The Jingle Pack will also create a PATH variable so you can use Jingle straight from the Command Prompt straight away. Check if your installation succeeded by running `jingle` into the console. This should show the following:
```
Jingle Lang v1.x - (c) Exedys Digital/ Millo Evers 2019
run "jingle help" for commands
``` 

## 🎈 Usage <a name="usage"></a>
As Jingle is a general-purpose programming language, its intended usage is to be up to the user and for them to use it for whatever they need it for. However, because it is still a very new language, Jingle cannot be used for as many things other languages can be used for. This is mostly because other languages have a lot of frameworks, libraries, plugins, extensions, etc... that allow developers do what they want. However for most plain/raw usage it should suffice.

## 🚀 Deployment <a name = "deployment"></a>
Please read the Jingle documentation for information about deployment & compiliation.

## ✍️ Authors <a name = "authors"></a>
- [@exedys/Millo Evers](https://github.com/exedys) - Creator of Jingle

See also the list of [contributors](https://github.com/exedys/jingle-lang/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
*  My fellow computer science students for helping me test the language out
* Marc-André Cournoyer for his [excellent book](http://createyourproglang.com/) that started off Coral which led to Jingle.
