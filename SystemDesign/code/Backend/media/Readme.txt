EAST Test 59 Release v1.0
Dec. 1, 2016
Brett A. Cruden

EAST Test 59 Release 1 contains 51 shots in Air between 7-9 km/s and freestream pressures of 0.01-0.70 Torr.
Shots 1-33 were collected in the 60.3 cm diameter shock tube, shots 34-51 in the 10.16 cm diameter tube.
Also included are the paper and presentation that describe the data and are approved for public release 

The EAST Test 59 Data Release is organized as follows:
Readme.txt					- This File
Data Sheets (Folder)					- Details of individual shots
Cross Sections (Folder)				- Selected x and y cross sections from each shot (in .xls format)
Fig Files (Folder)					- Calibrated 3D images in Matlab .fig format
SPE Files (Folder)					- Calibrated 3D images in .SPE format
Test 59 Shot Summary.xls				- Summary of Shots
Test 59 Lineshapes.xls				- Parameterization of Instrument Lineshapes for Each Shot 
Test 59 SRFs.xls					- Parameterization of Spatial Resolution Functions for Each Shot
Test59 Shot Parameters.xls				- Summary of SRF/ILS Data for Selected Test Shots.  Parameters are given for NEQAIR inputs
Non-equilibrium Metric.xls				- A subset of selected non-equilibrium validation data
RHTG 2016 (Air).ppt					- A presentation that describes the data
2017 AIAA AVIATION Abstract - LowSpeedAirNonEq.pdf 	- A paper (extended abstract) that describes the data 

Test 59 Shot Summary.xls contains selected details and notes for all shots, including velocity, pressure and spectrometer
ranges.  Spectrometer data is color coded to indicate the quality of the collected data. 

For information on how to use the spectrometer and spatial resolution functions, users are referred to the following NATO report:
Cruden , B. A., "Absolute Radiation Measurements in Earth and Mars Entry Conditions," RTO-EN-AVT-218, 2014.

Users of this data are requested to cite:
Cruden, BA and Brandis, AM, "Measurement of Radiative Non-equilibrium for Air Shocks Between 7-9 km/s," AIAA Thermophysics Conference, 2017.
The AIAA paper number will not be available until June of 2017.  Publications of the data after that time should identify the corresponding paper number

Notes on formats:

*.SPE files may be read through WinSpec software by PI-Acton, or converted to Matlab/IGOR format with routines provided in the general directory:
	WinSpec.ipf (IGOR)
	ImportSPE.m (Matlab)

	In SPE format, the x and y calibrations are given in the file header.  y-calibration does not display in WinSpec but is 
	incorporated in the parsing routines provided.

	Wavelength is expressed in nm
	Position is given in cm
	Intensity is given in uW/cm2-sr-nm.  Divide by 1e3 to obtain W/cm2-sr-um.

*.fig files are Matlab figures files containing data in W/cm2-sr-um.  Data may be extracted from the figure with the 'get' command.
	See Matlab documentation for more details.

NOTE: Most Excel files have dynamic links which may not transfer in the unzipped archive.  It is recommended not to update links to
avoid any possible issues with this.

ASCII versions are presently not included due to file size limitations but may be posted on request.

Raw data files, including calibration spectra and analysis routines, are available on request.
Please direct any comments or questions, including observed errors or discrepancies to Brett Cruden:
Brett.A.Cruden@nasa.gov
