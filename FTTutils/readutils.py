import xarray as xr
import numpy as np

def fixcesmtime(dat,timebndsvar='time_bnds'):
    """ Fix the CESM timestamp using the average of time_bnds"""
    timebndavg = np.array(dat.isel(M=0)[timebndsvar],
                     dtype='datetime64[s]').view('i8').mean(axis=1).astype('datetime64[s]')
    dat['time'] = timebndavg
    return dat


def readpicontrol(files, timebndsvar='time_bnds'):
    """Read in the piControl data and use the average of time_bnds"""
    dat = xr.open_mfdataset(files, coords='minimal', decode_times='False')
    timebnds = dat[timebndsvar]
    diff = np.array(timebnds.isel(nbnd=1)) - np.array(timebnds.isel(nbnd=0))
    diff = diff/2.
    newtime = np.array(timebnds.isel(nbnd=0)) + diff
    dat['time'] = newtime
    return dat
