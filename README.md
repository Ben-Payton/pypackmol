# Welcome

This is a python package meant to replace packmol.

Packmol is an industry standard when it comes to packing boxes when running molecular dynamics, however many wrappers around it involve creating inputs that conform, and then running packmol from the commandline or a shell.

This is a tedious process, and many workflows are moving to python. This package is meant to expose a more python friendly interface and behave like packmol. For now we are working to provide only the python api, as core functionality is acheived we will provide a CLI that can serve as a drop in replacement to packmol.

As of the time of writing this, this will be python based project, as greater performance is needed, we may implement some functionality using Rust. We do this to avoid memory based errors, and because maturin and PyO3 allow us to do this easily.