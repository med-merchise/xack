# xack - Tutorials on computer programming theory and techniques

This project contains useful resources for learning and improving computer
programming skills.

This project is a work–in–progress; it is a place to share thoughts and ideas
about programming.

In addition to the theoretical aspects of computer programming ([Computer
Science][cs]), this project will contain:

- Engineering topics on the [Software Development Life Cycle][sdlc].
- [Package manager tools][pm].
- [Computing Environments][ce], some infrastructure aspects to deploy projects
  in production.  [Cloud Computing Architecture][cloud] is the top one
  approach to this concept.
- [Software Project Management][spm].

[cs]: https://en.wikipedia.org/wiki/Computer_science
[sdlc]: https://geeksforgeeks.org/software-development-life-cycle-sdlc
[pm]: https://en.wikipedia.org/wiki/Package_manager
[ce]: https://geeksforgeeks.org/computing-environments
[cloud]: https://geeksforgeeks.org/architecture-of-cloud-computing
[spm]: https://wrike.com/project-management-guide/faq/what-is-software-project-management

## Getting Started

This project was created with the command:

```
uv init --package xack
```

You should [install uv][uv] before:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

[uv]: https://docs.astral.sh/uv/getting-started/installation/

### Setting up your development environment

To start programming you need:

- A Code Editor: Most programmers use [Visual Studio Code][code] and we will
  try to use it as much as possible even when I use Emacs for everything.
- A Programming Language: We will use [Python] for most of the examples.
- Version Control: [Git] has become the de facto standard for VC.
- A packaging tool: See [Python Packaging User Guide][pp] for a Python
  Packaging User Guide, and [uv] for an extremely fast Python package and
  project manager, written in Rust that some people are calling "the future of
  Python Packaging".

[code]: https://code.visualstudio.com
[python]: https://www.python.org
[git]: https://git-scm.com
[pp]: https://packaging.python.org
[uv]: https://docs.astral.sh/uv

## Project Folder Structure

- `bin`: executable scripts that can be run directly from the command line.
- `data`: original copies of raw data.
- `docs`: project documentation.
- `notebooks`: Jupyter notebooks (interactive web application for creating and
  sharing computational documents).
- `rc`: resource configuration to configure the shell environment.
- `src`: package source code.
- `tests`: unit tests and integration tests for the code.

## Known issues

Using `%paste` IPython magic gives an error because `tk` is not properly
installed with `uv add`.  To solve this problem temporarily, copy to the local
virtual environment the `tk` configuration files `{tcl8,tcl8.6,tk8.6}` from
the `$UV_SYSTEM_PYTHON/lib/` folder.  In my case I use as `$UV_SYSTEM_PYTHON`
the folder `~/.uv`.
