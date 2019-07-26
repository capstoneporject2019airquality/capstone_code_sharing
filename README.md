# NYU CUSP 2019 Capstone Project
## Local Air Quality Management: Disrupting Vehicle Emission Testing Programs (New York University, Marron Institute)
### Sponsor: Dr. Kevin Cromar
### Team Members:
Project manager: Ewelina Marcinkiewicz (em3845@nyu.edu)  
Web application lead: Jiawen Liang (jl9760@nyu.edu)  
Data processing lead: Jingxi Zhao (jz3309@nyu.edu)  
Document lead: Ursula Kaczmarek (uak211@nyu.edu)  
Data visualisation lead: Yunhe Cui (yc3420@nyu.edu)

### Project Abstract:
Salt Lake County oversees a vehicle emissions testing program to ensure compliance with federal air quality standards. Motorists annually spend millions of dollars for inspections carried out under this program. However, it is not subject to cost controls and suffers from programmatic inefficiencies wherein a large number of compliant vehicles undergo testing and a small number of high-polluting vehicles forgo timely repair. Using survey-based emissions test pricing data, we assess through empirical and spatial autocorrelation analysis the potential economic impact of instituting both emissions test price caps and subsidies to fund compliance repairs. Our results indicate testing providers have an overall negative view towards regulatory price caps but a majority would voluntarily participate in a subsidized repair program. Following completion of the project, we anticipate Salt Lake County regulators will better understand where the testing program experiences cost inefficiencies and the impact on test providers and motorists of introducing price cap and repair subsidies. If demonstrated to increase cost efficiencies and increases in pollution-reducing repairs, local programmatic improvements like these often serve as powerful examples of change other localities are quick to emulate.

### Code:
1. [Data Glance](https://github.com/capstoneproject2019airquality/capstone_code_sharing/blob/master/Data%20Glance/data_glance_update_yc3420.ipynb)
  - PLEASE NOTE: the team did not receive permission to publicly share county-provided data
  - Filter rejects
  - Retest analysis
  - Get stats: pass/fail/reject percentage by station  
  - Link station info and testing record files and calculate:  
    1) Average testing cost and total cost  
    2) Number of test per facility

2. [Data Sampling](https://github.com/capstoneproject2019airquality/capstone_code_sharing/blob/master/Data%20Sampling/data_sampling.ipynb)
  - Selected ~35 samples from the original dataset with stratified sampling
  - Due to low response rate, we added more samples to ensure that we got 35 effective answers
 
3. [Emission Test Data analysis](https://github.com/capstoneproject2019airquality/capstone_code_sharing/blob/master/Emission%20Test%20Data%20Analysis/pass_fail_analysis_v3.ipynb)
  - Cleaning and munging .txt of vehicle-level test data using R's Tidyverse package to prepare for modeling
  - High-level analysis on initial emision test pass/fail rates using Python's Pandas package

4. [Final Paper](https://github.com/capstoneproject2019airquality/capstone_code_sharing/blob/master/Final%20Paper/air_quality_final.pdf)
  - Rendering of content in R Markdown and LaTeX

5. [Mapping Data Preparation](https://github.com/capstoneproject2019airquality/capstone_code_sharing/blob/master/Mapping%20Data%20Preparation/Mapping_yc3420.ipynb)
  - Cleaned and merged datasets for mapping
  - Used ArcGIS for mapping and spatial analysis
  - Maps can be viewed [here](https://drive.google.com/open?id=1_RUWiXNjXRbj_tAb_H6AaePHDXV_AatY)

6. [Application](https://github.com/capstoneproject2019airquality/capstone_code_sharing/blob/master/Web%20Application/app_0719_Gavin.py)
  - Displayed locations of testing facilities with detailed information on each of them and filter feature based on zip code and price range
  - Developed with [Dash](https://pypi.org/project/dash/)
  - [Deployed](https://jz3309capstone.herokuapp.com/) Dash app on Heroku ([Instruction](https://dash.plot.ly/deployment))
7. [Website](https://github.com/capstoneproject2019airquality/capstone-website)
  - Used [HTML5 UP](https://html5up.net) site template
  - Website Link: https://capstoneproject2019airquality.github.io/capstone-website/


### [Presentation](https://docs.google.com/presentation/d/1pZGm5TyhvfBVFyYlPeTtQkFEGlsaPTrwDwA7ffx5mLY/edit?usp=sharing)
