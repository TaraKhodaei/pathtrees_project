<div align="center"><img src="https://raw.githubusercontent.com/TaraKhodaei/pathtrees_project/main/images/pathtrees_logo.jpg" width="420"/></div>


Python package **PATHTREES** enables the construction, visualization and exploration of the continuous tree landscape interior of the convex hull of given starting trees, using insights from the Billera-Holmes-Vogtmann treespace.



## $\color{purple}{\textsf{Usage}}$
    pathtrees.py [-h] [-o OUTPUTDIR] [-v] [-p PLOTFILE] [-n NUMPATHTREES]
                        [-b NUMBESTTREES] [-r NUM_RANDOM_TREES] [-g OUTGROUP]
                        [-i NUM_ITERATIONS] [-e] [-hull] [-gtp] [-nel] [-c COMPARE_TREES]
                        [-interp INTERPOLATION]
                        STARTTREES DATAFILE


## $\color{purple}{\textsf{Positional Arguments}}$

    STARTTREES     mandatory input file that holds a set of trees in Newick format

    DATAFILE       mandatory input file that holds a sequence data set in PHYLIP format



## $\color{purple}{\textsf{Optional Arguments}}$

**-h, --help**
> show this help message and exi  

<br/>

**-o OUTPUTDIR, --output OUTPUTDI**
> directory that holds the output files

<br/>

**-v, --verbose**
> Do not remove the intermediate files generated by GPT

<br/>

**-p PLOTFILE, --plot PLOTFILE** 
> Create an MDS plot from the generated distances

<br/>

**-n NUMPATHTREES, --np NUMPATHTREES, --numpathtrees NUMPATHTREES**
> Number of trees along the path between two initial trees

<br/>

**-b NUMBESTTREES, --best NUMBESTTREES, --numbesttrees NUMBESTTREES**
> Number of trees selected from the best likliehood trees for the next round of refinement

<br/>

**-r NUM_RANDOM_TREES, --randomtrees NUM_RANDOM_TREES**
> Generate num_random_trees rooted trees using the sequence data individual names.

<br/>

**-g OUTGROUP, --outgroup OUTGROUP**
> Forces an outgroup when generating random trees.                       

<br/>

**-i NUM_ITERATIONS, --iterate NUM_ITERATIONS**
> * With specified NUM_ITERATIONS > 1, PATHTREESS will run NUM_ITERATIONS iterations. In each iteration, this will add an iteration number to the outputdir, and also adds iteration to the plotting.
> * Otherwise, it just runs one iteration.                         

<br/>

**-e, --extended**
> If the phylip dataset is in the extended format, use this.    

<br/>

**-hull, --convex_hull**
> * Extracts the convex hull of input sample trees and considers them as starting trees in the first iteration to generate pairwise pathtrees. 
> * If false, it directly considers input sample trees as starting trees in the first iteration to generate pairwise pathtrees.                       

<br/>

**-gtp, --gtp_distance**
> * Use GTP derived geodesic distance for MDS plotting [slower]
> * If false, use weighted Robinson-Foulds distance for MDS plotting [faster]

<br/>

**-nel, --neldermead**
> * Use Nelder-Mead optimization method to optimize branchlengths [slower], 
> * If false, use Newton-Raphson to optimize branchlengths [fast]

<br/>

**-c, --compare_trees**
> * String "D1" considers my two trees (PAUP_MAP in data folder) to be plotted and compared with the best tree of PATHTREES for first dataset,
> * String "D2" considers my two trees (PAUP_RXML_bropt in data folder) to be plotted and compared with the best tree of PATHTREES, 
> * String "user_trees" considers user_trees to be plotted and compared with the best tree of PATHTREES, 
> * Otherwise it considers no extra trees to be plotted and compared       

<br/>

**-interp, --interpolate**
> * Use interpolation scipy.interpolate.griddata for interpolation [more overshooting], or use scipy.interpolate.Rbf [less overshooting]. 
> * String "rbf" considers scipy.interpolate.Rbf, Radial basis function (RBF) thin-plate spline interpolation, with default smoothness=1e-10. 
> * String "rbf,s_value", e.g. "rbf,0.0001", considers scipy.interpolate.Rbf with smoothness=0.0001.
> * String "cubic" considers scipy.interpolate.griddata, cubic spline interpolation. 
> * Otherwise, with None interpolation, it considers default scipy.interpolate.Rbf with smoothness=1e-10


    

## $\color{purple}{\textsf{Application To Real Data}}$

## $\color{purple}{\textsf{First Dataset D1}}$
___
Primates of 1141 base pairs of the mitochondrial cytochrome b gene of 23 primate taxa.<br/>

> **Input for Generating Boundary Trees:**
> * **"D1.sampletrees"** is a sample of around 1000 trees in Newick format which are extracted from RevBayes for D1 <br/>
> (find that in folder "data").
> * **"D1.phy"** is an mandatory input file that holds a sequence data set in PHYLIP format <br/>
> (find that in folder "data").

<br/>

> **Extracting Boundary Trees:**
> * Input data should be in the same directory as "pathtrees.py".<br/>
> ```
> python pathtrees.py -hull D1.sampletrees D1.phy
> ```
> * Output : **Boundary_Trees** <br/>
> (find that renamed as "D1.boundarytrees" in folder "data")

<br/>

> **Experiment 1.1**.<br/>
> ```
> python pathtrees.py -n 3 -gtp -c D1 -p myplot -o output D1.boundarytrees D1.phy
> ```
> <div align="center"><img src="https://raw.githubusercontent.com/TaraKhodaei/pathtrees_project/main/images/D1_GTP_rbf_s1e-10_n3.png" width="1000"/></div>

<br/>

> **Experiment 1.2**.<br/>
> ```
> python pathtrees.py -n 3 -b 15 -gtp -c usertrees -p myplot -o output D1.boundarytrees D1.phy
> ``` 
> <div align="center"><img src="https://raw.githubusercontent.com/TaraKhodaei/pathtrees_project/main/images/D1_GTP_rbf_s1e-10_n3_b15_usertrees.png" width="1000"/></div>

<br/>

> **Experiment 1.3**.<br/>
> ```
> python pathtrees.py -n 3 -gtp -p myplot -o output D1.boundarytrees D1.phy
> ``` 
> <div align="center"><img src="https://raw.githubusercontent.com/TaraKhodaei/pathtrees_project/main/images/D1_GTP_rbf_s1e-10_n3_NoCompare.png" width="1000"/></div>





## $\color{purple}{\textsf{Second Dataset D2}}$

> **Experiment 2.1**.<br/>
> ```
> python pathtrees.py -e -i 2  -n 6,7 -b 100 -c D2 -p myplot -o output D2.boundarytrees D2.phy
> ``` 
> <div align="center"><img src="https://raw.githubusercontent.com/TaraKhodaei/pathtrees_project/main/images/D2_iter1_RF_rbf_s1e-10_n6_b100.png" width="1000"/></div>
> <div align="center"><img src="https://raw.githubusercontent.com/TaraKhodaei/pathtrees_project/main/images/D2_iter2_RF_rbf_s1e-10_n7.png" width="1000"/></div> 







