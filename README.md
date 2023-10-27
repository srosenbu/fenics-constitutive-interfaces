# fenics-constitutive-interfaces

This is a very lightweight package that provides interfaces for constitutive models which other repositories can use to actually build constitutive models.

## Why only interfaces? Where is plasticity, damage, etc.?

FEniCSx was never intended to be a solver for nonlinear mechanics models. Some projects have written their own workarounds:

1. `MFront` https://github.com/thelfer/MFrontGenericInterfaceSupport
2. `fenics-constitutive` (Abandoned) https://github.com/BAMresearch/fenics-constitutive
3. `comFE` (WIP) https://github.com/srosenbu/comFE

However, from a user perspective, there is no easy way to write a simulation script with `dolfinx` where a nonlinear constitutive model can just be exchanged for a model from another project without major rewrites of their code.

Here, this project comes into play. By providing predefined behaviours for constitutive models, that other developers may use to base their models on, we hope to make it easier simulate mechanics problems in dolfinx without being bound to a specific package.

