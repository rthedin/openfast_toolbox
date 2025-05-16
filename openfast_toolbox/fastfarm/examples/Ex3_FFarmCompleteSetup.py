""" 
Setup a FAST.Farm suite of cases based on input parameters.

The extent of the high res and low res domain are setup according to the guidelines:
    https://openfast.readthedocs.io/en/dev/source/user/fast.farm/ModelGuidance.html

NOTE: If driving FAST.Farm using TurbSim inflow, the resulting boxes are necessary to
      build the final FAST.Farm case and are not provided as part of this repository. 
      If driving FAST.Farm using LES inflow, the VTK boxes are not necessary to exist.

"""

from openfast_toolbox.fastfarm.FASTFarmCaseCreation import FFCaseCreation

def main():

    # -----------------------------------------------------------------------------
    # USER INPUT: Modify these
    #             For the d{t,s}_{high,low}_les paramters, use AMRWindSimulation.py
    # -----------------------------------------------------------------------------

    # ----------- Case absolute path
    path = '/complete/path/of/your/case'
    
    # ----------- General hard-coded parameters
    cmax     = 5      # maximum blade chord (m)
    fmax     = 10/6   # maximum excitation frequency (Hz)
    Cmeander = 1.9    # Meandering constant (-)

    # ----------- Wind farm
    # The wts dictionary holds information of each wind turbine. The allowed entries
    # are: x, y, z, D, zhub, cmax, fmax, Cmeander, and phi_deg. The phi_deg is the
    # only entry that is optional and is related to floating platform heading angle,
    # given in degrees. The angle phi_deg is not illustrated on the example below.
    D = 240
    zhub = 150
    wts  = {
              0 :{'x':0.0,     'y':0,       'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              1 :{'x':1852.0,  'y':0,       'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              2 :{'x':3704.0,  'y':0,       'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              3 :{'x':5556.0,  'y':0,       'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              4 :{'x':7408.0,  'y':0,       'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              5 :{'x':1852.0,  'y':1852.0,  'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              6 :{'x':3704.0,  'y':1852.0,  'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              7 :{'x':5556.0,  'y':1852.0,  'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              8 :{'x':7408.0,  'y':1852.0,  'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              9 :{'x':3704.0,  'y':3704.0,  'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              10:{'x':5556.0,  'y':3704.0,  'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
              11:{'x':7408.0,  'y':3704.0,  'z':0.0,  'D':D,  'zhub':zhub,  'cmax':cmax,  'fmax':fmax,  'Cmeander':Cmeander},
            }
    refTurb_rot = 0
    
    # ----------- Additional variables
    tmax = 1800     # Total simulation time
    nSeeds = 6      # Number of different seeds
    zbot = 1        # Bottom of your domain
    mod_wake = 1    # Wake model. 1: Polar, 2: Curl, 3: Cartesian
    
    # ----------- Desired sweeps
    vhub       = [10]
    shear      = [0.2]
    TIvalue    = [10]
    inflow_deg = [0]
    
    # ----------- Turbine parameters
    # Set the yaw of each turbine for wind dir. One row for each wind direction.
    yaw_init = None
    
    # ----------- Execution parameters
    ffbin = '/full/path/to/your/binary/.../bin/FAST.Farm'

    # ----------- Inflow type (LES or TS)
    inflowType = 'TS'  # Choose 'LES' or 'TS'
    # If LES, then set the inflowPath below
    # inflowPath = '/full/path/to/LES/case'

    # -----------------------------------------------------------------------------
    # ----------- Template files
    templatePath            = '/full/path/where/template/files/are'
    
    # Put None on any input that is not applicable to your case
    # Files should be in templatePath
    templateFiles = {
        "EDfilename"              : 'ElastoDyn.T',
        'SEDfilename'             : None,  #'SimplifiedElastoDyn.T',
        'HDfilename'              : None,  # 'HydroDyn.dat', # ending with .T for per-turbine HD, .dat for holisitc
        'MDfilename'              : None,  # 'MoorDyn.T',    # ending with .T for per-turbine MD, .dat for holistic
        'SSfilename'              : None,  # 'SeaState.dat',
        'SrvDfilename'            : 'ServoDyn.T',
        'ADfilename'              : 'AeroDyn.dat',
        'ADskfilename'            : 'AeroDisk.dat',
        'SubDfilename'            : 'SubDyn.dat',
        'IWfilename'              : 'InflowWind.dat',
        'BDfilepath'              : None,
        'bladefilename'           : 'Blade.dat',
        'towerfilename'           : 'Tower.dat',
        'turbfilename'            : 'Model.T',
        'libdisconfilepath'       : '/full/path/to/controller/libdiscon.so',
        'controllerInputfilename' : 'DISCON.IN',
        'coeffTablefilename'      : 'CpCtCq.csv',
        'hydroDatapath'           : None,  # '/full/path/to/hydroData',
        'FFfilename'              : 'Model_FFarm.fstf',

        # TurbSim setups
        'turbsimLowfilepath'      : './SampleFiles/template_Low_InflowXX_SeedY.inp',
        'turbsimHighfilepath'     : './SampleFiles/template_HighT1_InflowXX_SeedY.inp'
    }
    
    # SLURM scripts
    slurm_TS_high           = './SampleFiles/runAllHighBox.sh'
    slurm_TS_low            = './SampleFiles/runAllLowBox.sh'
    slurm_FF_single         = './SampleFiles/runFASTFarm_cond0_case0_seed0.sh'


    # -----------------------------------------------------------------------------
    # END OF USER INPUT
    # -----------------------------------------------------------------------------


    # Initial setup
    case = FFCaseCreation(path, wts, tmax, zbot, vhub, shear, TIvalue, inflow_deg,
                          ffbin=ffbin, mod_wake=mod_wake, yaw_init=yaw_init,
                          nSeeds=nSeeds,
                          inflowType=inflowType,
                          #inflowPath=inflowPath, # if LES, uncomment this line
                          refTurb_rot=refTurb_rot, verbose=1)

    case.setTemplateFilename(templatePath, templateFiles)

    # Get domain paramters
    case.getDomainParameters()

    # Organize file structure
    case.copyTurbineFilesForEachCase()

    # TurbSim setup
    if inflowType == 'TS':
        case.TS_low_setup()
        case.TS_low_slurm_prepare(slurm_TS_low)
        #case.TS_low_slurm_submit()

        case.TS_high_setup()
        case.TS_high_slurm_prepare(slurm_TS_high)
        #case.TS_high_slurm_submit()

    # Final setup
    case.FF_setup()
    case.FF_slurm_prepare(slurm_FF_single)
    #case.FF_slurm_submit()


if __name__ == '__main__':
    # This example cannot be fully run.
    pass
