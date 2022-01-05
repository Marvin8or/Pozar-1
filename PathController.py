# -*- coding: utf-8 -*-
from pathlib import Path


OPENFOAM_FILES_FOLDER_BASH = Path("mnt", "g", "OpenFoamFiles")
SOLVER = "wildfireScalarTransportFoam"
ALLRUN_BASH = Path(OPENFOAM_FILES_FOLDER_BASH, "Allrun")
BASH_COMMAND = f'bash -c "{ALLRUN_BASH} {OPENFOAM_FILES_FOLDER_BASH} {SOLVER}"'

PROJECT_ROOT = Path.cwd()
OPENFOAM_FILES_FOLDER = Path(PROJECT_ROOT, "OpenFoamFiles")

SYSTEM = Path(PROJECT_ROOT, OPENFOAM_FILES_FOLDER, "system")
ZERO = Path(PROJECT_ROOT, OPENFOAM_FILES_FOLDER, "0")
CONSTANT = Path(PROJECT_ROOT, OPENFOAM_FILES_FOLDER, "constant")
OPENFOAM_DIRS = {"system": SYSTEM, "0": ZERO, "constant": CONSTANT}

OPENFOAM_CONTROL = {
    "0": {
        "A": Path(ZERO, "A"),
        "Cs": Path(ZERO, "Cs"),
        "k": Path(ZERO, "k"),
        "kwind": Path(
            ZERO,
        ),
        "S": Path(ZERO, "S"),
        "T": Path(ZERO, "T"),
        "U": Path(ZERO, "U"),
        "Z": Path(ZERO, "Z"),
    },
    "constant": {"transportProperties": Path(CONSTANT, "transportProperties")},
    "system": {
        "blockMeshDict": Path(SYSTEM, "blockMeshDict"),
        "controlDict": Path(SYSTEM, "controlDict"),
        "setFieldsDict": Path(SYSTEM, "setFieldsDict"),
    },
}

OPENFOAM_ORIGINAL_FILES_FOLDER = Path(PROJECT_ROOT, "OpenFoamOriginalFiles")
SYSTEM_ORIGINAL = Path(PROJECT_ROOT, OPENFOAM_ORIGINAL_FILES_FOLDER, "system")
ZERO_ORIGINAL = Path(PROJECT_ROOT, OPENFOAM_ORIGINAL_FILES_FOLDER, "0")
CONSTAN_ORIGINAL = Path(PROJECT_ROOT, OPENFOAM_ORIGINAL_FILES_FOLDER, "constant")
OPENFOAM_DIRS_ORIGINAL = {"system": SYSTEM_ORIGINAL, "0": ZERO_ORIGINAL, "constant": CONSTAN_ORIGINAL}

OPENFOAM_CONTROL_ORIGINAL = {
    "0": {
        "A": Path(ZERO_ORIGINAL, "A"),
        "Cs": Path(ZERO_ORIGINAL, "Cs"),
        "k": Path(ZERO_ORIGINAL, "k"),
        "kwind": Path(
            ZERO_ORIGINAL,
        ),
        "S": Path(ZERO_ORIGINAL, "S"),
        "T": Path(ZERO_ORIGINAL, "T"),
        "U": Path(ZERO_ORIGINAL, "U"),
        "Z": Path(ZERO_ORIGINAL, "Z"),
    },
    "constant": {"transportProperties": Path(CONSTAN_ORIGINAL, "transportProperties")},
    "system": {
        "blockMeshDict": Path(SYSTEM_ORIGINAL, "blockMeshDict"),
        "controlDict": Path(SYSTEM_ORIGINAL, "controlDict"),
        "setFieldsDict": Path(SYSTEM_ORIGINAL, "setFieldsDict"),
    },
}