from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from typing import final

import dolfinx as df

__all__ = ["ConstitutiveModel", "IncrSmallStrainModel", "IncrSmallStrainExplicitModel"]

class ConstitutiveModel(ABC):
    @abstractmethod
    def evaluate(
        del_t: float = 1.0,
    ) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractproperty
    def input(self) -> dict[str, df.fem.Function]:
        pass

    @abstractproperty
    def output(self) -> dict[str, df.fem.Function]:
        pass

    @abstractproperty
    def fields_0(self) -> dict[str, df.fem.Function]:
        pass

    @abstractproperty
    def fields_1(self) -> dict[str, df.fem.Function]:
        pass


class IncrSmallStrainModel(ConstitutiveModel):
    @final
    def input(self) -> dict[str, df.fem.Function]:
        return {
            "mandel_strain_increment": self.fields_0["mandel_strain_increment"],
            "mandel_stress": self.fields_0["mandel_stress"],
        }

    @final
    def output(self) -> dict[str, df.fem.Function]:
        return {
            "mandel_stress": self.fields_1["mandel_stress"],
            "mandel_tangent": self.fields_1["mandel_tangent"],
        }


class IncrSmallStrainExplicitModel(ConstitutiveModel):
    @final
    def input(self) -> dict[str, df.fem.Function]:
        return {
            "velocity_gradient": self.fields_0["velocity_gradient"],
            "mandel_stress": self.fields_0["mandel_stress"],
        }

    @final
    def output(self) -> dict[str, df.fem.Function]:
        return {
            "mandel_stress": self.fields_1["mandel_stress"],
        }
