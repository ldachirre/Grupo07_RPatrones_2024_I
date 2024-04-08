'PQ_ProcessedData'
Folder contains fully processed data from pressure & flow sensor array.
Files are saved in these folders by subject number ('Subject01' through to 'Subject20'), PEEP used ('0cmH2O', '4cmH2O', or '8cmH2O') and COPD simultor size ('0ml', '200ml', '250ml', or '300ml') e.g. 'MayTrial2023_Subject01_0cmH2O_0ml.csv' through to 'MayTrial2023_Subject20_8cmH2O_300ml.csv'
These files contain data in columns (A:F): 
	'T' - Time [s],
        'P' - Pressure [cmH2O], 
	'Q' - Flow [L/s], 
	'V' - Tidal Volume [L],
	'Ind' - Inspiratory Indicies,
	'm' - Weight [kg]	

'PQ_rawData'
Folder contains raw data and raw data with units processed from pressure & flow sensor array.
Files are saved under folders by subject number ('01' through to '20'), PEEP ('0cmH2O', '4cmH2O', '8cmH2O'), and size ('0ml', '200ml', '250ml', '300ml'). 
Files with relevant units (e.g. 'COPDTrial2023_Subject1_0cmH2O_0mL.csv') contain data in columns (A:D): 
	'time' - time [s], 
	'GaugeP' - Gauge pressure [cmH2O], 
	'InhaleDeltaP' - Inspiratory differenrtial pressure [cmH2O], 
	'ExhaleDeltaP' - Expiratory differenrtial pressure [cmH2O], 

Files with raw ADC counts (e.g. 'COPDTrial2023_Subject1_0cmH2O_0mL_raw.csv') contain data in columns (A:H): 
	'time' - time [s], 
	'GaugeP_ADC' - Gauge pressure, 
	'InhaleP_ADC' - Inspiratory differenrtial pressure, 
	'ExhaleP_DC' - Expiratory differenrtial pressure, 	

'figure_1.png' is an example PQ plot for the first breath of Subject 1 with 0 PEEP and the 300ml device attached 
'PQ_Loop.m' is the MATLAB code used to plot figure-1



