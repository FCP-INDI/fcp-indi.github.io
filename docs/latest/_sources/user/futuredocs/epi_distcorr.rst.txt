Distortion correction is a method used for minimizing noise primarily in images obtained by echo-planar imaging (EPI). Using EPI, it has been possible to obtain individual MR slices in time frames of 50 - 100 ms, which minimizes losses in signal due to patient motion. However,EPI sequences have other sources of signal loss, primarily arising from tissue differences in the brain which result in static field inhomogenities {https://en.wikibooks.org/wiki/Neuroimaging_Data_Processing/Field_map_correction} 
C-PAC provides options for configuring the Distortion correction workflow, either directly by manipulating the pipeline configuration, or by using the GUI. The EPI_DistCorr workflow is placed under the Functional Preprocessing tab. You can choose to run the workflow, and customize the parameters for the run. The field maps are generated within the distortion correction workflow, and sub sequentially sent to the “func_to_anat” non-linear registration for converting the input epi image into the structural phase. 
FSL's fieldmap correction takes in as it's input a magnitude image, and a phase image which is obtained by phase subtraction between two magnitude images obtained in series. If the user has two input magnitude images, both should be inspected using fsleyes or afni to determine the image with “better quality" which can then be used. 
The parameters provided in the GUI are described below:

1. Perform Field Map Distortion correction [switch]: "On" or "Off". You can switch on or off the workflow as necessary    
2. Skull-strip the magnitude file with-[choice-box]: Since the output of the Distortion correction relies heavily on the skull strip, you could choose between AFNI-3d Skull-Strip and FSL-BET. The choice of tool to be used is currently only a feature for Distortion correction workflow. Both the workflows have identical options, thereby preventing any bias towards one tool. 
3.BET threshold/AFNI shrink factor-[float]: The threshold for brain extraction. FSL requires tight skull-stripping, erring on the side of ignoring brain voxels rather than adding noise. However, it might not be required to increase the threshold in all datasets, so it is important to check your dataset before changing the threshold.In FSL-BET, this is referred to as "threshold intensity” and in AFNI'S 3dSkull Strip, it is the -shrink_facto. The default value is 0.5.
4. DeltaTE-[float,ms]: The time difference between the first magnitude image and the second magnitude image. The default value is 2.46 ms, which is widely used for SIEMENS, but it may differ with different datasets.
5.Dwell Time-[float,s]: The dwell time is also known as echo spacing, and it is the time between the start of the readout of two successive lines in k-space during the EPI acquisition. This is a value obtained from the functional epi (NOT the fieldmap)  Here, the default value is 0.0005s.
6. Dwell to asymmetric ratio-[float]: This is the ratio between the Dwell time, as referenced above and the asymmetric time. Here, the default value is 0.93902439.
7. Phase encoding direction-[string]: This is the position of the voxels in the input image, and can have values of x/y/z or -x/-y/-z. This is predominantly a trail and error based parameter.

Configuration without the GUI 
The following key/value pairs must be defined in your pipeline configuration YAML for C-PAC to run Distortion correction

Key 					Descripton 				Potential Values
Perform distortion			Run Distortion 				A switch with [‘On’], 
correction with field map		correction workflow			[‘Off’] or [‘On’,’Off’]
correction 

Skull-strip the magnitude		Use either FSL-BET			A list to choose between 
file					or AFNI-3dSkullStrip 			[‘FSL-BET’] and 
					for the brain extraction 		[3d-SkullStrip’]
					of magnitude image. 

Brain Extraction Threshold		The ratio between 				
(or shrink factor in 			 brain voxels to include		Float,default value is 0.5
AFNI-3dSkullStrip)			 and those to exclude(strip)

DeltaTE, ms				 The time delay between 		Float,default value is 2.46
					 first magnitude image and 		for SIEMENS scanner.
					 second magnitude image.
					 The value is specific to each 
					 session.This parameter is 
					 used for preparing the 
					 field map.
Dwell Time, s				 Also called the “echo spacing”	Float,default value is 
					 time, this is used as a parameter 	0.0005
					 for FUGUE interface.

Dwell to asymmetric			 Ratio between the dwell time 		Float,default value is
ratio					 to the asymmetric time. This 		0.93902439
					 parameter is used for running 
					 the EPI-registration


Phase encoding                         Direction of unwrapping, the 		(x/y/z or -x/-y/-z)	
direction				 location of voxels in the input
					 image 
					 


The box below contains an example of what these parameters might look like when defined in the YAML:

runEPI_DistCorr                       :              [1]
fmap_distcorr_skullstrip	        :          	[BET]
fmap_distcorr_frac                    :          	[0.5]
fmap_distcorr_deltaTE                 :          	[2.46]
fmap_distcorr_dwell_time              :         	[0.0005]
fmap_distcorr_dwell_asym_ratio        :         	[0.93902439]
fmap_distcorr_pedir		        :		-y