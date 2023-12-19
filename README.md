
## Overview

This repository contains the implementation of an innovative tool designed for real-time panoramic imaging in an optical microscopy environment. The tool aims to overcome limitations associated with conventional panoramic image construction techniques, offering an efficient and high-quality solution through the use of computer vision algorithms.

## Motivation

In the field of optical microscopy, analysts commonly rely on a macroscopic reference frame to locate specific details in samples. Often, computational tools are employed to construct high-resolution panoramic images from lower-resolution captures. However, this traditional process is tedious, time-consuming, and often yields low-quality results in terms of image resolution.

## Key Features

- **Continuous Image Acquisition:** The tool employs an innovative strategy of continuously forming the image while traversing the sample by moving the microscope stage.

- **Panoramic Construction Algorithm:** An advanced algorithm based on computer vision tools has been developed for efficient real-time panoramic image construction.

- **Testing and Validation:** The repository includes tests conducted in simulated environments and a real optical microscope. Simulated tests have shown promising results, demonstrating the ability to reconstruct images accurately. Tests on the optical microscope have yielded encouraging results in terms of speed and image quality.

- **Identification of Intrinsic Aberrations:** Tests on the optical microscope have also allowed the identification of sources of intrinsic instrument aberrations, contributing to improving the technique's robustness.

# Clonning de repository

1 - Clone the repository

2 - Create a virtual enviroment with:
```bash
    python3 -m venv /path/name_venv
```

3 - Activate venv with:
    
    .\.name_venv\Scripts\Activate.ps1

4 - Install dependencies

    py -m pip install -r requirements.txt

## User Interface

The tool features a user-friendly interface built with QML and Qt.

### Video demo
[![Micro Stitch](https://i3.ytimg.com/vi/4HrGwN9sFaQ/hqdefault.jpg)](https://youtu.be/4HrGwN9sFaQ)


To launch the tool with the graphical user interface, run:

```bash
cd micro_stitch
python main.py
```

## Contributions and Issues
Contributions are welcome! Please fork the repository and create a pull request.
If you encounter any issues, please open a new issue here.
## License
This project is licensed under the [License Name] - see the LICENSE.md file for details.
