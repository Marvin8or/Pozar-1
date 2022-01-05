from PathController import *
import subprocess
from tempfile import mkstemp, TemporaryFile
from shutil import move, copymode
import os
from os import fdopen, remove
import numpy as np
import shutil
import matplotlib.pyplot as plt


def writeToFile(new_file_path, original_file_path, pattern, subst):
    """
    Function to write new values of coordinates (x, y) to setFieldsDict file or
    new time of duration (T) in controlDict file
    """
    # Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, "w") as new_file:
        with open(original_file_path, "r") as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))

    # Copy the file permissions from the old file to the new file
    copymode(original_file_path, abs_path)

    # Move new file
    move(abs_path, new_file_path)



def createNewDirectory(original_case, new_case, symlinks=False, ignore=None):
    """
    Creates new directory by copying files in OpenFoamOriginalFiles to new directory OpenFoamFiles
    """

    for item in os.listdir(original_case):
        source = Path(original_case, item)
        destination = Path(new_case, item)
        if os.path.isdir(source):
            shutil.copytree(source, destination, symlinks, ignore)
        else:
            shutil.copy2(source, destination)


def removeFilesInDirectory(directory_path, files_to_keep):

    """Removes specific files in Directory"""

    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        try:
            if file in files_to_keep:
                continue
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path} Reason: {e}")


def calculateDifferenceOfBurnedArea(original_case, new_case, plot=False):

    original_data, new_data, difference_data = np.zeros(1000000), np.zeros(1000000), np.zeros(1000000)

    with open(original_case, "r+") as original_obj, open(new_case, "r+") as new_obj:
        for i, (original_line, new_line) in enumerate(
            zip(original_obj, new_obj), start=22
        ):
            new_data[i - 22] = new_line
            original_data[i - 22] = original_line
            difference_data = np.abs(new_data[i - 22], original_data[i - 22])

    difference_data_matrix = np.reshape(difference_data, (1000, 1000))

    # TODO chose format to save images as jpg
    if plot:
        plt.imshow(difference_data_matrix)
        plt.savefig("diff.jpg")
        plt.show()

    return difference_data, difference_data_matrix


# TODO find better way to start simulation
def startSimulation(case_dir_bash, case_dir_win, command_bash):
    print(f" - Starting calculation... {case_dir_bash}")
    proc = subprocess.Popen(
        command_bash, cwd=case_dir_win, stdout=TemporaryFile(), stderr=TemporaryFile()
    )
    proc.communicate()
    print(f" - Calculation finished! {case_dir_bash}")


def mainFunction(X, remove_files=True):

    # X = [750,1000,3600]
    createNewDirectory(
        original_case=OPENFOAM_ORIGINAL_FILES_FOLDER, new_case=OPENFOAM_FILES_FOLDER
    )

    writeToFile(
        new_file_path=OPENFOAM_CONTROL["system"]["setFieldsDict"],
        original_file_path=OPENFOAM_CONTROL_ORIGINAL["system"]["setFieldsDict"],
        pattern= "box (850 1800 -0.5) (860 1810 0.5);",
        subst=f"box ({X[0]} {X[1]} -0.5) ({int(X[0]) + 10} {int(X[1]) + 10} 0.5);",
    )

    writeToFile(
        new_file_path=OPENFOAM_CONTROL["system"]["controlDict"],
        original_file_path=OPENFOAM_CONTROL_ORIGINAL["system"]["controlDict"],
        pattern="endTime         3600;",
        subst=f"endTime         {X[2]};",
    )

    startSimulation(
        case_dir_bash=OPENFOAM_FILES_FOLDER_BASH,
        case_dir_win=OPENFOAM_FILES_FOLDER,
        command_bash=BASH_COMMAND,
    )

    difference_data = calculateDifferenceOfBurnedArea(
        original_case=OPENFOAM_ORIGINAL_FILES_FOLDER, new_case=OPENFOAM_FILES_FOLDER
    )
    if remove_files:
        removeFilesInDirectory(directory_path=OPENFOAM_FILES_FOLDER, files_to_keep=None)

    return difference_data
