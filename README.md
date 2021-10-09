# Forcing test tool 

This is a package for checking that the forcings applied in CESM simulations are working as expected.  It uses model output and forcings are compared against those within the CESM2 large ensemble

### Installing Utilities

Assuming you have cloned this github repostory to $DIR, in order to install the python functions located in ./FTTutils which form the basis of this package you will need to do the following

```bash
cd $DIR
pip install -e . --user
```

## Metrics considered 

* **Volcanoes** = Annual mean num\_a4, globally averaged at the model level closest to 70hPa.
* **Solar** = Annual mean SOLIN, globally averaged

## Instructions

This tool can be run using the notebook RUN\_THE\_DIAGS.ipynb.  The user will have to modify the "User defined options" cell to specify the file locations, project code etc.  Here you can also specify what dataset to compare to.  The choices are...

* **LENS2** = Compare to the second 50 members of the CESM2 large ensemble (i.e., those with smoothed biomass burning).  The minimum to maximum range used range from the minimum to maximum ensemble member.
* **1850** = Compare to the 1850 pre-industrial control.  The minimum to maximum range shown is the mean +/- 2 times the interannual standard deviation
* **BOTH** = Compare to both LENS2 and the CMIP6 pre-industrial control

Users may also need to modify the set-up of the dask cluster depending on the size of their dataset.

