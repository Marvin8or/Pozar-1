# -*- coding: utf-8 -*-
from pathlib import Path

_PROJECT_ROOT = Path.cwd()
_OPENFOAM_FILES_FOLDER = Path(_PROJECT_ROOT, "OpenFoamFiles")
_SYSTEM = Path(_PROJECT_ROOT, _OPENFOAM_FILES_FOLDER, "system")
_0 = Path(_PROJECT_ROOT, _OPENFOAM_FILES_FOLDER, "0")
_CONSTANT = Path(_PROJECT_ROOT, _OPENFOAM_FILES_FOLDER, "constant")


OPENFOAM_CONTROL = {
    "0": {
        "A": Path(_0, "A"),
        "Cs": Path(_0, "Cs"),
        "k": Path(_0, "k"),
        "kwind": Path(
            _0,
        ),
        "S": Path(_0, "S"),
        "T": Path(_0, "T"),
        "U": Path(_0, "U"),
        "Z": Path(_0, "Z"),
    },
    "constant": {"transportProperties": Path(_CONSTANT, "transportProperties")},
    "system": {
        "blockMeshDict": Path(_SYSTEM, "blockMeshDict"),
        "controlDict": Path(_SYSTEM, "controlDict"),
        "setFieldsDict": Path(_SYSTEM, "setFieldsDict"),
    },
}
