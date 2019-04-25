The executable is attached with CVPR 2014 paper "Fast Edge-Preserving 
PatchMatch for Large Displacement Optical Flow" for academic use. It has been 
tested on 32-bit and 64-bit Windows 7 with Visual Studio 2008 and CUDA 4.2 SDK 
installed. 

Usage:
--------------------------------------------------------------------
EPPM_flow.exe img1 img2 flo_output flow_color

img1 -- input frame 1 (*.png)
img2 -- input frame 2 (*.png)
flo_output -- output flow result (*.flo)
flow_color -- color preview for flow result (*.png)
--------------------------------------------------------------------

NOTE:
    0) You should have a CUDA-capable NVIDIA GPU to run the program. 
    1) The parameters are fixed to the default parameters reported in the paper.
    2) Due to the randomized algorithm involved, the results of each running may 
       be a little different.
    3) The output file flo_output (*.flo) is in the format described in 
       Middlebury or MPI Sintel benchmark. You can use our FloFileReader to open
       it for color show. 
    4) The output file flow_color (*.png) is only for preview, and its color 
       mapping may be different from that is used in the benchmarks' websites. 
    5) The runtime reported in our paper is obtained on a Geforce GTX 780 GPU. 


    
