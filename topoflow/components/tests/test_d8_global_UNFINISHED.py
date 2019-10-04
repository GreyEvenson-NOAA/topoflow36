
# Copyright (c) 2001-2013, Scott D. Peckham

#---------------------------------------------------------------------

# from topoflow.utils      import tf_utils  # (not used)

#-------------------------------------------
# For use outside of the TopoFlow package.
#-------------------------------------------
## import tf_utils  # (not used)

#---------------------------------------------------------------------
#
#   unit_test()
#
#---------------------------------------------------------------------
def unit_test(TREYNOR=False, KY_SUB=False, BEAVER=False,
              SILENT=False, REPORT=True):

    #---------------------------------------------------------------
    # NOTE! The tests will appear to fail if the existing flow
    #       grid used for comparison was computed using a flat
    #       resolution method other than "Iterative linking".
    #
    # The KY_Sub and Beaver DEMs were processed using RiverTools
    # 3.0 using the WGS_1984 ellipsoid model for computing lengths
    # and areas.  The "Iterative linking" method was used for both
    # as the "Flat resolution method", to make them comparable to
    # the ones generated by functions in d8_base.py and
    # fill_pits.py.  Older version of these data sets used other
    # methods and can't be compared directly.
    #
    # Make sure that LINK_FLATS=True, LR_PERIODIC=False, and
    # TB_PERIODIC=False in CFG file.
    #
    # NB! There is another "local" test in update_area_grid().
    #
    # NB! "d8.A_units" is read from CFG file "*_d8.cfg" and needs
    #     to be km^2 whenever RT3_TEST is used.
    #---------------------------------------------------------------
    if not(TREYNOR or KY_SUB or BEAVER):
        TREYNOR = True
    start = time.time()

    #------------------------------------------------------
    # Example of DEM with fixed-angle pixels (Geographic)
    #     min(da) = 6802.824074169645  [m^2]
    #     max(da) = 6837.699120083246  [m^2]
    #     min(A)  =    0.000000000000  [km^2]
    #     max(A)  =  807.063354492188  [km^2]
    #------------------------------------------------------
    if (KY_SUB):
        # cfg_directory = '/Applications/Erode/Data/KY_Sub/'
        cfg_directory = '/home/csdms/models/erode/0.5/share/data/KY_Sub/'
        cfg_prefix    = 'KY_Sub'

    #------------------------------------------------
    # Example of DEM with fixed-length pixels (UTM)
    #     min(da) = 900.000  [m^2]
    #     max(da) = 900.000  [m^2]
    #     min(A)  =   0.000000000000  [km^2]
    #     max(A)  = 681.914184570312  [km^2]
    #------------------------------------------------
    if (BEAVER):
        # cfg_directory = '/Applications/Erode/Data/Beaver_Creek_KY/'
        cfg_directory = '/home/csdms/models/erode/0.5/share/data/Beaver_Creek_KY/'
        cfg_prefix    = 'Beaver'
    if (TREYNOR):
        # cfg_directory = '/Applications/Erode/Data/Treynor_Iowa/'
        cfg_directory = '/home/csdms/models/erode/0.5/share/data/Treynor_Iowa/'
        cfg_prefix    = 'Treynor'
        
    #-------------------------------------------------
    # NOTE: The Treynor_Iowa DEM has no depressions!
    #-------------------------------------------------   
    # cfg_directory = tf_utils.TF_Test_Directory()
    # cfg_prefix    = tf_utils.TF_Test_Site_Prefix()
  
    d8 = d8_component()
    d8.CCA    = False
    d8.DEBUG  = True
    d8.SILENT = SILENT
    d8.REPORT = REPORT

    #--------------------------
    # Change to cfg_directory
    #--------------------------
    os.chdir( cfg_directory )

    d8.initialize(cfg_prefix=cfg_prefix, mode="driver",
                  SILENT=SILENT, REPORT=REPORT)
    d8.RT3_TEST = True  # (compare flow and area grid to RT3)
    d8.update(SILENT=SILENT, REPORT=REPORT)
    print('grid nx =', d8.nx)
    print('grid ny =', d8.ny)
    print('Run time =', (time.time() - start), ' [secs]')
    print('Finished with unit_test().')
    print(' ')
                
#   unit_test()
#---------------------------------------------------------------------
