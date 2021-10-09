import xarray as xr
import matplotlib.pyplot as plt
import numpy as np 

from FTTutils import readutils as read
from FTTutils import averaging_utils as avg

# These are the tools to do the individual tests

#-------Volcanoes------------
# num_a4 globally averaged at the model level closest to 70hPa
def testvolc(compareto,volcfiles,runshortname):
    """Performing the volcanic test
    Input: compaareto = the flag to decide whether to compare to LENS2 or B1850 or both
           volcfiles = the file listing for the volcanic test for your test case
           runshortname = the shortname for labelling the test case
    """
    # Read in the test data
    members = [xr.open_mfdataset(i, combine='nested', concat_dim=['time'], parallel=True).sel(lev=70, method='nearest') for i in volcfiles]
    dat = xr.concat(members, dim='M', join='override')
    dat = read.fixcesmtime(dat)
    dat = dat.groupby('time.year').mean(['time','lon'])
    dat = avg.cosweightlat(dat,-90,90).num_a4.persist()
    
    if ((compareto =='LENS2') | (compareto == 'BOTH')):
        lens2 = xr.open_dataset('/glade/work/islas/CVCWG/forcing_test_tool/LENS2/num_a4_70hpa.nc')
    if ((compareto == '1850') | (compareto == 'BOTH')):
        b1850 = xr.open_dataset('/glade/work/islas/CVCWG/forcing_test_tool/B1850/num_a4_70hpa.nc')
    
    # Plotting the plot
    fig = plt.figure(figsize=(16,16))
    ax = fig.add_axes([0.1,0.7,0.6,0.28])
    ax.set_title('Volcano test: num_a4, global mean, ~70hPa', fontsize=14)
    ax.set_ylabel('num_a4', fontsize=12)
    
    if ((compareto == 'LENS2') | (compareto == 'BOTH')):
        ax.fill_between(lens2.year, lens2.min_volc, lens2.max_volc, color='red', alpha=0.5)
        ax.plot(lens2.year, lens2.mean_volc, color='red', linewidth=3, label='LENS2')
    if ((compareto == '1850') | (compareto == 'BOTH')):
        ax.fill_between(lens2.year, np.zeros(lens2.year.size)+np.array(b1850.min_volc), np.zeros(lens2.year.size)+np.array(b1850.max_volc),
                        color='gray', alpha=0.5)
        ax.plot(lens2.year, np.zeros(lens2.year.size) + np.array(b1850.mean_volc), color='gray', linewidth=3, label='B1850')
    
    
    for imem in np.arange(0,dat.M.size,1):
        if (imem == 0):
            ax.plot(dat.year, dat.isel(M=imem), color='royalblue', label=runshortname)
        else:
            ax.plot(dat.year, dat.isel(M=imem), color='royalblue')
            
    ax.legend() 
    return fig  

#--------Solar------------------------
#SOLIN globally averaged
def testsolar(compareto, solarfiles, runshortname):
    """Performing the solar test
    Input: compaareto = the flag to decide whether to compare to LENS2 or B1850 or both
           solarfiles = the file listing for the solar test for your test case
           runshortname = the shortname for labelling the test case
    """

    members = [xr.open_mfdataset(i, combine='nested', concat_dim=['time'], parallel=True).sel(lev=70, method='nearest') for i in solarfiles]
    dat = xr.concat(members, dim='M', join='override')
    dat = read.fixcesmtime(dat)
    dat = dat.groupby('time.year').mean(['time','lon'])
    dat = avg.cosweightlat(dat,-90,90).SOLIN.persist()

    if ((compareto =='LENS2') | (compareto == 'BOTH')):
        lens2 = xr.open_dataset('/glade/work/islas/CVCWG/forcing_test_tool/LENS2/SOLIN.nc')
    if ((compareto == '1850') | (compareto == 'BOTH')):
        b1850 = xr.open_dataset('/glade/work/islas/CVCWG/forcing_test_tool/B1850/SOLIN.nc')

    # Plotting the plot
    fig = plt.figure(figsize=(16,16))
    ax = fig.add_axes([0.1,0.7,0.6,0.28])
    ax.set_title('Solar test: SOLIN, global mean', fontsize=14)
    ax.set_ylabel('SOLIN', fontsize=12)

    if ((compareto == 'LENS2') | (compareto == 'BOTH')):
        ax.fill_between(lens2.year, lens2.min_SOLIN, lens2.max_SOLIN, color='red', alpha=0.5)
        ax.plot(lens2.year, lens2.mean_SOLIN, color='red', linewidth=3, label='LENS2')
    if ((compareto == '1850') | (compareto == 'BOTH')):
        ax.fill_between(lens2.year, np.zeros(lens2.year.size)+np.array(b1850.min_SOLIN), np.zeros(lens2.year.size)+np.array(b1850.max_SOLIN),
                        color='gray', alpha=0.5)
        ax.plot(lens2.year, np.zeros(lens2.year.size) + np.array(b1850.mean_SOLIN), color='gray', linewidth=3, label='B1850')


    for imem in np.arange(0,dat.M.size,1):
        if (imem == 0):
            ax.plot(dat.year, dat.isel(M=imem), color='royalblue', label=runshortname)
        else:
            ax.plot(dat.year, dat.isel(M=imem), color='royalblue')

    ax.legend()
    return fig







