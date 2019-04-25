The GUI tool is for visualizing optical flow results with "flo" file format. See http://vision.middlebury.edu/flow/code/flow-code/README.txt for the "flo" file format definition. The color visualization is also following the Middlebury way (white means no displacements). The tool is only for academic use. 

Usage:
1. File opening: double click on a flo file, set the opener as the executable. 
2. Multi-file browsing: open one flo file, put the mouse on the canvas, scroll mouse wheel to view other flo files in the same folder. 
3. Adjust color range with the slider on the rightside. Toggle the checkbox "Keep" on to keep the range fixed when browsing multi-files. 
4. Hovering the mouse over the canvas will show the pixel values in status bar. 
5. Toggle the checkbox "Show Channels" to view the grayscale map of the two channels of optical flow. 
6. You can save the colorization results into RGB images. 
7. Please cite our paper if you find this tool useful :-) 

@inproceedings{bao2014cvpreppm,
  title={Fast Edge-Preserving PatchMatch for Large Displacement Optical Flow},
  author={Bao, Linchao and Yang, Qingxiong and Jin, Hailin},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2014},
  organization={IEEE}
}


ACKNOWLEDGEMENTS: Thanks to the Middlebury flo file read/write code. Thanks to the QT4 library. 

Please contact with linchaobao at gmail dot com for reporting bugs. Last update: Apr 02, 2014.