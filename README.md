Python Workshop - Image Processing
==================================


## Course Aims and Overview

This course teaches the basics of bio-image processing, segmentation and analysis in python. It is based on tutorials that integrate explanations and exercises, enabling participants to build their own image analysis pipeline step by step.

All material is provided as Jupyter notebooks. To find out more about how to run these materials interactively, see the [Jupyter documentation](https://jupyter.readthedocs.io/en/latest/index.html).

The [`main_tutorial`](./main_tutorial/) uses single-cell segmentation of a confocal fluorescence microscopy image to illustrate key concepts from preprocessing to segmentation to data analysis. It includes a tutorial on how to apply such a pipeline to multiple images at once (batch processing).

The main tutorial is complemented by the [`pre_tutorial`](./pre_tutorial/) content, which provides some basics of Jupyter, `matplotlib` and an introduction to `numpy` and working with arrays, and by the `optional_advanced_content`, which features further examples and tutorials on the topics of vectorization, multiprocessing, cluster computation and advanced data analysis.

This course is aimed at people with basic to intermediate knowledge of python and basic knowledge of microscopy. For people with basic knowledge of image processing, the tutorials can be followed without attending the lectures.


## Instructions on following this course

- If you have only very basic knowledge of python or if you are feeling a little rusty, you should start with the `pre_tutorial`, which includes two notebooks: one on `numpy` arrays and one on the basics of Jupyter and `matplotlib`. If you are more experienced, you may want to skim or skip the pre-tutorial.

- In the `main_tutorial`, it is recommended to follow the `tutorial_pipeline` first. By following the exercises, you should be able to implement your own segmentation pipeline. If you run into trouble, you can use the provided solutions as inspiration - however, it is *highly* recommended to spend a lot of time figuring things out yourself, as this is an important part of any programming exercise.

- Finally, the `optional_advanced_content` contains an introductory example to three important techniques for making making your scripts faster and operating on large datasets, namely *vectorization*, *multiprocessing* and *cluster processing*. The `data_analysis` tutorial (currently in *BETA*!) is an introduction to piping segmentation results into more advanced statistical data analysis, including *feature extraction*, *PCA*, *clustering* and *graph-based analysis*.


## Concepts discussed in course lectures

1. **Introductory Material (Toby Hodges)**
   	* Working with the Jupyter Notebook
	* Importing packages and modules
	* Reading data from files
	* A brief introduction to `matplotlib`
	* Data and variable types
	* An introduction to `numpy`
	* Arrays, indexing, slicing
	* Using the documentation

2. **Basics of BioImage Processing (KM)**
	* Images as numbers
		* Bit/colour depth
		* Colour maps and look up tables 
	* Definition of Bio-image Analysis
		* Image Analysis definition for signal processing science 
		* Image Analysis definition for biology
		* Algorithms and Workflows
		* Typical workflows in biology
	* Convolution and Filtering
		* Why do we do filtering?
		* Convolution in 1D, 2D and 3D 
	* Pre-segmentation filtering
		* De-noising
		* Smoothing
		* Unsharp mask
	* Post-segmentation filtering
		* Tuning segmented structures
		* Mathematical morphology, erosion, dilation
			* Distance map 
			* Watershed

3. **Introduction to the Tutorial Pipeline (JH)**
	* Automated Single-Cell Segmentation
		* Why? (Advantages of single-cell approaches)
		* How? (Standard segmentation pipeline build)
			* Preprocessing (smoothing, background subtraction)
			* Presegmentation (thresholding, seed detection)
			* Segmentation (seed expansion; e.g. watershed)
			* Postprocessing (removing artefacts, refining segmentation)
			* Quantification and analysis
		* What? (for the main tutorial: 2D spinning disc confocal fluorescence microscopy images of Zebrafish embryonic cells)
		* Who? (YOU!)

3. **Advanced material**
	* CellProfiler to automate image analysis workflows and python plugin module **(VH)**
	* Code Optimisation (vectorisation, multiprocessing, cluster processing) & advanced data analysis **(JH)**

		
## Instructors

- Jonas Hartmann
    - Gilmour Lab, CBB, EMBL
    - Pipeline developer, practical materials preparation, tutor, TA
- Toby Hodges
    - Bio-IT, Zeller Team, SCB, EMBL
    - TA (python)


## Inspiration

This repository was forked from [Karin Sasaki's materials on GitHub](https://github.com/karinsasaki/python-workshop-image-processing). These materials have been adapted from the original version, written and taught by Karin Sasaki, Jonas Hartmann, Kota Miura, Volker Hinsenstein, Aliaksandr Halavatyi, Imre Gaspar, and Toby Hodges.

## Feedback 

We welcome any feedback on this course! 

Feel free to contact us at *jonas.hartmann@embl.de* or *toby.hodges@embl.de*.
