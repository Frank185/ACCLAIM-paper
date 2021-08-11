########################################
#
# @file 01logit.py
# @author: Michel Bierlaire, EPFL
# @date: Wed Dec 21 13:23:27 2011
#
#######################################

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *

#Parameters to be estimated
# Arguments:
#   - 1  Name for report; Typically, the same as the variable.
#   - 2  Starting value.
#   - 3  Lower bound.
#   - 4  Upper bound.
#   - 5  0: estimate the parameter, 1: keep it fixed.



SIGMA_iti = Beta('SIGMA_iti',0,-100,100,0 )
SIGMA_itia = Beta('SIGMA_itia',0,-100,100,0 )
SIGMA_itib = Beta('SIGMA_itib',0,-100,100,0 )
b_male  = Beta('b_male',0,-100,100,0 )
b_male_L  = Beta('b_male_L',0,-100,100,0 )
b_male_N  = Beta('b_male_N',0,-100,100,0 )
b_male_P  = Beta('b_male_P',0,-100,100,0 )
b_male_S  = Beta('b_male_S',0,-100,100,0 )
b_income_high = Beta('b_income_high',0,-100,100,0 )
b_income_med = Beta('b_income_med',0,-100,100,0 )
b_high_edu = Beta('b_high_edu',0,-100,100,0 )
b_full_empl  = Beta('b_full_empl',0,-100,100,0 )
b_self_empl  = Beta('b_self_empl',0,-100,100,0 )
b_above50y = Beta('b_above50y',0,-100,100,0 )
b_purp_pers = Beta('b_purp_pers',0,-100,100,0 )
b_purp_bus = Beta('b_purp_bus',0,-100,100,0 )
b_purp_pers_bus = Beta('b_purp_pers_bus',0,-100,100,0 )
b_livinginLondon = Beta('b_livinginLondon',0,-100,100,0 )
b_eth_white_L = Beta('b_eth_white_L',0,-100,100,0 )
b_eth_asian_L = Beta('b_eth_asian_L',0,-100,100,0 )
b_eth_black_L = Beta('b_eth_black_L',0,-100,100,0 )
b_eth_white_N = Beta('b_eth_white_N',0,-100,100,0 )
b_eth_asian_N = Beta('b_eth_asian_N',0,-100,100,0 )
b_eth_black_N = Beta('b_eth_black_N',0,-100,100,0 )
b_eth_white_S = Beta('b_eth_white_S',0,-100,100,0 )
b_eth_asian_S = Beta('b_eth_asian_S',0,-100,100,0 )
b_eth_black_S = Beta('b_eth_black_S',0,-100,100,0 )
b_eth_white_P = Beta('b_eth_white_P',0,-100,100,0 )
b_eth_asian_P = Beta('b_eth_asian_P',0,-100,100,0 )
b_eth_black_P = Beta('b_eth_blackv',0,-100,100,0 )
b_full_empl_L   = Beta('b_full_empl_L',0,-100,100,0 ) 
b_above50y_L    = Beta('b_above50y_L',0,-100,100,0 ) 
b_income_high_L = Beta('b_income_high_L',0,-100,100,0 )
b_full_empl_N   = Beta('b_full_empl_N',0,-100,100,0 ) 
b_above50y_N    = Beta('b_above50y_N',0,-100,100,0 ) 
b_income_high_N = Beta('b_income_high_N',0,-100,100,0 ) 
b_full_empl_S   = Beta('b_full_empl_S',0,-100,100,0 ) 
b_above50y_S    = Beta('b_above50y_S',0,-100,100,0 ) 
b_income_high_S = Beta('b_income_high_S',0,-100,100,0 ) 
b_full_empl_P   = Beta('b_full_empl_P',0,-100,100,0 ) 
b_above50y_P    = Beta('b_above50y_P',0,-100,100,0 ) 
b_income_high_P = Beta('b_income_high_P',0,-100,100,0 ) 
b_part_empl_L   = Beta('b_part_empl_L',0,-100,100,0 ) 
b_part_empl_N   = Beta('b_part_empl_N',0,-100,100,0 ) 
b_part_empl_S   = Beta('b_part_empl_S',0,-100,100,0 ) 
b_part_empl_P   = Beta('b_part_empl_P',0,-100,100,0 ) 
b_self_empl_L   = Beta('b_self_empl_L',0,-100,100,0 ) 
b_self_empl_N   = Beta('b_self_empl_N',0,-100,100,0 ) 
b_self_empl_S   = Beta('b_self_empl_S',0,-100,100,0 ) 
b_self_empl_P   = Beta('b_self_empl_P',0,-100,100,0 ) 
b_Bef_VirtBus = Beta('b_Bef_VirtBus',0,-100,100,0 )
b_Bef_VirtPers = Beta('b_Bef_VirtPers',0,-100,100,0 )
b_Dur_VirtBus = Beta('b_Dur_VirtBus',0,-100,100,0 )
b_Dur_VirtPers = Beta('b_Dur_VirtPers',0,-100,100,0 )
b_Aft_VirtBus = Beta('b_Aft_VirtBus',0,-100,100,0 )
b_Aft_VirtPers = Beta('b_Aft_VirtPers',0,-100,100,0 )
b_Aft_FlyBus = Beta('b_Aft_FlyBus',0,-100,100,0 )
b_Aft_FlyPers = Beta('b_Aft_FlyPers',0,-100,100,0 )
b_Bef_VirtBus_L = Beta('b_Bef_VirtBus_L',0,-100,100,0 )
b_Bef_VirtPers_L = Beta('b_Bef_VirtPers_L',0,-100,100,0 )
b_Dur_VirtBus_L = Beta('b_Dur_VirtBus_L',0,-100,100,0 )
b_Dur_VirtPers_L = Beta('b_Dur_VirtPers_L',0,-100,100,0 )
b_Aft_VirtBus_L = Beta('b_Aft_VirtBus_L',0,-100,100,0 )
b_Aft_VirtPers_L = Beta('b_Aft_VirtPers_L',0,-100,100,0 )
b_Aft_FlyBus_L = Beta('b_Aft_FlyBus_L',0,-100,100,0 )
b_Aft_FlyPers_L = Beta('b_Aft_FlyPers_L',0,-100,100,0 )
b_Bef_VirtBus_N = Beta('b_Bef_VirtBus_N',0,-100,100,0 )
b_Bef_VirtPers_N = Beta('b_Bef_VirtPers_N',0,-100,100,0 )
b_Dur_VirtBus_N = Beta('b_Dur_VirtBus_N',0,-100,100,0 )
b_Dur_VirtPers_N = Beta('b_Dur_VirtPers_N',0,-100,100,0 )
b_Aft_VirtBus_N = Beta('b_Aft_VirtBus_N',0,-100,100,0 )
b_Aft_VirtPers_N = Beta('b_Aft_VirtPers_N',0,-100,100,0 )
b_Aft_FlyBus_N = Beta('b_Aft_FlyBus_N',0,-100,100,0 )
b_Aft_FlyPers_N = Beta('b_Aft_FlyPers_N',0,-100,100,0 )
b_Bef_VirtBus_S = Beta('b_Bef_VirtBus_S',0,-100,100,0 )
b_Bef_VirtPers_S = Beta('b_Bef_VirtPers_S',0,-100,100,0 )
b_Dur_VirtBus_S = Beta('b_Dur_VirtBus_S',0,-100,100,0 )
b_Dur_VirtPers_S = Beta('b_Dur_VirtPers_S',0,-100,100,0 )
b_Aft_VirtBus_S = Beta('b_Aft_VirtBus_S',0,-100,100,0 )
b_Aft_VirtPers_S = Beta('b_Aft_VirtPers_S',0,-100,100,0 )
b_Aft_FlyBus_S = Beta('b_Aft_FlyBus_S',0,-100,100,0 )
b_Aft_FlyPers_S = Beta('b_Aft_FlyPers_S',0,-100,100,0 )
b_Bef_VirtBus_P = Beta('b_Bef_VirtBus_P',0,-100,100,0 )
b_Bef_VirtPers_P = Beta('b_Bef_VirtPers_P',0,-100,100,0 )
b_Dur_VirtBus_P = Beta('b_Dur_VirtBus_P',0,-100,100,0 )
b_Dur_VirtPers_P = Beta('b_Dur_VirtPers_P',0,-100,100,0 )
b_Aft_VirtBus_P = Beta('b_Aft_VirtBus_P',0,-100,100,0 )
b_Aft_VirtPers_P = Beta('b_Aft_VirtPers_P',0,-100,100,0 )
b_Aft_FlyBus_P = Beta('b_Aft_FlyBus_P',0,-100,100,0 )
b_Aft_FlyPers_P = Beta('b_Aft_FlyPers_P',0,-100,100,0 )
b_reserved = Beta('b_reserved',0,-100,100,0 )
b_trusting = Beta('b_trusting',0,-100,100,0 )
b_lazy = Beta('b_lazy',0,-100,100,0 )
b_relaxed = Beta('b_relaxed',0,-100,100,0 )
b_artistic = Beta('b_artistic',0,-100,100,0 )
b_sociable = Beta('b_sociable',0,-100,100,0 )
b_othersfault = Beta('b_othersfault',0,-100,100,0 )
b_thoroughjob = Beta('b_thoroughjob',0,-100,100,0 )
b_easynervous = Beta('b_easynervous',0,-100,100,0 )
b_activeimag = Beta('b_activeimag',0,-100,100,0 )
ASC_iti_L    = Beta('ASC_iti_L',0,-100,100,0)
ASC_iti_S    = Beta('ASC_iti_S',0,-100,100,0)
ASC_iti_P    = Beta('ASC_iti_P',0,-100,100,0)
ASC_iti_N    = Beta('ASC_iti_N',0,-100,100,0)
b_Cost_N_bus = Beta('b_Cost_N_bus',0,-100,100,0)
b_Cost_L_SH_bus   = Beta('b_Cost_L_SH_bus',0,-100,100,0)
b_Cost_L_MH_bus   = Beta('b_Cost_L_MH_bus',0,-100,100,0)
b_Cost_L_LH_bus   = Beta('b_Cost_L_LH_bus',0,-100,100,0)
b_Cost_L_SH   = Beta('b_Cost_L_SH',0,-100,100,0)
b_Cost_L_MH   = Beta('b_Cost_L_MH',0,-100,100,0)
b_Cost_L_LH   = Beta('b_Cost_L_LH',0,-100,100,0)
b_Cost_P_SH_bus   = Beta('b_Cost_P_SH_bus',0,-100,100,0)
b_Cost_P_MH_bus   = Beta('b_Cost_P_MH_bus',0,-100,100,0)
b_Cost_P_LH_bus   = Beta('b_Cost_P_LH_bus',0,-100,100,0)
b_Cost_P_SH   = Beta('b_Cost_P_SH',0,-100,100,0)
b_Cost_P_MH   = Beta('b_Cost_P_MH',0,-100,100,0)
b_Cost_P_LH   = Beta('b_Cost_P_LH',0,-100,100,0)
b_Cost_S_SH_bus   = Beta('b_Cost_S_SH_bus',0,-100,100,0)
b_Cost_S_MH_bus   = Beta('b_Cost_S_MH_bus',0,-100,100,0)
b_Cost_S_LH_bus   = Beta('b_Cost_S_LH_bus',0,-100,100,0)
b_Cost_S_SH   = Beta('b_Cost_S_SH',0,-100,100,0)
b_Cost_S_MH   = Beta('b_Cost_S_MH',0,-100,100,0)
b_Cost_S_LH   = Beta('b_Cost_S_LH',0,-100,100,0)
b_Cost_N_SH_bus   = Beta('b_Cost_N_SH_bus',0,-100,100,0)
b_Cost_N_MH_bus   = Beta('b_Cost_N_MH_bus',0,-100,100,0)
b_Cost_N_LH_bus   = Beta('b_Cost_N_LH_bus',0,-100,100,0)
b_Cost_N_SH   = Beta('b_Cost_N_SH',0,-100,100,0)
b_Cost_N_MH   = Beta('b_Cost_N_MH',0,-100,100,0)
b_Cost_N_LH   = Beta('b_Cost_N_LH',0,-100,100,0)
b_Cost_N_SMH_bus = Beta('b_Cost_N_SMH_bus',0,-100,100,0)
b_deptime_L_LMH_bus = Beta('b_deptime_L_LMH_bus',0,-100,100,0)
b_deptime_N_bus  = Beta('b_deptime_N_bus',0,-100,100,0)
b_deptime_SH = Beta('b_deptime_SH',0,-100,100,0)
b_deptime_L   = Beta('b_deptime_L',0,-100,100,0)
b_deptime_P   = Beta('b_deptime_P',0,-100,100,0)
b_deptime_S   = Beta('b_deptime_S',0,-100,100,0)
b_deptime_N   = Beta('b_deptime_N',0,-100,100,0)
b_deptime_L_SH = Beta('b_deptime_L_SH',0,-100,100,0)
b_deptime_P_SH = Beta('b_deptime_P_SH',0,-100,100,0)
b_deptime_S_SH = Beta('b_deptime_S_SH',0,-100,100,0)
b_deptime_N_SH = Beta('b_deptime_N_SH',0,-100,100,0)
b_deptime_L_MH = Beta('b_deptime_L_MH',0,-100,100,0)
b_deptime_P_MH = Beta('b_deptime_P_MH',0,-100,100,0)
b_deptime_S_MH = Beta('b_deptime_S_MH',0,-100,100,0)
b_deptime_N_MH = Beta('b_deptime_N_MH',0,-100,100,0)
b_deptime_L_LH = Beta('b_deptime_L_LH',0,-100,100,0)
b_deptime_P_LH = Beta('b_deptime_P_LH',0,-100,100,0)
b_deptime_S_LH = Beta('b_deptime_S_LH',0,-100,100,0)
b_deptime_N_LH = Beta('b_deptime_N_LH',0,-100,100,0)
b_deptime_L_LMH = Beta('b_deptime_L_LMH',0,-100,100,0)
b_deptime_P_LMH = Beta('b_deptime_P_LMH',0,-100,100,0)
b_deptime_S_LMH = Beta('b_deptime_S_LMH',0,-100,100,0)
b_deptime_N_LMH = Beta('b_deptime_N_LMH',0,-100,100,0)
b_deptime_S_SMH_Bus = Beta('b_deptime_S_SMH_Bus',0,-100,100,0)
b_deptime_L_SH_bus = Beta('b_deptime_L_SH_bus',0,-100,100,0)
b_deptime_P_SH_bus = Beta('b_deptime_P_SH_bus',0,-100,100,0)
b_deptime_S_SH_bus = Beta('b_deptime_S_SH_bus',0,-100,100,0)
b_deptime_N_SH_bus = Beta('b_deptime_N_SH_bus',0,-100,100,0)
b_deptime_L_MH_bus = Beta('b_deptime_L_MH_bus',0,-100,100,0)
b_deptime_P_MH_bus = Beta('b_deptime_P_MH_bus',0,-100,100,0)
b_deptime_S_MH_bus = Beta('b_deptime_S_MH_bus',0,-100,100,0)
b_deptime_N_MH_bus = Beta('b_deptime_N_MH_bus',0,-100,100,0)
b_deptime_L_LH_bus = Beta('b_deptime_L_LH_bus',0,-100,100,0)
b_deptime_P_LH_bus = Beta('b_deptime_P_LH_bus',0,-100,100,0)
b_deptime_S_LH_bus = Beta('b_deptime_S_LH_bus',0,-100,100,0)
b_deptime_N_LH_bus = Beta('b_deptime_N_LH_bus',0,-100,100,0)
b_deptime_L_LMH_bus = Beta('b_deptime_L_LMH_bus',0,-100,100,0)
b_deptime_P_LMH_bus = Beta('b_deptime_P_LMH_bus',0,-100,100,0)
b_deptime_S_LMH_bus = Beta('b_deptime_S_LMH_bus',0,-100,100,0)
b_deptime_N_LMH_bus = Beta('b_deptime_N_LMH_bus',0,-100,100,0)
b_arrtime_N_bus = Beta('b_arrtime_N_bus',0,-100,100,0)
b_arrtime_P_LMH = Beta('b_arrtime_P_LMH',0,-100,100,0)
b_arrtime_P_LMH_bus = Beta('b_arrtime_P_LMH_bus',0,-100,100,0)
b_arrtime_S_LMH_bus = Beta('b_arrtime_S_LMH_bus',0,-100,100,0)
b_arrtime_L = Beta('b_arrtime_L',0,-100,100,0)
b_arrtime_S = Beta('b_arrtime_S',0,-100,100,0)
b_arrtime_P = Beta('b_arrtime_P',0,-100,100,0)
b_arrtime_N = Beta('b_arrtime_N',0,-100,100,0)
b_arrtime_L_SH =  Beta('b_arrtime_L_SH',0,-100,100,0)
b_arrtime_P_SH =  Beta('b_arrtime_P_SH',0,-100,100,0)
b_arrtime_S_SH =  Beta('b_arrtime_S_SH',0,-100,100,0)
b_arrtime_N_SH =  Beta('b_arrtime_N_SH',0,-100,100,0)
b_arrtime_L_MH =  Beta('b_arrtime_L_MH',0,-100,100,0)
b_arrtime_P_MH =  Beta('b_arrtime_P_MH',0,-100,100,0)
b_arrtime_S_MH =  Beta('b_arrtime_S_MH',0,-100,100,0)
b_arrtime_N_MH =  Beta('b_arrtime_N_MH',0,-100,100,0)
b_arrtime_L_LH =  Beta('b_arrtime_L_LH',0,-100,100,0)
b_arrtime_P_LH =  Beta('b_arrtime_P_LH',0,-100,100,0)
b_arrtime_S_LH =  Beta('b_arrtime_S_LH',0,-100,100,0)
b_arrtime_N_LH =  Beta('b_arrtime_N_LH',0,-100,100,0)
b_arrtime_L_SH_bus =  Beta('b_arrtime_L_SH_bus',0,-100,100,0)
b_arrtime_P_SH_bus =  Beta('b_arrtime_P_SH_bus',0,-100,100,0)
b_arrtime_S_SH_bus =  Beta('b_arrtime_S_SH_bus',0,-100,100,0)
b_arrtime_N_SH_bus =  Beta('b_arrtime_N_SH_bus',0,-100,100,0)
b_arrtime_L_MH_bus =  Beta('b_arrtime_L_MH_bus',0,-100,100,0)
b_arrtime_P_MH_bus =  Beta('b_arrtime_P_MH_bus',0,-100,100,0)
b_arrtime_S_MH_bus =  Beta('b_arrtime_S_MH_bus',0,-100,100,0)
b_arrtime_N_MH_bus =  Beta('b_arrtime_N_MH_bus',0,-100,100,0)
b_arrtime_L_LH_bus =  Beta('b_arrtime_L_LH_bus',0,-100,100,0)
b_arrtime_P_LH_bus =  Beta('b_arrtime_P_LH_bus',0,-100,100,0)
b_arrtime_S_LH_bus =  Beta('b_arrtime_S_LH_bus',0,-100,100,0)
b_arrtime_N_LH_bus =  Beta('b_arrtime_N_LH_bus',0,-100,100,0)
b_transfer = Beta('b_transfer',0,-100,100,0)
b_transfer_L = Beta('b_transfer_L',0,-100,100,0)
b_transfer_LMH= Beta('b_transfer_LMH',0,-100,100,0)
b_transfer_LMH_bus= Beta('b_transfer_LMH_bus',0,-100,100,0)
b_transfer_SH= Beta('b_transfer_SH',0,-100,100,0)
b_transfer_SH_bus= Beta('b_transfer_SH_bus',0,-100,100,0)
b_transfer_L_SH = Beta('b_transfer_L_SH',0,-100,100,0)
b_transfer_S_SH = Beta('b_transfer_S_SH',0,-100,100,0)
b_transfer_P_SH = Beta('b_transfer_P_SH',0,-100,100,0)
b_transfer_N_SH = Beta('b_transfer_N_SH',0,-100,100,0)
b_transfer_L_MH = Beta('b_transfer_L_MH',0,-100,100,0)
b_transfer_S_MH = Beta('b_transfer_S_MH',0,-100,100,0)
b_transfer_P_MH = Beta('b_transfer_P_MH',0,-100,100,0)
b_transfer_N_MH = Beta('b_transfer_N_MH',0,-100,100,0)
b_transfer_L_LH = Beta('b_transfer_L_LH',0,-100,100,0)
b_transfer_S_LH = Beta('b_transfer_S_LH',0,-100,100,0)
b_transfer_P_LH = Beta('b_transfer_P_LH',0,-100,100,0)
b_transfer_N_LH = Beta('b_transfer_N_LH',0,-100,100,0)
b_transfer_L_SH_bus = Beta('b_transfer_L_SH_bus',0,-100,100,0)
b_transfer_S_SH_bus = Beta('b_transfer_S_SH_bus',0,-100,100,0)
b_transfer_P_SH_bus = Beta('b_transfer_P_SH_bus',0,-100,100,0)
b_transfer_N_SH_bus = Beta('b_transfer_N_SH_bus',0,-100,100,0)
b_transfer_L_MH_bus = Beta('b_transfer_L_MH_bus',0,-100,100,0)
b_transfer_S_MH_bus = Beta('b_transfer_S_MH_bus',0,-100,100,0)
b_transfer_P_MH_bus = Beta('b_transfer_P_MH_bus',0,-100,100,0)
b_transfer_N_MH_bus = Beta('b_transfer_N_MH_bus',0,-100,100,0)
b_transfer_L_LH_bus = Beta('b_transfer_L_LH_bus',0,-100,100,0)
b_transfer_S_LH_bus = Beta('b_transfer_S_LH_bus',0,-100,100,0)
b_transfer_P_LH_bus = Beta('b_transfer_P_LH_bus',0,-100,100,0)
b_transfer_N_LH_bus = Beta('b_transfer_N_LH_bus',0,-100,100,0)
b_transfer_L_LMH =  Beta('b_transfer_L_LMH',0,-100,100,0)
b_transfer_S_LMH =  Beta('b_transfer_S_LMH',0,-100,100,0)
b_transfer_P_LMH =  Beta('b_transfer_P_LMH',0,-100,100,0)
b_transfer_N_LMH =  Beta('b_transfer_N_LMH',0,-100,100,0)
b_transfer_L_LMH_bus =  Beta('b_transfer_L_LMH_bus',0,-100,100,0)
b_transfer_S_LMH_bus =  Beta('b_transfer_S_LMH_bus',0,-100,100,0)
b_transfer_P_LMH_bus =  Beta('b_transfer_P_LMH_bus',0,-100,100,0)
b_transfer_N_LMH_bus =  Beta('b_transfer_N_LMH_bus',0,-100,100,0)
b_transfer_L_bus =  Beta('b_transfer_L_bus',0,-100,100,0)
b_transfer_S_bus =  Beta('b_transfer_S_bus',0,-100,100,0)
b_transfer_P_bus =  Beta('b_transfer_P_bus',0,-100,100,0)
b_transfer_N_bus =  Beta('b_transfer_N_bus',0,-100,100,0)
Scale_N = Beta('Scale_N',1,0.001,1000,1)
Scale_S = Beta('Scale_S',1,0.001,1000,1)
Scale_P = Beta('Scale_P',1,0.001,1000,1)
SIGMA_iti = Beta('SIGMA_iti',0,-100,100,0 )
iti_RND = SIGMA_iti  * bioDraws('iti_RND')
SIGMA_iti_L = Beta('SIGMA_iti_L',0,-100,100,0 )
iti_RND_L = SIGMA_iti_L  * bioDraws('iti_RND_L')
SIGMA_iti_N = Beta('SIGMA_iti_N',0,-100,100,0 )
iti_RND_N = SIGMA_iti_N  * bioDraws('iti_RND_N')
SIGMA_iti_S = Beta('SIGMA_iti_S',0,-100,100,0 )
iti_RND_S = SIGMA_iti_S * bioDraws('iti_RND_S')
SIGMA_iti_P = Beta('SIGMA_iti_P',0,-100,100,0 )
iti_RND_P = SIGMA_iti_P  * bioDraws('iti_RND_P')

############################ 

London = (City == 1) 
NewYork = (City == 2) 
Shanghai = (City == 3) 
SaoPaulo = (City == 4) 
scale = London + NewYork * Scale_N + Shanghai * Scale_S + SaoPaulo * Scale_P
ppp_Shang = 4.175868532  
ppp_SaoPaulo = 2.399577218   
ppp_Lond = 0.775531 

###########################

Cost_a =   alt1_fare / 100
Cost_b =   alt2_fare / 100
Cost_L_a =   Cost_a / ppp_Lond
Cost_L_b =   Cost_b / ppp_Lond
Cost_S_a =   Cost_a / ppp_Shang
Cost_S_b =   Cost_b / ppp_Shang
Cost_P_a =   Cost_a / ppp_SaoPaulo
Cost_P_b =   Cost_b / ppp_SaoPaulo
Cost_N_a =   Cost_a 
Cost_N_b =   Cost_b 
SH = (Count == 1) | (Count == 2)
MH = (Count == 3) | (Count == 4)
LH = (Count == 5) | (Count == 6)


#### LONDON    ######### 
SH_L_a =      (b_Cost_L_SH * Cost_L_a        +   b_deptime_L_SH * alt1_tdep       +  b_arrtime_L_SH	* alt1_tarr        +  b_transfer_L * alt1_transf) * SH 
MH_L_a =      (b_Cost_L_MH * Cost_L_a        +   b_deptime_L_MH * alt1_tdep       +  b_arrtime_L_MH	* alt1_tarr        +  b_transfer_L * alt1_transf) * MH 
LH_L_a =      (b_Cost_L_LH * Cost_L_a        +   b_deptime_L_LH * alt1_tdep       +  b_arrtime_L_LH	* alt1_tarr        +  b_transfer_L * alt1_transf) * LH 

SH_L_b =      (b_Cost_L_SH * Cost_L_b        +   b_deptime_L_SH * alt2_tdep       +  b_arrtime_L_SH	* alt2_tarr        +  b_transfer_L * alt2_transf) * SH 
MH_L_b =      (b_Cost_L_MH * Cost_L_b        +   b_deptime_L_MH * alt2_tdep       +  b_arrtime_L_MH	* alt2_tarr        +  b_transfer_L * alt2_transf) * MH 
LH_L_b =      (b_Cost_L_LH * Cost_L_b        +   b_deptime_L_LH * alt2_tdep       +  b_arrtime_L_LH	* alt2_tarr        +  b_transfer_L * alt2_transf) * LH 

SH_L_a_bus =  (b_Cost_L_SH_bus  * Cost_L_a  +   b_deptime_L_SH_bus  * alt1_tdep   +  b_arrtime_L_SH_bus  * alt1_tarr   +  b_transfer_L_bus  * alt1_transf) * SH 
MH_L_a_bus  = (b_Cost_L_MH_bus  * Cost_L_a  +   b_deptime_L_LMH_bus  * alt1_tdep   +  b_arrtime_L_MH_bus  * alt1_tarr   +  b_transfer_L_bus  * alt1_transf) * MH 
LH_L_a_bus  = (b_Cost_L_LH_bus  * Cost_L_a  +   b_deptime_L_LMH_bus  * alt1_tdep   +  b_arrtime_L_LH_bus  * alt1_tarr   +  b_transfer_L_bus  * alt1_transf) * LH 

SH_L_b_bus  = (b_Cost_L_SH_bus  * Cost_L_b   +   b_deptime_L_SH_bus * alt2_tdep    +  b_arrtime_L_SH_bus 	* alt2_tarr   +  b_transfer_L_bus  * alt2_transf) * SH 
MH_L_b_bus  = (b_Cost_L_MH_bus  * Cost_L_b   +   b_deptime_L_LMH_bus  * alt2_tdep   +  b_arrtime_L_MH_bus 	* alt2_tarr   +  b_transfer_L_bus  * alt2_transf) * MH 
LH_L_b_bus  = (b_Cost_L_LH_bus  * Cost_L_b   +   b_deptime_L_LMH_bus  * alt2_tdep   +  b_arrtime_L_LH_bus 	* alt2_tarr   +  b_transfer_L_bus  * alt2_transf) * LH 



#### NY    #########
SH_N_a =      (b_Cost_N_SH * Cost_N_a        +   b_deptime_N_SH * alt1_tdep       +  b_arrtime_N_SH	* alt1_tarr        +  b_transfer_N_SH * alt1_transf) * SH 
MH_N_a =      (b_Cost_N_MH * Cost_N_a        +   b_deptime_N_LMH * alt1_tdep       +  b_arrtime_N_MH	* alt1_tarr        +  b_transfer_N_LMH * alt1_transf) * MH 
LH_N_a =      (b_Cost_N_LH * Cost_N_a        +   b_deptime_N_LMH * alt1_tdep       +  b_arrtime_N_LH	* alt1_tarr        +  b_transfer_N_LMH * alt1_transf) * LH 

SH_N_b =      (b_Cost_N_SH * Cost_N_b        +   b_deptime_N_SH * alt2_tdep       +  b_arrtime_N_SH	* alt2_tarr        +  b_transfer_N_SH * alt2_transf) * SH 
MH_N_b =      (b_Cost_N_MH * Cost_N_b        +   b_deptime_N_LMH * alt2_tdep       +  b_arrtime_N_MH	* alt2_tarr        +  b_transfer_N_LMH * alt2_transf) * MH 
LH_N_b =      (b_Cost_N_LH * Cost_N_b        +   b_deptime_N_LMH * alt2_tdep       +  b_arrtime_N_LH	* alt2_tarr        +  b_transfer_N_LMH * alt2_transf) * LH 

SH_N_a_bus =  (b_Cost_N_SMH_bus  * Cost_N_a  +   b_deptime_N_SH  * alt1_tdep   +  b_arrtime_N_SH  * alt1_tarr   +  b_transfer_N_SH  * alt1_transf) * SH 
MH_N_a_bus  = (b_Cost_N_SMH_bus  * Cost_N_a  +   b_deptime_N_LMH  * alt1_tdep   +  b_arrtime_N_MH  * alt1_tarr   +  b_transfer_N_LMH  * alt1_transf) * MH 
LH_N_a_bus  = (b_Cost_N_LH_bus  * Cost_N_a  +   b_deptime_N_LMH  * alt1_tdep   +  b_arrtime_N_LH  * alt1_tarr   +  b_transfer_N_LMH  * alt1_transf) * LH 

SH_N_b_bus  = (b_Cost_N_SMH_bus  * Cost_N_b   +   b_deptime_N_SH * alt2_tdep    +  b_arrtime_N_SH 	* alt2_tarr   +  b_transfer_N_SH  * alt2_transf) * SH 
MH_N_b_bus  = (b_Cost_N_SMH_bus  * Cost_N_b   +   b_deptime_N_LMH  * alt2_tdep   +  b_arrtime_N_MH 	* alt2_tarr   +  b_transfer_N_LMH  * alt2_transf) * MH 
LH_N_b_bus  = (b_Cost_N_LH_bus  * Cost_N_b   +   b_deptime_N_LMH  * alt2_tdep   +  b_arrtime_N_LH 	* alt2_tarr   +  b_transfer_N_LMH  * alt2_transf) * LH 



#### Shanghai    ######### 
SH_S_a =      (b_Cost_S_SH * Cost_S_a        +   b_deptime_S_SH * alt1_tdep       +  b_arrtime_S_SH	* alt1_tarr        +  b_transfer_S_SH * alt1_transf) * SH 
MH_S_a =      (b_Cost_S_MH * Cost_S_a        +   b_deptime_S_LMH * alt1_tdep       +  b_arrtime_S_MH	* alt1_tarr        +  b_transfer_S_LMH * alt1_transf) * MH 
LH_S_a =      (b_Cost_S_LH * Cost_S_a        +   b_deptime_S_LMH * alt1_tdep       +  b_arrtime_S_LH	* alt1_tarr        +  b_transfer_S_LMH * alt1_transf) * LH 

SH_S_b =      (b_Cost_S_SH * Cost_S_b        +   b_deptime_S_SH * alt2_tdep       +  b_arrtime_S_SH	* alt2_tarr        +  b_transfer_S_SH * alt2_transf) * SH 
MH_S_b =      (b_Cost_S_MH * Cost_S_b        +   b_deptime_S_LMH * alt2_tdep       +  b_arrtime_S_MH	* alt2_tarr        +  b_transfer_S_LMH * alt2_transf) * MH 
LH_S_b =      (b_Cost_S_LH * Cost_S_b        +   b_deptime_S_LMH * alt2_tdep       +  b_arrtime_S_LH	* alt2_tarr        +  b_transfer_S_LMH * alt2_transf) * LH 

SH_S_a_bus =  (b_Cost_S_SH_bus  * Cost_S_a  +   b_deptime_S_SMH_Bus  * alt1_tdep   +  b_arrtime_S_SH_bus  * alt1_tarr   +  b_transfer_S_SH_bus  * alt1_transf) * SH 
MH_S_a_bus  = (b_Cost_S_MH_bus  * Cost_S_a  +   b_deptime_S_SMH_Bus  * alt1_tdep   +  b_arrtime_S_LMH_bus  * alt1_tarr   +  b_transfer_S_LMH_bus  * alt1_transf) * MH 
LH_S_a_bus  = (b_Cost_S_LH_bus  * Cost_S_a  +   b_deptime_S_LH_bus  * alt1_tdep   +  b_arrtime_S_LMH_bus  * alt1_tarr   +  b_transfer_S_LMH_bus  * alt1_transf) * LH 

SH_S_b_bus  = (b_Cost_S_SH_bus  * Cost_S_b   +   b_deptime_S_SMH_Bus * alt2_tdep    +  b_arrtime_S_SH_bus 	* alt2_tarr   +  b_transfer_S_SH_bus  * alt2_transf) * SH 
MH_S_b_bus  = (b_Cost_S_MH_bus  * Cost_S_b   +   b_deptime_S_SMH_Bus  * alt2_tdep   +  b_arrtime_S_LMH_bus 	* alt2_tarr   +  b_transfer_S_LMH_bus  * alt2_transf) * MH 
LH_S_b_bus  = (b_Cost_S_LH_bus  * Cost_S_b   +   b_deptime_S_LH_bus  * alt2_tdep   +  b_arrtime_S_LMH_bus 	* alt2_tarr   +  b_transfer_S_LMH_bus  * alt2_transf) * LH 



#### SaoPaulo    ######### 
SH_P_a =      (b_Cost_P_SH * Cost_P_a        +   b_deptime_P_SH * alt1_tdep       +  b_arrtime_P_SH	* alt1_tarr        +  b_transfer_P_SH * alt1_transf) * SH 
MH_P_a =      (b_Cost_P_MH * Cost_P_a        +   b_deptime_P_LMH * alt1_tdep       +  b_arrtime_P_LMH	* alt1_tarr        +  b_transfer_P_LMH * alt1_transf) * MH 
LH_P_a =      (b_Cost_P_LH * Cost_P_a        +   b_deptime_P_LMH * alt1_tdep       +  b_arrtime_P_LMH	* alt1_tarr        +  b_transfer_P_LMH * alt1_transf) * LH 

SH_P_b =      (b_Cost_P_SH * Cost_P_b        +   b_deptime_P_SH * alt2_tdep       +  b_arrtime_P_SH	* alt2_tarr        +  b_transfer_P_SH * alt2_transf) * SH 
MH_P_b =      (b_Cost_P_MH * Cost_P_b        +   b_deptime_P_LMH * alt2_tdep       +  b_arrtime_P_LMH	* alt2_tarr        +  b_transfer_P_LMH * alt2_transf) * MH 
LH_P_b =      (b_Cost_P_LH * Cost_P_b        +   b_deptime_P_LMH * alt2_tdep       +  b_arrtime_P_LMH	* alt2_tarr        +  b_transfer_P_LMH * alt2_transf) * LH 

SH_P_a_bus =  (b_Cost_P_SH_bus  * Cost_P_a  +   b_deptime_P_SH_bus  * alt1_tdep   +  b_arrtime_P_SH_bus  * alt1_tarr   +  b_transfer_P_SH_bus  * alt1_transf) * SH 
MH_P_a_bus  = (b_Cost_P_MH_bus  * Cost_P_a  +   b_deptime_P_LMH_bus  * alt1_tdep   +  b_arrtime_P_LMH_bus  * alt1_tarr   +  b_transfer_P_LMH_bus  * alt1_transf) * MH 
LH_P_a_bus  = (b_Cost_P_LH_bus  * Cost_P_a  +   b_deptime_P_LMH_bus  * alt1_tdep   +  b_arrtime_P_LMH_bus  * alt1_tarr   +  b_transfer_P_LMH_bus  * alt1_transf) * LH 

SH_P_b_bus  = (b_Cost_P_SH_bus  * Cost_P_b   +   b_deptime_P_SH_bus * alt2_tdep    +  b_arrtime_P_SH_bus 	* alt2_tarr   +  b_transfer_P_SH_bus  * alt2_transf) * SH 
MH_P_b_bus  = (b_Cost_P_MH_bus  * Cost_P_b   +   b_deptime_P_LMH_bus  * alt2_tdep   +  b_arrtime_P_LMH_bus 	* alt2_tarr   +  b_transfer_P_LMH_bus  * alt2_transf) * MH 
LH_P_b_bus  = (b_Cost_P_LH_bus  * Cost_P_b   +   b_deptime_P_LMH_bus  * alt2_tdep   +  b_arrtime_P_LMH_bus 	* alt2_tarr   +  b_transfer_P_LMH_bus  * alt2_transf) * LH 


#############################################
#  Sociodemographics


below50y = (Q4_2 < 4) 
male =  (Q4_1 == 2)
above50y = (Q4_2 >= 4) & (Q4_2 < 7)
single =  (Q4_3 == 1) 
married =  (Q4_3 == 2) 
high_edu  = (Q4_6 == 6) |  (Q4_6 == 7) | (Q4_6 == 8)
full_empl  = (Q4_4 == 1)
part_empl = (Q4_4 == 2)
self_empl  =	(Q4_4 == 3)
eth_asian = (Q4_9 == 1)
eth_black = (Q4_9 == 2)
eth_white = (Q4_9 == 5) 
income_low = (Income >= 1) & (Income <= 3)
income_med = (Income == 4) | (Income == 5) 
income_high = (Income == 6) | ( (Income == 7) * NewYork ) 
purp_pers = (Purpose_SP == 1)
purp_bus= (Purpose_SP == 2)
purp_pers_bus= (Purpose_SP == 3)
purp_bus_tot =   (Purpose_SP == 2) |  (Purpose_SP == 3)

Socioeconomic =  b_full_empl_L * full_empl * London \
             + b_above50y_L * above50y * London   + b_above50y_N * above50y * NewYork       \
               + b_income_high_L * income_high * London   

Bef_VirtBus = (Q147_1 <= 2)
Bef_VirtPers = (Q147_2 <= 2)
Dur_VirtBus = (Q148_1 <= 2)
Dur_VirtPers = (Q148_2 <= 2)
Aft_VirtBus = (Q150_1 >= 4)
Aft_VirtPers = (Q150_2 >= 4)
Aft_FlyBus = (Q150_3 >= 4)
Aft_FlyPers = (Q150_4 >= 4)


BeforeCov_bus   =  b_Bef_VirtBus_N * Bef_VirtBus * NewYork 
DuringCovid_bus = b_Dur_VirtBus_L * Dur_VirtBus * London 
AfterCov_bus    = b_Aft_VirtBus_L * Aft_VirtBus * London 

BeforeCov_pers   = b_Bef_VirtPers_S * Bef_VirtPers * Shanghai  
DuringCovid_pers = b_Dur_VirtPers_L * Dur_VirtPers * London + b_Dur_VirtPers_N * Dur_VirtPers * NewYork  + b_Dur_VirtPers_S * Dur_VirtPers * Shanghai  + b_Dur_VirtPers_P * Dur_VirtPers * SaoPaulo 
AfterCov_pers    = b_Aft_VirtPers_L * Aft_VirtPers * London + b_Aft_VirtPers_N * Aft_VirtPers * NewYork  + b_Aft_VirtPers_S * Aft_VirtPers * Shanghai  + b_Aft_VirtPers_P * Aft_VirtPers * SaoPaulo 

reserved = (Q154_1 >= 4)
trusting = (Q154_2 >= 4)
lazy = (Q154_3 >= 4)
relaxed = (Q154_4 >= 4)
artistic = (Q154_5 >= 4)
sociable = (Q154_6 >= 4)
othersfault = (Q154_7 >= 4)
thoroughjob = (Q154_8 >= 4)
easynervous = (Q154_9 >= 4)
activeimag =  (Q154_10 >= 4)

 
personality = b_reserved *reserved  \
            + b_trusting *trusting \
            + b_lazy *lazy     \
            + b_relaxed *relaxed \
            + b_othersfault *othersfault \
			+ b_thoroughjob *thoroughjob \
			+ b_easynervous *easynervous



b_latent_afr = Beta('b_latent_afr',0.3352,-100,100,0 )
b_latent_saf = Beta('b_latent_saf',0.3352,-100,100,0 )
b_latent_qua = Beta('b_latent_qua',0.3352,-100,100,0 )

################Latent 1 London###########


b_latent_afr_L = Beta('b_latent_afr_L',0.3352,-100,100,0 )
LV_const_L = Beta('LV_const_L',3.98582,-100,100,0 )
lv_sigma_L = Beta('lv_sigma_L',2.123,-100,100,0)
LV_above50y_L = Beta('LV_above50y_L',0.398999,-100,100,0 )
LV_male_L = Beta('LV_male_L',0.06838,-100,100,0 )
LV_self_empl_L = Beta('LV_self_empl_L',0.06838,-100,100,0 )
LV_high_edu_L = Beta('LV_high_edu_L',0.06838,-100,100,0 )
LV_income_high_L = Beta('LV_income_high_L',0.06838,-100,100,0 )
LV_income_low_L =  Beta('LV_income_low_L',0.06838,-100,100,0 )
LV_purp_pers_L =  Beta('LV_purp_pers_L',0.06838,-100,100,0 )
LV_below50y_L =  Beta('LV_below50y_L',0.06838,-100,100,0 )
b_reserved_L_1 = Beta('b_reserved_L_1',0,-100,100,0 )
b_trusting_L_1 = Beta('b_trusting_L_1',0,-100,100,0 )
b_lazy_L_1 = Beta('b_lazy_L_1',0,-100,100,0 )
b_relaxed_L_1 = Beta('b_relaxed_L_1',0,-100,100,0 )
b_artistic_L_1 = Beta('b_artistic_L_1',0,-100,100,0 )
b_sociable_L_1 = Beta('b_sociable_L_1',0,-100,100,0 )
b_othersfault_L_1 = Beta('b_othersfault_L_1',0,-100,100,0 )
b_thoroughjob_L_1 = Beta('b_thoroughjob_L_1',0,-100,100,0 )
b_easynervous_L_1 = Beta('b_easynervous_L_1',0,-100,100,0 )
b_activeimag_L_1 = Beta('b_activeimag_L_1',0,-100,100,0 )

ASC_Ind_1_L = Beta('ASC_Ind_1_L',0,-100,100,1 )

alfa_LV_I1_L = Beta('alfa_LV_I1_L',1,-100,100,1 )

sig_Ind_1_L = Beta('sig_Ind_1_L',-0.508863,-100,100,0)

ASC_Ind_2_L = Beta('ASC_Ind_2_L',0.733218,-100,100,0 )

alfa_LV_I2_L = Beta('alfa_LV_I2_L',0.838539,-100,100,0 )

sig_Ind_2_L = Beta('sig_Ind_2_L',-0.289028,-100,100,0 )

ASC_Ind_3_L = Beta('ASC_Ind_3_L',0.330353,-100,100,0 )

alfa_LV_I3_L = Beta('alfa_LV_I3_L',0.880481,-100,100,0 )

sig_Ind_3_L = Beta('sig_Ind_3_L',-0.206661,-100,100,0 )

ASC_Ind_4_L = Beta('ASC_Ind_4_L',0.341769,-100,100,0)

alfa_LV_I4_L = Beta('alfa_LV_I4_L',0.93511,-100,100,0)

sig_Ind_4_L = Beta('sig_Ind_4_L',-0.128357,-100,100,0)

ASC_Ind_5_L = Beta('ASC_Ind_5_L',0.341769,-100,100,0)

alfa_LV_I5_L = Beta('alfa_LV_I5_L',0.93511,-100,100,0)

sig_Ind_5_L = Beta('sig_Ind_5_L',-0.128357,-100,100,0)

ASC_Ind_6_L = Beta('ASC_Ind_6_L',0.341769,-100,100,0)

alfa_LV_I6_L = Beta('alfa_LV_I6_L',0.93511,-100,100,0)

sig_Ind_6_L = Beta('sig_Ind_6_L',-0.128357,-100,100,0)

omega_L =  bioDraws('omega_L')


personality_afr_L =  b_othersfault_L_1 * othersfault  + b_reserved_L_1 * reserved 


latent_afr_L = LV_const_L + omega_L * exp(lv_sigma_L) + LV_male_L * male  + LV_below50y_L * below50y \
+ personality_afr_L



#Indicators


Ind_1_L 			= Q151_1
t_Ind_1_L 		= (Ind_1_L - ASC_Ind_1_L - alfa_LV_I1_L * latent_afr_L) / exp(sig_Ind_1_L)
f_Ind_1_L 		= bioNormalPdf(t_Ind_1_L) / exp(sig_Ind_1_L)
#
Ind_2_L 			= Q151_3
t_Ind_2_L 		= (Ind_2_L - ASC_Ind_2_L - alfa_LV_I2_L * latent_afr_L) / exp(sig_Ind_2_L)
f_Ind_2_L 		= bioNormalPdf(t_Ind_2_L) / exp(sig_Ind_2_L)


Ind_3_L 			= Q151_5
t_Ind_3_L 		= (Ind_3_L - ASC_Ind_3_L - alfa_LV_I3_L * latent_afr_L) / exp(sig_Ind_3_L)
f_Ind_3_L 		= bioNormalPdf(t_Ind_3_L) / exp(sig_Ind_3_L)

Ind_4_L 			= Q151_6
t_Ind_4_L 		= (Ind_4_L - ASC_Ind_4_L - alfa_LV_I4_L * latent_afr_L) / exp(sig_Ind_4_L)
f_Ind_4_L 		= bioNormalPdf(t_Ind_4_L) / exp(sig_Ind_4_L)

Ind_5_L 			= Q151_13
t_Ind_5_L 		= (Ind_5_L - ASC_Ind_5_L - alfa_LV_I5_L * latent_afr_L) / exp(sig_Ind_5_L)
f_Ind_5_L 		= bioNormalPdf(t_Ind_5_L) / exp(sig_Ind_5_L)





##Latent 2 London###########

b_latent_saf_L = Beta('b_latent_saf_L_2',0.3352,-100,100,0 )

LV_const_L_2 = Beta('LV_const_L_2',3.98582,-100,100,0 )
lv_sigma_L_2 = Beta('lv_sigma_L_2',2.123,-100,100,0)

LV_above50y_L_2 = Beta('LV_above50y_L_2',0.398999,-100,100,0 )
LV_male_L_2 = Beta('LV_male_L_2',0.06838,-100,100,0 )
LV_self_empl_L_2 = Beta('LV_self_empl_L_2',0.06838,-100,100,0 )
LV_high_edu_L_2 = Beta('LV_high_edu_L_2',0.06838,-100,100,0 )
LV_income_high_L_2 = Beta('LV_income_high_L_2',0.06838,-100,100,0 )
LV_income_low_L_2 =  Beta('LV_income_low_L_2',0.06838,-100,100,0 )
LV_purp_pers_L_2 =  Beta('LV_purp_pers_L_2',0.06838,-100,100,0 )
LV_below50y_L_2 =  Beta('LV_below50y_L_2',0.06838,-100,100,0 )

b_reserved_L_2 = Beta('b_reserved_L_2',0,-100,100,0 )
b_trusting_L_2 = Beta('b_trusting_L_2',0,-100,100,0 )
b_lazy_L_2 = Beta('b_lazy_L_2',0,-100,100,0 )
b_relaxed_L_2 = Beta('b_relaxed_L_2',0,-100,100,0 )
b_artistic_L_2 = Beta('b_artistic_L_2',0,-100,100,0 )
b_sociable_L_2 = Beta('b_sociable_L_2',0,-100,100,0 )
b_othersfault_L_2 = Beta('b_othersfault_L_2',0,-100,100,0 )
b_thoroughjob_L_2 = Beta('b_thoroughjob_L_2',0,-100,100,0 )
b_easynervous_L_2 = Beta('b_easynervous_L_2',0,-100,100,0 )
b_activeimag_L_2 = Beta('b_activeimag_L_2',0,-100,100,0 )


ASC_Ind_1_L_2 = Beta('ASC_Ind_1_L_2',0,-100,100,1 )

alfa_LV_I1_L_2 = Beta('alfa_LV_I1_L_2',1,-100,100,1 )

sig_Ind_1_L_2 = Beta('sig_Ind_1_L_2',-0.508863,-100,100,0)

ASC_Ind_2_L_2 = Beta('ASC_Ind_2_L_2',0.733218,-100,100,0 )

alfa_LV_I2_L_2 = Beta('alfa_LV_I2_L_2',0.838539,-100,100,0 )

sig_Ind_2_L_2 = Beta('sig_Ind_2_L_2',-0.289028,-100,100,0 )

ASC_Ind_3_L_2 = Beta('ASC_Ind_3_L_2',0.330353,-100,100,0 )

alfa_LV_I3_L_2 = Beta('alfa_LV_I3_L_2',0.880481,-100,100,0 )

sig_Ind_3_L_2 = Beta('sig_Ind_3_L_2',-0.206661,-100,100,0 )



omega_L_2 =  bioDraws('omega_L_2')


personality_saf_L =  b_othersfault_L_2 * othersfault


latent_saf_L = LV_const_L_2 + omega_L_2 * exp(lv_sigma_L_2) + LV_male_L_2 * male  + LV_below50y_L_2 * below50y \
+ personality_saf_L



#Indicators


Ind_1_L_2 			= Q151_7
t_Ind_1_L_2 		= (Ind_1_L_2 - ASC_Ind_1_L_2 - alfa_LV_I1_L_2 * latent_saf_L) / exp(sig_Ind_1_L_2)
f_Ind_1_L_2 		= bioNormalPdf(t_Ind_1_L_2) / exp(sig_Ind_1_L_2)
#
Ind_2_L_2 			= Q151_8
t_Ind_2_L_2 		= (Ind_2_L_2 - ASC_Ind_2_L_2 - alfa_LV_I2_L_2 * latent_saf_L) / exp(sig_Ind_2_L_2)
f_Ind_2_L_2 		= bioNormalPdf(t_Ind_2_L_2) / exp(sig_Ind_2_L_2)


Ind_3_L_2 			= Q151_9
t_Ind_3_L_2 		= (Ind_3_L_2 - ASC_Ind_3_L_2 - alfa_LV_I3_L_2 * latent_saf_L) / exp(sig_Ind_3_L_2)
f_Ind_3_L_2 		= bioNormalPdf(t_Ind_3_L_2) / exp(sig_Ind_3_L_2)



##Latent 3 London###########

b_latent_qua_L = Beta('b_latent_qua_L',0.3352,-100,100,0 )

LV_const_L_3 = Beta('LV_const_L_3',3.98582,-100,100,0 )
lv_sigma_L_3 = Beta('lv_sigma_L_3',2.123,-100,100,0)

LV_above50y_L_3 = Beta('LV_above50y_L_3',0.398999,-100,100,0 )
LV_male_L_3 = Beta('LV_male_L_3',0.06838,-100,100,0 )
LV_self_empl_L_3 = Beta('LV_self_empl_L_3',0.06838,-100,100,0 )
LV_high_edu_L_3 = Beta('LV_high_edu_L_3',0.06838,-100,100,0 )
LV_income_high_L_3 = Beta('LV_income_high_L_3',0.06838,-100,100,0 )
LV_income_low_L_3 =  Beta('LV_income_low_L_3',0.06838,-100,100,0 )
LV_purp_pers_L_3 =  Beta('LV_purp_pers_L_3',0.06838,-100,100,0 )
LV_below50y_L_3 =  Beta('LV_below50y_L_3',0.06838,-100,100,0 )

b_reserved_L_3 = Beta('b_reserved_L_3',0,-100,100,0 )
b_trusting_L_3 = Beta('b_trusting_L_3',0,-100,100,0 )
b_lazy_L_3 = Beta('b_lazy_L_3',0,-100,100,0 )
b_relaxed_L_3 = Beta('b_relaxed_L_3',0,-100,100,0 )
b_artistic_L_3 = Beta('b_artistic_L_3',0,-100,100,0 )
b_sociable_L_3 = Beta('b_sociable_L_3',0,-100,100,0 )
b_othersfault_L_3 = Beta('b_othersfault_L_3',0,-100,100,0 )
b_thoroughjob_L_3 = Beta('b_thoroughjob_L_3',0,-100,100,0 )
b_easynervous_L_3 = Beta('b_easynervous_L_3',0,-100,100,0 )
b_activeimag_L_3 = Beta('b_activeimag_L_3',0,-100,100,0 )


ASC_Ind_1_L_3 = Beta('ASC_Ind_1_L_3',0,-100,100,1 )

alfa_LV_I1_L_3 = Beta('alfa_LV_I1_L_3',1,-100,100,1 )

sig_Ind_1_L_3 = Beta('sig_Ind_1_L_3',-0.508863,-100,100,0)

ASC_Ind_2_L_3 = Beta('ASC_Ind_2_L_3',0.733218,-100,100,0 )

alfa_LV_I2_L_3 = Beta('alfa_LV_I2_L_3',0.838539,-100,100,0 )

sig_Ind_2_L_3 = Beta('sig_Ind_2_L_3',-0.289028,-100,100,0 )

ASC_Ind_3_L_3 = Beta('ASC_Ind_3_L_3',0.330353,-100,100,0 )

alfa_LV_I3_L_3 = Beta('alfa_LV_I3_L_3',0.880481,-100,100,0 )

sig_Ind_3_L_3 = Beta('sig_Ind_3_L_3',-0.206661,-100,100,0 )



omega_L_3 =  bioDraws('omega_L_3')

personality_qua_L =  b_othersfault_L_3 * othersfault

latent_qua_L = LV_const_L_3 + omega_L_3 * exp(lv_sigma_L_3) + LV_male_L_3 * male  \
+ personality_qua_L



#Indicators


Ind_1_L_3 			= Q151_10
t_Ind_1_L_3 		= (Ind_1_L_3 - ASC_Ind_1_L_3 - alfa_LV_I1_L_3 * latent_qua_L) / exp(sig_Ind_1_L_3)
f_Ind_1_L_3 		= bioNormalPdf(t_Ind_1_L_3) / exp(sig_Ind_1_L_3)

Ind_2_L_3 			= Q151_11
t_Ind_2_L_3 		= (Ind_2_L_3 - ASC_Ind_2_L_3 - alfa_LV_I2_L_3 * latent_qua_L) / exp(sig_Ind_2_L_3)
f_Ind_2_L_3 		= bioNormalPdf(t_Ind_2_L_3) / exp(sig_Ind_2_L_3)



################Latent NY###########

b_latent_afr_N = Beta('b_latent_afr_N',0.3352,-100,100,0 )

LV_const_N = Beta('LV_const_N',3.98582,-100,100,0 )
lv_sigma_N = Beta('lv_sigma_N',2.123,-100,100,0)

LV_above50y_N = Beta('LV_above50y_N',0.398999,-100,100,0 )
LV_male_N = Beta('LV_male_N',0.06838,-100,100,0 )
LV_self_empl_N = Beta('LV_self_empl_N',0.06838,-100,100,0 )
LV_high_edu_N = Beta('LV_high_edu_N',0.06838,-100,100,0 )
LV_income_high_N = Beta('LV_income_high_N',0.06838,-100,100,0 )
LV_income_low_N =  Beta('LV_income_low_N',0.06838,-100,100,0 )
LV_purp_pers_N =  Beta('LV_purp_pers_N',0.06838,-100,100,0 )
LV_below50y_N =  Beta('LV_below50y_N',0.06838,-100,100,0 )

b_reserved_N_1 = Beta('b_reserved_N_1',0,-100,100,0 )
b_trusting_N_1 = Beta('b_trusting_N_1',0,-100,100,0 )
b_lazy_N_1 = Beta('b_lazy_N_1',0,-100,100,0 )
b_relaxed_N_1 = Beta('b_relaxed_N_1',0,-100,100,0 )
b_artistic_N_1 = Beta('b_artistic_N_1',0,-100,100,0 )
b_sociable_N_1 = Beta('b_sociable_N_1',0,-100,100,0 )
b_othersfault_N_1 = Beta('b_othersfault_N_1',0,-100,100,0 )
b_thoroughjob_N_1 = Beta('b_thoroughjob_N_1',0,-100,100,0 )
b_easynervous_N_1 = Beta('b_easynervous_N_1',0,-100,100,0 )
b_activeimag_N_1 = Beta('b_activeimag_N_1',0,-100,100,0 )



ASC_Ind_1_N = Beta('ASC_Ind_1_N',0,-100,100,1 )

alfa_LV_I1_N = Beta('alfa_LV_I1_N',1,-100,100,1 )

sig_Ind_1_N = Beta('sig_Ind_1_N',-0.508863,-100,100,0)

ASC_Ind_2_N = Beta('ASC_Ind_2_N',0.733218,-100,100,0 )

alfa_LV_I2_N = Beta('alfa_LV_I2_N',0.838539,-100,100,0 )

sig_Ind_2_N = Beta('sig_Ind_2_N',-0.289028,-100,100,0 )

ASC_Ind_3_N = Beta('ASC_Ind_3_N',0.330353,-100,100,0 )

alfa_LV_I3_N = Beta('alfa_LV_I3_N',0.880481,-100,100,0 )

sig_Ind_3_N = Beta('sig_Ind_3_N',-0.206661,-100,100,0 )

ASC_Ind_4_N = Beta('ASC_Ind_4_N',0.341769,-100,100,0)

alfa_LV_I4_N = Beta('alfa_LV_I4_N',0.93511,-100,100,0)

sig_Ind_4_N = Beta('sig_Ind_4_N',-0.128357,-100,100,0)

ASC_Ind_5_N = Beta('ASC_Ind_5_N',0.341769,-100,100,0)

alfa_LV_I5_N = Beta('alfa_LV_I5_N',0.93511,-100,100,0)

sig_Ind_5_N = Beta('sig_Ind_5_N',-0.128357,-100,100,0)

ASC_Ind_6_N = Beta('ASC_Ind_6_L',0.341769,-100,100,0)

alfa_LV_I6_N = Beta('alfa_LV_I6_N',0.93511,-100,100,0)

sig_Ind_6_N = Beta('sig_Ind_6_N',-0.128357,-100,100,0)

omega_N =  bioDraws('omega_N')


personality_afr_N =  b_othersfault_N_1 * othersfault


latent_afr_N = LV_const_N + omega_N * exp(lv_sigma_N) + LV_male_N * male  + LV_below50y_N * below50y \
+ personality_afr_N



#Indicators


Ind_1_N 			= Q151_1
t_Ind_1_N 		= (Ind_1_N - ASC_Ind_1_N - alfa_LV_I1_N * latent_afr_N) / exp(sig_Ind_1_N)
f_Ind_1_N 		= bioNormalPdf(t_Ind_1_N) / exp(sig_Ind_1_N)
#
Ind_2_N 			= Q151_2
t_Ind_2_N 		= (Ind_2_N - ASC_Ind_2_N - alfa_LV_I2_N * latent_afr_N) / exp(sig_Ind_2_N)
f_Ind_2_N 		= bioNormalPdf(t_Ind_2_N) / exp(sig_Ind_2_N)


Ind_3_N 			= Q151_3
t_Ind_3_N 		= (Ind_3_N - ASC_Ind_3_N - alfa_LV_I3_N * latent_afr_N) / exp(sig_Ind_3_N)
f_Ind_3_N 		= bioNormalPdf(t_Ind_3_N) / exp(sig_Ind_3_N)

Ind_4_N 			= Q151_5
t_Ind_4_N 		= (Ind_4_N - ASC_Ind_4_N - alfa_LV_I4_N * latent_afr_N) / exp(sig_Ind_4_N)
f_Ind_4_N 		= bioNormalPdf(t_Ind_4_N) / exp(sig_Ind_4_N)

Ind_5_N 			= Q151_6
t_Ind_5_N 		= (Ind_5_N - ASC_Ind_5_N - alfa_LV_I5_N * latent_afr_N) / exp(sig_Ind_5_N)
f_Ind_5_N 		= bioNormalPdf(t_Ind_5_N) / exp(sig_Ind_5_N)


##Latent 2 NY###########

b_latent_saf_N = Beta('b_latent_saf_N_2',0.3352,-100,100,0 )

LV_const_N_2 = Beta('LV_const_N_2',3.98582,-100,100,0 )
lv_sigma_N_2 = Beta('lv_sigma_N_2',2.123,-100,100,0)

LV_above50y_N_2 = Beta('LV_above50y_N_2',0.398999,-100,100,0 )
LV_male_N_2 = Beta('LV_male_N_2',0.06838,-100,100,0 )
LV_self_empl_N_2 = Beta('LV_self_empl_N_2',0.06838,-100,100,0 )
LV_high_edu_N_2 = Beta('LV_high_edu_N_2',0.06838,-100,100,0 )
LV_income_high_N_2 = Beta('LV_income_high_N_2',0.06838,-100,100,0 )
LV_income_low_N_2 =  Beta('LV_income_low_N_2',0.06838,-100,100,0 )
LV_purp_pers_N_2 =  Beta('LV_purp_pers_N_2',0.06838,-100,100,0 )
LV_below50y_N_2 =  Beta('LV_below50y_N_2',0.06838,-100,100,0 )


b_reserved_N_2 = Beta('b_reserved_N_2',0,-100,100,0 )
b_trusting_N_2 = Beta('b_trusting_N_2',0,-100,100,0 )
b_lazy_N_2 = Beta('b_lazy_N_2',0,-100,100,0 )
b_relaxed_N_2 = Beta('b_relaxed_N_2',0,-100,100,0 )
b_artistic_N_2 = Beta('b_artistic_N_2',0,-100,100,0 )
b_sociable_N_2 = Beta('b_sociable_N_2',0,-100,100,0 )
b_othersfault_N_2 = Beta('b_othersfault_N_2',0,-100,100,0 )
b_thoroughjob_N_2 = Beta('b_thoroughjob_N_2',0,-100,100,0 )
b_easynervous_N_2 = Beta('b_easynervous_N_2',0,-100,100,0 )
b_activeimag_N_2 = Beta('b_activeimag_N_2',0,-100,100,0 )


ASC_Ind_1_N_2 = Beta('ASC_Ind_1_N_2',0,-100,100,1 )

alfa_LV_I1_N_2 = Beta('alfa_LV_I1_N_2',1,-100,100,1 )

sig_Ind_1_N_2 = Beta('sig_Ind_1_N_2',-0.508863,-100,100,0)

ASC_Ind_2_N_2 = Beta('ASC_Ind_2_N_2',0.733218,-100,100,0 )

alfa_LV_I2_N_2 = Beta('alfa_LV_I2_N_2',0.838539,-100,100,0 )

sig_Ind_2_N_2 = Beta('sig_Ind_2_N_2',-0.289028,-100,100,0 )

ASC_Ind_3_N_2 = Beta('ASC_Ind_3_N_2',0.330353,-100,100,0 )

alfa_LV_I3_N_2 = Beta('alfa_LV_I3_N_2',0.880481,-100,100,0 )

sig_Ind_3_N_2 = Beta('sig_Ind_3_N_2',-0.206661,-100,100,0 )



omega_N_2 =  bioDraws('omega_N_2')

personality_saf_N =   b_thoroughjob_N_2 * thoroughjob  

latent_saf_N = LV_const_N_2 + omega_N_2 * exp(lv_sigma_N_2) + LV_male_N_2 * male  + LV_below50y_N_2 * below50y \
+ personality_saf_N



#Indicators


Ind_1_N_2 			= Q151_7
t_Ind_1_N_2 		= (Ind_1_N_2 - ASC_Ind_1_N_2 - alfa_LV_I1_N_2 * latent_saf_N) / exp(sig_Ind_1_N_2)
f_Ind_1_N_2 		= bioNormalPdf(t_Ind_1_N_2) / exp(sig_Ind_1_N_2)
#
Ind_2_N_2 			= Q151_8
t_Ind_2_N_2 		= (Ind_2_N_2 - ASC_Ind_2_N_2 - alfa_LV_I2_N_2 * latent_saf_N) / exp(sig_Ind_2_N_2)
f_Ind_2_N_2 		= bioNormalPdf(t_Ind_2_N_2) / exp(sig_Ind_2_N_2)


Ind_3_N_2 			= Q151_9
t_Ind_3_N_2 		= (Ind_3_N_2 - ASC_Ind_3_N_2 - alfa_LV_I3_N_2 * latent_saf_N) / exp(sig_Ind_3_N_2)
f_Ind_3_N_2 		= bioNormalPdf(t_Ind_3_N_2) / exp(sig_Ind_3_N_2)



#Latent 3 NY###########

b_latent_qua_N = Beta('b_latent_qua_N',0.3352,-100,100,0 )

LV_const_N_3 = Beta('LV_const_N_3',3.98582,-100,100,0 )
lv_sigma_N_3 = Beta('lv_sigma_N_3',2.123,-100,100,0)

LV_above50y_N_3 = Beta('LV_above50y_N_3',0.398999,-100,100,0 )
LV_male_N_3 = Beta('LV_male_N_3',0.06838,-100,100,0 )
LV_self_empl_N_3 = Beta('LV_self_empl_N_3',0.06838,-100,100,0 )
LV_high_edu_N_3 = Beta('LV_high_edu_N_3',0.06838,-100,100,0 )
LV_income_high_N_3 = Beta('LV_income_high_N_3',0.06838,-100,100,0 )
LV_income_low_N_3 =  Beta('LV_income_low_N_3',0.06838,-100,100,0 )
LV_purp_pers_N_3 =  Beta('LV_purp_pers_N_3',0.06838,-100,100,0 )
LV_below50y_N_3 =  Beta('LV_below50y_N_3',0.06838,-100,100,0 )


b_reserved_N_3 = Beta('b_reserved_N_3',0,-100,100,0 )
b_trusting_N_3 = Beta('b_trusting_N_3',0,-100,100,0 )
b_lazy_N_3 = Beta('b_lazy_N_3',0,-100,100,0 )
b_relaxed_N_3 = Beta('b_relaxed_N_3',0,-100,100,0 )
b_artistic_N_3 = Beta('b_artistic_N_3',0,-100,100,0 )
b_sociable_N_3 = Beta('b_sociable_N_3',0,-100,100,0 )
b_othersfault_N_3 = Beta('b_othersfault_N_3',0,-100,100,0 )
b_thoroughjob_N_3 = Beta('b_thoroughjob_N_3',0,-100,100,0 )
b_easynervous_N_3 = Beta('b_easynervous_N_3',0,-100,100,0 )
b_activeimag_N_3 = Beta('b_activeimag_N_3',0,-100,100,0 )



ASC_Ind_1_N_3 = Beta('ASC_Ind_1_N_3',0,-100,100,1 )

alfa_LV_I1_N_3 = Beta('alfa_LV_I1_N_3',1,-100,100,1 )

sig_Ind_1_N_3 = Beta('sig_Ind_1_N_3',-0.508863,-100,100,0)

ASC_Ind_2_N_3 = Beta('ASC_Ind_2_N_3',0.733218,-100,100,0 )

alfa_LV_I2_N_3 = Beta('alfa_LV_I2_N_3',0.838539,-100,100,0 )

sig_Ind_2_N_3 = Beta('sig_Ind_2_N_3',-0.289028,-100,100,0 )


omega_N_3 =  bioDraws('omega_N_3')

personality_qua_N =  b_othersfault_N_3 * othersfault

latent_qua_N = LV_const_N_3 + omega_N_3 * exp(lv_sigma_N_3) + LV_male_N_3 * male  + LV_below50y_N_3 * below50y \
+ personality_qua_N



#Indicators


Ind_1_N_3 			= Q151_10
t_Ind_1_N_3 		= (Ind_1_N_3 - ASC_Ind_1_N_3 - alfa_LV_I1_N_3 * latent_qua_N) / exp(sig_Ind_1_N_3)
f_Ind_1_N_3 		= bioNormalPdf(t_Ind_1_N_3) / exp(sig_Ind_1_N_3)
#
Ind_2_N_3 			= Q151_11
t_Ind_2_N_3 		= (Ind_2_N_3 - ASC_Ind_2_N_3 - alfa_LV_I2_N_3 * latent_qua_N) / exp(sig_Ind_2_N_3)
f_Ind_2_N_3 		= bioNormalPdf(t_Ind_2_N_3) / exp(sig_Ind_2_N_3)


################Latent Shanghai###########


b_latent_afr_S = Beta('b_latent_afr_S',0.3352,-100,100,0 )

LV_const_S = Beta('LV_const_S',3.98582,-100,100,0 )
lv_sigma_S = Beta('lv_sigma_S',2.123,-100,100,0)

LV_above50y_S = Beta('LV_above50y_S',0.398999,-100,100,0 )
LV_male_S = Beta('LV_male_S',0.06838,-100,100,0 )
LV_self_empl_S = Beta('LV_self_empl_S',0.06838,-100,100,0 )
LV_high_edu_S = Beta('LV_high_edu_S',0.06838,-100,100,0 )
LV_income_high_S = Beta('LV_income_high_S',0.06838,-100,100,0 )
LV_income_low_S =  Beta('LV_income_low_S',0.06838,-100,100,0 )
LV_purp_pers_S =  Beta('LV_purp_pers_S',0.06838,-100,100,0 )
LV_below50y_S =  Beta('LV_below50y_S',0.06838,-100,100,0 )


b_reserved_S_1 = Beta('b_reserved_S_1',0,-100,100,0 )
b_trusting_S_1 = Beta('b_trusting_S_1',0,-100,100,0 )
b_lazy_S_1 = Beta('b_lazy_S_1',0,-100,100,0 )
b_relaxed_S_1 = Beta('b_relaxed_S_1',0,-100,100,0 )
b_artistic_S_1 = Beta('b_artistic_S_1',0,-100,100,0 )
b_sociable_S_1 = Beta('b_sociable_S_1',0,-100,100,0 )
b_othersfault_S_1 = Beta('b_othersfault_S_1',0,-100,100,0 )
b_thoroughjob_S_1 = Beta('b_thoroughjob_S_1',0,-100,100,0 )
b_easynervous_S_1 = Beta('b_easynervous_S_1',0,-100,100,0 )
b_activeimag_S_1 = Beta('b_activeimag_S_1',0,-100,100,0 )



ASC_Ind_1_S = Beta('ASC_Ind_1_S',0,-100,100,1 )

alfa_LV_I1_S = Beta('alfa_LV_I1_S',1,-100,100,1 )

sig_Ind_1_S = Beta('sig_Ind_1_S',-0.508863,-100,100,0)

ASC_Ind_2_S = Beta('ASC_Ind_2_S',0.733218,-100,100,0 )

alfa_LV_I2_S = Beta('alfa_LV_I2_S',0.838539,-100,100,0 )

sig_Ind_2_S = Beta('sig_Ind_2_S',-0.289028,-100,100,0 )

ASC_Ind_3_S = Beta('ASC_Ind_3_S',0.330353,-100,100,0 )

alfa_LV_I3_S = Beta('alfa_LV_I3_S',0.880481,-100,100,0 )

sig_Ind_3_S = Beta('sig_Ind_3_S',-0.206661,-100,100,0 )

ASC_Ind_4_S = Beta('ASC_Ind_4_S',0.341769,-100,100,0)

alfa_LV_I4_S = Beta('alfa_LV_I4_S',0.93511,-100,100,0)

sig_Ind_4_S = Beta('sig_Ind_4_S',-0.128357,-100,100,0)

ASC_Ind_5_S = Beta('ASC_Ind_5_S',0.341769,-100,100,0)

alfa_LV_I5_S = Beta('alfa_LV_I5_S',0.93511,-100,100,0)

sig_Ind_5_S = Beta('sig_Ind_5_S',-0.128357,-100,100,0)

ASC_Ind_6_S = Beta('ASC_Ind_6_L',0.341769,-100,100,0)

alfa_LV_I6_S = Beta('alfa_LV_I6_S',0.93511,-100,100,0)

sig_Ind_6_S = Beta('sig_Ind_6_S',-0.128357,-100,100,0)

omega_S =  bioDraws('omega_S')


personality_afr_S =  b_othersfault_S_1 * othersfault

latent_afr_S = LV_const_S + omega_S * exp(lv_sigma_S) + LV_male_S * male  + LV_below50y_S * below50y \
+ personality_afr_S



#Indicators


Ind_1_S 			= Q151_1
t_Ind_1_S 		= (Ind_1_S - ASC_Ind_1_S - alfa_LV_I1_S * latent_afr_S) / exp(sig_Ind_1_S)
f_Ind_1_S 		= bioNormalPdf(t_Ind_1_S) / exp(sig_Ind_1_S)
#
Ind_2_S 			= Q151_2
t_Ind_2_S 		= (Ind_2_S - ASC_Ind_2_S - alfa_LV_I2_S * latent_afr_S) / exp(sig_Ind_2_S)
f_Ind_2_S 		= bioNormalPdf(t_Ind_2_S) / exp(sig_Ind_2_S)


Ind_3_S 			= Q151_3
t_Ind_3_S 		= (Ind_3_S - ASC_Ind_3_S - alfa_LV_I3_S * latent_afr_S) / exp(sig_Ind_3_S)
f_Ind_3_S 		= bioNormalPdf(t_Ind_3_S) / exp(sig_Ind_3_S)

Ind_4_S 			= Q151_5
t_Ind_4_S 		= (Ind_4_S - ASC_Ind_4_S - alfa_LV_I4_S * latent_afr_S) / exp(sig_Ind_4_S)
f_Ind_4_S 		= bioNormalPdf(t_Ind_4_S) / exp(sig_Ind_4_S)

Ind_5_S 			= Q151_6
t_Ind_5_S 		= (Ind_5_S - ASC_Ind_5_S - alfa_LV_I5_S * latent_afr_S) / exp(sig_Ind_5_S)
f_Ind_5_S 		= bioNormalPdf(t_Ind_5_S) / exp(sig_Ind_5_S)


##Latent 2 SH###########

b_latent_saf_S = Beta('b_latent_saf_S_2',0.3352,-100,100,0 )

LV_const_S_2 = Beta('LV_const_S_2',3.98582,-100,100,0 )
lv_sigma_S_2 = Beta('lv_sigma_S_2',2.123,-100,100,0)

LV_above50y_S_2 = Beta('LV_above50y_S_2',0.398999,-100,100,0 )
LV_male_S_2 = Beta('LV_male_S_2',0.06838,-100,100,0 )
LV_self_empl_S_2 = Beta('LV_self_empl_S_2',0.06838,-100,100,0 )
LV_high_edu_S_2 = Beta('LV_high_edu_S_2',0.06838,-100,100,0 )
LV_income_high_S_2 = Beta('LV_income_high_S_2',0.06838,-100,100,0 )
LV_income_low_S_2 =  Beta('LV_income_low_S_2',0.06838,-100,100,0 )
LV_purp_pers_S_2 =  Beta('LV_purp_pers_S_2',0.06838,-100,100,0 )
LV_below50y_S_2 =  Beta('LV_below50y_S_2',0.06838,-100,100,0 )


b_reserved_S_2 = Beta('b_reserved_S_2',0,-100,100,0 )
b_trusting_S_2 = Beta('b_trusting_S_2',0,-100,100,0 )
b_lazy_S_2 = Beta('b_lazy_S_2',0,-100,100,0 )
b_relaxed_S_2 = Beta('b_relaxed_S_2',0,-100,100,0 )
b_artistic_S_2 = Beta('b_artistic_S_2',0,-100,100,0 )
b_sociable_S_2 = Beta('b_sociable_S_2',0,-100,100,0 )
b_othersfault_S_2 = Beta('b_othersfault_S_2',0,-100,100,0 )
b_thoroughjob_S_2 = Beta('b_thoroughjob_S_2',0,-100,100,0 )
b_easynervous_S_2 = Beta('b_easynervous_S_2',0,-100,100,0 )
b_activeimag_S_2 = Beta('b_activeimag_S_2',0,-100,100,0 )

ASC_Ind_1_S_2 = Beta('ASC_Ind_1_S_2',0,-100,100,1 )

alfa_LV_I1_S_2 = Beta('alfa_LV_I1_S_2',1,-100,100,1 )

sig_Ind_1_S_2 = Beta('sig_Ind_1_S_2',-0.508863,-100,100,0)

ASC_Ind_2_S_2 = Beta('ASC_Ind_2_S_2',0.733218,-100,100,0 )

alfa_LV_I2_S_2 = Beta('alfa_LV_I2_S_2',0.838539,-100,100,0 )

sig_Ind_2_S_2 = Beta('sig_Ind_2_S_2',-0.289028,-100,100,0 )

ASC_Ind_3_S_2 = Beta('ASC_Ind_3_S_2',0.330353,-100,100,0 )

alfa_LV_I3_S_2 = Beta('alfa_LV_I3_S_2',0.880481,-100,100,0 )

sig_Ind_3_S_2 = Beta('sig_Ind_3_S_2',-0.206661,-100,100,0 )



omega_S_2 =  bioDraws('omega_S_2')

personality_saf_S =  b_othersfault_S_2 * othersfault

latent_saf_S = LV_const_S_2 + omega_S_2 * exp(lv_sigma_S_2) + LV_male_S_2 * male  + LV_below50y_S_2 * below50y \
+ personality_saf_S



#Indicators


Ind_1_S_2 			= Q151_7
t_Ind_1_S_2 		= (Ind_1_S_2 - ASC_Ind_1_S_2 - alfa_LV_I1_S_2 * latent_saf_S) / exp(sig_Ind_1_S_2)
f_Ind_1_S_2 		= bioNormalPdf(t_Ind_1_S_2) / exp(sig_Ind_1_S_2)
#
Ind_2_S_2 			= Q151_8
t_Ind_2_S_2 		= (Ind_2_S_2 - ASC_Ind_2_S_2 - alfa_LV_I2_S_2 * latent_saf_S) / exp(sig_Ind_2_S_2)
f_Ind_2_S_2 		= bioNormalPdf(t_Ind_2_S_2) / exp(sig_Ind_2_S_2)


Ind_3_S_2 			= Q151_9
t_Ind_3_S_2 		= (Ind_3_S_2 - ASC_Ind_3_S_2 - alfa_LV_I3_S_2 * latent_saf_S) / exp(sig_Ind_3_S_2)
f_Ind_3_S_2 		= bioNormalPdf(t_Ind_3_S_2) / exp(sig_Ind_3_S_2)


#Latent 3 SH###########

b_latent_qua_S = Beta('b_latent_qua_S',0.3352,-100,100,0 )

LV_const_S_3 = Beta('LV_const_S_3',3.98582,-100,100,0 )
lv_sigma_S_3 = Beta('lv_sigma_S_3',2.123,-100,100,0)

LV_above50y_S_3 = Beta('LV_above50y_S_3',0.398999,-100,100,0 )
LV_male_S_3 = Beta('LV_male_S_3',0.06838,-100,100,0 )
LV_self_empl_S_3 = Beta('LV_self_empl_S_3',0.06838,-100,100,0 )
LV_high_edu_S_3 = Beta('LV_high_edu_S_3',0.06838,-100,100,0 )
LV_income_high_S_3 = Beta('LV_income_high_S_3',0.06838,-100,100,0 )
LV_income_low_S_3 =  Beta('LV_income_low_S_3',0.06838,-100,100,0 )
LV_purp_pers_S_3 =  Beta('LV_purp_pers_S_3',0.06838,-100,100,0 )
LV_below50y_S_3 =  Beta('LV_below50y_S_3',0.06838,-100,100,0 )

b_reserved_S_3 = Beta('b_reserved_S_3',0,-100,100,0 )
b_trusting_S_3 = Beta('b_trusting_S_3',0,-100,100,0 )
b_lazy_S_3 = Beta('b_lazy_S_3',0,-100,100,0 )
b_relaxed_S_3 = Beta('b_relaxed_S_3',0,-100,100,0 )
b_artistic_S_3 = Beta('b_artistic_S_3',0,-100,100,0 )
b_sociable_S_3 = Beta('b_sociable_S_3',0,-100,100,0 )
b_othersfault_S_3 = Beta('b_othersfault_S_3',0,-100,100,0 )
b_thoroughjob_S_3 = Beta('b_thoroughjob_S_3',0,-100,100,0 )
b_easynervous_S_3 = Beta('b_easynervous_S_3',0,-100,100,0 )
b_activeimag_S_3 = Beta('b_activeimag_S_3',0,-100,100,0 )

ASC_Ind_1_S_3 = Beta('ASC_Ind_1_S_3',0,-100,100,1 )

alfa_LV_I1_S_3 = Beta('alfa_LV_I1_S_3',1,-100,100,1 )

sig_Ind_1_S_3 = Beta('sig_Ind_1_S_3',-0.508863,-100,100,0)

ASC_Ind_2_S_3 = Beta('ASC_Ind_2_S_3',0.733218,-100,100,0 )

alfa_LV_I2_S_3 = Beta('alfa_LV_I2_S_3',0.838539,-100,100,0 )

sig_Ind_2_S_3 = Beta('sig_Ind_2_S_3',-0.289028,-100,100,0 )


omega_S_3 =  bioDraws('omega_S_3')

personality_qua_S =  b_trusting_S_3 * trusting + b_thoroughjob_S_3 * thoroughjob

latent_qua_S = LV_const_S_3 + omega_S_3 * exp(lv_sigma_S_3) + LV_male_S_3 * male  + LV_below50y_S_3 * below50y \
+ personality_qua_S



#Indicators


Ind_1_S_3 			= Q151_10
t_Ind_1_S_3 		= (Ind_1_S_3 - ASC_Ind_1_S_3 - alfa_LV_I1_S_3 * latent_qua_S) / exp(sig_Ind_1_S_3)
f_Ind_1_S_3 		= bioNormalPdf(t_Ind_1_S_3) / exp(sig_Ind_1_S_3)

Ind_2_S_3 			= Q151_11
t_Ind_2_S_3 		= (Ind_2_S_3 - ASC_Ind_2_S_3 - alfa_LV_I2_S_3 * latent_qua_S) / exp(sig_Ind_2_S_3)
f_Ind_2_S_3 		= bioNormalPdf(t_Ind_2_S_3) / exp(sig_Ind_2_S_3)


################Latent Sao###########


b_latent_afr_P = Beta('b_latent_afr_P',0.3352,-100,100,0 )

LV_const_P = Beta('LV_const_P',3.98582,-100,100,0 )
lv_sigma_P = Beta('lv_sigma_P',2.123,-100,100,0)

LV_above50y_P = Beta('LV_above50y_P',0.398999,-100,100,0 )
LV_male_P = Beta('LV_male_P',0.06838,-100,100,0 )
LV_self_empl_P = Beta('LV_self_empl_P',0.06838,-100,100,0 )
LV_high_edu_P = Beta('LV_high_edu_P',0.06838,-100,100,0 )
LV_income_high_P = Beta('LV_income_high_P',0.06838,-100,100,0 )
LV_income_low_P =  Beta('LV_income_low_P',0.06838,-100,100,0 )
LV_purp_pers_P =  Beta('LV_purp_pers_P',0.06838,-100,100,0 )
LV_below50y_P =  Beta('LV_below50y_P',0.06838,-100,100,0 )

b_reserved_P_1 = Beta('b_reserved_P_1',0,-100,100,0 )
b_trusting_P_1 = Beta('b_trusting_P_1',0,-100,100,0 )
b_lazy_P_1 = Beta('b_lazy_P_1',0,-100,100,0 )
b_relaxed_P_1 = Beta('b_relaxed_P_1',0,-100,100,0 )
b_artistic_P_1 = Beta('b_artistic_P_1',0,-100,100,0 )
b_Pociable_P_1 = Beta('b_Pociable_P_1',0,-100,100,0 )
b_othersfault_P_1 = Beta('b_othersfault_P_1',0,-100,100,0 )
b_thoroughjob_P_1 = Beta('b_thoroughjob_P_1',0,-100,100,0 )
b_easynervous_P_1 = Beta('b_easynervous_P_1',0,-100,100,0 )
b_activeimag_P_1 = Beta('b_activeimag_P_1',0,-100,100,0 )


ASC_Ind_1_P = Beta('ASC_Ind_1_P',0,-100,100,1 )

alfa_LV_I1_P = Beta('alfa_LV_I1_P',1,-100,100,1 )

sig_Ind_1_P = Beta('sig_Ind_1_P',-0.508863,-100,100,0)

ASC_Ind_2_P = Beta('ASC_Ind_2_P',0.733218,-100,100,0 )

alfa_LV_I2_P = Beta('alfa_LV_I2_P',0.838539,-100,100,0 )

sig_Ind_2_P = Beta('sig_Ind_2_P',-0.289028,-100,100,0 )

ASC_Ind_3_P = Beta('ASC_Ind_3_P',0.330353,-100,100,0 )

alfa_LV_I3_P = Beta('alfa_LV_I3_P',0.880481,-100,100,0 )

sig_Ind_3_P = Beta('sig_Ind_3_P',-0.206661,-100,100,0 )

ASC_Ind_4_P = Beta('ASC_Ind_4_P',0.341769,-100,100,0)

alfa_LV_I4_P = Beta('alfa_LV_I4_P',0.93511,-100,100,0)

sig_Ind_4_P = Beta('sig_Ind_4_P',-0.128357,-100,100,0)

ASC_Ind_5_P = Beta('ASC_Ind_5_P',0.341769,-100,100,0)

alfa_LV_I5_P = Beta('alfa_LV_I5_P',0.93511,-100,100,0)

sig_Ind_5_P = Beta('sig_Ind_5_P',-0.128357,-100,100,0)

ASC_Ind_6_P = Beta('ASC_Ind_6_L',0.341769,-100,100,0)

alfa_LV_I6_P = Beta('alfa_LV_I6_P',0.93511,-100,100,0)

sig_Ind_6_P = Beta('sig_Ind_6_P',-0.128357,-100,100,0)

omega_P =  bioDraws('omega_P')


personality_afr_P =  b_reserved_P_1 * reserved + b_thoroughjob_P_1 * thoroughjob

latent_afr_P = LV_const_P + omega_P * exp(lv_sigma_P) + LV_male_P * male   \
+ personality_afr_P



#Indicators


Ind_1_P 			= Q151_1
t_Ind_1_P 		= (Ind_1_P - ASC_Ind_1_P - alfa_LV_I1_P * latent_afr_P) / exp(sig_Ind_1_P)
f_Ind_1_P 		= bioNormalPdf(t_Ind_1_P) / exp(sig_Ind_1_P)
#
Ind_2_P 			= Q151_2
t_Ind_2_P 		= (Ind_2_P - ASC_Ind_2_P - alfa_LV_I2_P * latent_afr_P) / exp(sig_Ind_2_P)
f_Ind_2_P 		= bioNormalPdf(t_Ind_2_P) / exp(sig_Ind_2_P)


Ind_3_P 			= Q151_3
t_Ind_3_P 		= (Ind_3_P - ASC_Ind_3_P - alfa_LV_I3_P * latent_afr_P) / exp(sig_Ind_3_P)
f_Ind_3_P 		= bioNormalPdf(t_Ind_3_P) / exp(sig_Ind_3_P)

Ind_4_P 			= Q151_5
t_Ind_4_P 		= (Ind_4_P - ASC_Ind_4_P - alfa_LV_I4_P * latent_afr_P) / exp(sig_Ind_4_P)
f_Ind_4_P 		= bioNormalPdf(t_Ind_4_P) / exp(sig_Ind_4_P)

Ind_5_P 			= Q151_6
t_Ind_5_P 		= (Ind_5_P - ASC_Ind_5_P - alfa_LV_I5_P * latent_afr_P) / exp(sig_Ind_5_P)
f_Ind_5_P 		= bioNormalPdf(t_Ind_5_P) / exp(sig_Ind_5_P)


##Latent 2 SP###########

b_latent_saf_P = Beta('b_latent_saf_P_2',0.3352,-100,100,0 )

LV_const_P_2 = Beta('LV_const_P_2',3.98582,-100,100,0 )
lv_sigma_P_2 = Beta('lv_sigma_P_2',2.123,-100,100,0)

LV_above50y_P_2 = Beta('LV_above50y_P_2',0.398999,-100,100,0 )
LV_male_P_2 = Beta('LV_male_P_2',0.06838,-100,100,0 )
LV_self_empl_P_2 = Beta('LV_self_empl_P_2',0.06838,-100,100,0 )
LV_high_edu_P_2 = Beta('LV_high_edu_P_2',0.06838,-100,100,0 )
LV_income_high_P_2 = Beta('LV_income_high_P_2',0.06838,-100,100,0 )
LV_income_low_P_2 =  Beta('LV_income_low_P_2',0.06838,-100,100,0 )
LV_purp_pers_P_2 =  Beta('LV_purp_pers_P_2',0.06838,-100,100,0 )
LV_below50y_P_2 =  Beta('LV_below50y_P_2',0.06838,-100,100,0 )


b_reserved_P_2 = Beta('b_reserved_P_2',0,-100,100,0 )
b_trusting_P_2 = Beta('b_trusting_P_2',0,-100,100,0 )
b_lazy_P_2 = Beta('b_lazy_P_2',0,-100,100,0 )
b_relaxed_P_2 = Beta('b_relaxed_P_2',0,-100,100,0 )
b_artistic_P_2 = Beta('b_artistic_P_2',0,-100,100,0 )
b_Pociable_P_2 = Beta('b_Pociable_P_2',0,-100,100,0 )
b_othersfault_P_2 = Beta('b_othersfault_P_2',0,-100,100,0 )
b_thoroughjob_P_2 = Beta('b_thoroughjob_P_2',0,-100,100,0 )
b_easynervous_P_2 = Beta('b_easynervous_P_2',0,-100,100,0 )
b_activeimag_P_2 = Beta('b_activeimag_P_2',0,-100,100,0 )


ASC_Ind_1_P_2 = Beta('ASC_Ind_1_P_2',0,-100,100,1 )

alfa_LV_I1_P_2 = Beta('alfa_LV_I1_P_2',1,-100,100,1 )

sig_Ind_1_P_2 = Beta('sig_Ind_1_P_2',-0.508863,-100,100,0)

ASC_Ind_2_P_2 = Beta('ASC_Ind_2_P_2',0.733218,-100,100,0 )

alfa_LV_I2_P_2 = Beta('alfa_LV_I2_P_2',0.838539,-100,100,0 )

sig_Ind_2_P_2 = Beta('sig_Ind_2_P_2',-0.289028,-100,100,0 )

ASC_Ind_3_P_2 = Beta('ASC_Ind_3_P_2',0.330353,-100,100,0 )

alfa_LV_I3_P_2 = Beta('alfa_LV_I3_P_2',0.880481,-100,100,0 )

sig_Ind_3_P_2 = Beta('sig_Ind_3_P_2',-0.206661,-100,100,0 )



omega_P_2 =  bioDraws('omega_P_2')


personality_saf_P =  b_othersfault_P_2 * othersfault


latent_saf_P = LV_const_P_2 + omega_P_2 * exp(lv_sigma_P_2) + LV_male_P_2 * male  + LV_below50y_P_2 * below50y \
+ personality_saf_P



#Indicators


Ind_1_P_2 			= Q151_7
t_Ind_1_P_2 		= (Ind_1_P_2 - ASC_Ind_1_P_2 - alfa_LV_I1_P_2 * latent_saf_P) / exp(sig_Ind_1_P_2)
f_Ind_1_P_2 		= bioNormalPdf(t_Ind_1_P_2) / exp(sig_Ind_1_P_2)
#
Ind_2_P_2 			= Q151_8
t_Ind_2_P_2 		= (Ind_2_P_2 - ASC_Ind_2_P_2 - alfa_LV_I2_P_2 * latent_saf_P) / exp(sig_Ind_2_P_2)
f_Ind_2_P_2 		= bioNormalPdf(t_Ind_2_P_2) / exp(sig_Ind_2_P_2)


Ind_3_P_2 			= Q151_9
t_Ind_3_P_2 		= (Ind_3_P_2 - ASC_Ind_3_P_2 - alfa_LV_I3_P_2 * latent_saf_P) / exp(sig_Ind_3_P_2)
f_Ind_3_P_2 		= bioNormalPdf(t_Ind_3_P_2) / exp(sig_Ind_3_P_2)





#Latent 3 Sao###########

b_latent_qua_P = Beta('b_latent_qua_P',0.3352,-100,100,0 )

LV_const_P_3 = Beta('LV_const_P_3',3.98582,-100,100,0 )
lv_sigma_P_3 = Beta('lv_sigma_P_3',2.123,-100,100,0)

LV_above50y_P_3 = Beta('LV_above50y_P_3',0.398999,-100,100,0 )
LV_male_P_3 = Beta('LV_male_P_3',0.06838,-100,100,0 )
LV_self_empl_P_3 = Beta('LV_self_empl_P_3',0.06838,-100,100,0 )
LV_high_edu_P_3 = Beta('LV_high_edu_P_3',0.06838,-100,100,0 )
LV_income_high_P_3 = Beta('LV_income_high_P_3',0.06838,-100,100,0 )
LV_income_low_P_3 =  Beta('LV_income_low_P_3',0.06838,-100,100,0 )
LV_purp_pers_P_3 =  Beta('LV_purp_pers_P_3',0.06838,-100,100,0 )
LV_below50y_P_3 =  Beta('LV_below50y_P_3',0.06838,-100,100,0 )


b_reserved_P_3 = Beta('b_reserved_P_3',0,-100,100,0 )
b_trusting_P_3 = Beta('b_trusting_P_3',0,-100,100,0 )
b_lazy_P_3 = Beta('b_lazy_P_3',0,-100,100,0 )
b_relaxed_P_3 = Beta('b_relaxed_P_3',0,-100,100,0 )
b_artistic_P_3 = Beta('b_artistic_P_3',0,-100,100,0 )
b_Pociable_P_3 = Beta('b_Pociable_P_3',0,-100,100,0 )
b_othersfault_P_3 = Beta('b_othersfault_P_3',0,-100,100,0 )
b_thoroughjob_P_3 = Beta('b_thoroughjob_P_3',0,-100,100,0 )
b_easynervous_P_3 = Beta('b_easynervous_P_3',0,-100,100,0 )
b_activeimag_P_3 = Beta('b_activeimag_P_3',0,-100,100,0 )

ASC_Ind_1_P_3 = Beta('ASC_Ind_1_P_3',0,-100,100,1 )

alfa_LV_I1_P_3 = Beta('alfa_LV_I1_P_3',1,-100,100,1 )

sig_Ind_1_P_3 = Beta('sig_Ind_1_P_3',-0.508863,-100,100,0)

ASC_Ind_2_P_3 = Beta('ASC_Ind_2_P_3',0.733218,-100,100,0 )

alfa_LV_I2_P_3 = Beta('alfa_LV_I2_P_3',0.838539,-100,100,0 )

sig_Ind_2_P_3 = Beta('sig_Ind_2_P_3',-0.289028,-100,100,0 )



omega_P_3 =  bioDraws('omega_P_3')


personality_qua_P =  b_othersfault_P_3 * othersfault


latent_qua_P = LV_const_P_3 + omega_P_3 * exp(lv_sigma_P_3) + LV_male_P_3 * male  + LV_below50y_P_3 * below50y \
+ personality_qua_P



#Indicators


Ind_1_P_3 			= Q151_10
t_Ind_1_P_3 		= (Ind_1_P_3 - ASC_Ind_1_P_3 - alfa_LV_I1_P_3 * latent_qua_P) / exp(sig_Ind_1_P_3)
f_Ind_1_P_3 		= bioNormalPdf(t_Ind_1_P_3) / exp(sig_Ind_1_P_3)

Ind_2_P_3 			= Q151_11
t_Ind_2_P_3 		= (Ind_2_P_3 - ASC_Ind_2_P_3 - alfa_LV_I2_P_3 * latent_qua_P) / exp(sig_Ind_2_P_3)
f_Ind_2_P_3 		= bioNormalPdf(t_Ind_2_P_3) / exp(sig_Ind_2_P_3)




#Utility 

V1_L = ASC_iti_L  + ((SH_L_a + MH_L_a + LH_L_a + BeforeCov_pers    ) * purp_pers + (SH_L_a_bus + MH_L_a_bus + LH_L_a_bus + BeforeCov_bus + DuringCovid_bus + AfterCov_bus ) *   purp_bus_tot) +  iti_RND_L \
+ Socioeconomic  + b_latent_afr_L * latent_afr_L 

V2_L = ASC_iti_L  + ((SH_L_b + MH_L_b + LH_L_b + BeforeCov_pers    ) * purp_pers + (SH_L_b_bus + MH_L_b_bus + LH_L_b_bus + BeforeCov_bus + DuringCovid_bus + AfterCov_bus ) *   purp_bus_tot) +  iti_RND_L \
+ Socioeconomic  + b_latent_afr_L * latent_afr_L 

V3_L = 0



V1_N = ASC_iti_N  + ((SH_N_a + MH_N_a + LH_N_a + BeforeCov_pers    ) * purp_pers + (SH_N_a_bus + MH_N_a_bus + LH_N_a_bus + BeforeCov_bus + DuringCovid_bus + AfterCov_bus ) *   purp_bus_tot) +  iti_RND_N \
+ Socioeconomic  + b_latent_saf_N * latent_saf_N 

V2_N = ASC_iti_N  + ((SH_N_b + MH_N_b + LH_N_b + BeforeCov_pers    ) * purp_pers + (SH_N_b_bus + MH_N_b_bus + LH_N_b_bus + BeforeCov_bus + DuringCovid_bus + AfterCov_bus ) *   purp_bus_tot) +  iti_RND_N \
+ Socioeconomic  + b_latent_saf_N * latent_saf_N 

V3_N = 0



V1_S = ASC_iti_S  + ((SH_S_a + MH_S_a + LH_S_a + BeforeCov_pers    ) * purp_pers + (SH_S_a_bus + MH_S_a_bus + LH_S_a_bus  + BeforeCov_bus + DuringCovid_bus + AfterCov_bus ) *   purp_bus_tot) +  iti_RND_S \
+ Socioeconomic  +  b_latent_qua_S * latent_qua_S 

V2_S = ASC_iti_S  + ((SH_S_b + MH_S_b + LH_S_b + BeforeCov_pers    ) * purp_pers + (SH_S_b_bus + MH_S_b_bus + LH_S_b_bus  + BeforeCov_bus + DuringCovid_bus + AfterCov_bus ) *   purp_bus_tot)  +  iti_RND_S \
+ Socioeconomic   + b_latent_qua_S * latent_qua_S 

V3_S = 0




V1_P = ASC_iti_P  + ((SH_P_a + MH_P_a + LH_P_a + BeforeCov_pers    ) * purp_pers + (SH_P_a_bus + MH_P_a_bus + LH_P_a_bus + BeforeCov_bus + DuringCovid_bus + AfterCov_bus ) *   purp_bus_tot) +  iti_RND_P \
+ Socioeconomic + b_latent_afr_P * latent_afr_P 

V2_P = ASC_iti_P  + ((SH_P_b + MH_P_b + LH_P_b + BeforeCov_pers    ) * purp_pers + (SH_P_b_bus + MH_P_b_bus + LH_P_b_bus + BeforeCov_bus + DuringCovid_bus + AfterCov_bus ) *   purp_bus_tot) +  iti_RND_P  \
+ Socioeconomic  + b_latent_afr_P * latent_afr_P 

V3_P = 0





# Associate the availability conditions with the alternatives

itia_AV_L= one * London
itib_AV_L= one * London
NoTr_L= one * London

itia_AV_N= one * NewYork
itib_AV_N= one * NewYork
NoTr_N= one * NewYork

itia_AV_S= one * Shanghai
itib_AV_S= one * Shanghai
NoTr_S= one * Shanghai

itia_AV_P= one * SaoPaulo
itib_AV_P= one * SaoPaulo
NoTr_P= one * SaoPaulo


# Associate utility functions with the numbering of alternatives
V = {11: scale * V1_L,
     12: scale * V2_L,
     13: scale * V3_L, 
	 
	 21: scale * V1_N,
     22: scale * V2_N,
     23: scale * V3_N, 
     
     31: scale * V1_S,
     32: scale * V2_S,
     33: scale * V3_S, 
     
     41: scale * V1_P,
     42: scale * V2_P,
     43: scale * V3_P 

     }



av = {11: itia_AV_L,
      12: itib_AV_L,
      13: NoTr_L,
	  
	  21: itia_AV_N,
      22: itib_AV_N,
      23: NoTr_N,

      31: itia_AV_S,
      32: itib_AV_S,
      33: NoTr_S,

      41: itia_AV_P,
      42: itib_AV_P,
      43: NoTr_P

      }



# The choice model is a logit, with availability conditions
prob = bioLogit(V,av,Choice)


# Iterator on individuals, that is on groups of rows.
metaIterator('personIter','__dataFile__','panelObsIter','ID')

# For each item of personIter, iterates on the rows of the group.
rowIterator('panelObsIter','personIter')

#Conditional probability for the sequence of choices of an individual
condProbIndiv = Prod(prob,'panelObsIter')

measurementForIndividual1 = Sum((f_Ind_1_L  * f_Ind_2_L * f_Ind_3_L * f_Ind_4_L * f_Ind_5_L),'panelObsIter') / Sum(1.0,'panelObsIter')

measurementForIndividual4 = Sum((f_Ind_1_P  * f_Ind_2_P * f_Ind_3_P * f_Ind_4_P * f_Ind_5_P),'panelObsIter') / Sum(1.0,'panelObsIter')

measurementForIndividual2_2 = Sum((f_Ind_1_N_2  * f_Ind_2_N_2  * f_Ind_3_N_2),'panelObsIter') / Sum(1.0,'panelObsIter')

measurementForIndividual3_3 = Sum((f_Ind_1_S_3  * f_Ind_2_S_3 ),'panelObsIter') / Sum(1.0,'panelObsIter')


condLikelihoodOneObs = condProbIndiv * measurementForIndividual1   * measurementForIndividual4 \
                                     * measurementForIndividual3_3 * measurementForIndividual2_2

# Integration by 
probIndiv = MonteCarlo(condLikelihoodOneObs)


# Likelihood function
loglikelihood = Sum(log(probIndiv),'personIter')

BIOGEME_OBJECT.ESTIMATE = loglikelihood

# All observations verifying the following expression will not be
# considered for estimation
# The modeler here has developed the model only for work trips.
# Observations such that the dependent variable CHOICE is 0 are also removed.
exclude = ( Choice == -990 ) |  ((ID == 1331) & (Count == 3))

BIOGEME_OBJECT.EXCLUDE = exclude


# Statistics


nullLoglikelihood(av,'panelObsIter')
choiceSet = [11,12,13, 21,22,23, 31,32,33, 41,42,43]
cteLoglikelihood(choiceSet,Choice,'panelObsIter')
availabilityStatistics(av,'panelObsIter')


BIOGEME_OBJECT.PARAMETERS['NbrOfDraws'] = "500"
BIOGEME_OBJECT.PARAMETERS['RandomDistribution'] = "MLHS"
BIOGEME_OBJECT.PARAMETERS['numberOfThreads'] = "32"
BIOGEME_OBJECT.PARAMETERS['varCovarFromBHHH'] = "0"
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "CFSQP"
BIOGEME_OBJECT.PARAMETERS['checkDerivatives'] = "1"
BIOGEME_OBJECT.PARAMETERS['dumpDrawsOnFile'] = "0"

BIOGEME_OBJECT.DRAWS = {    'iti_RND_L'    : ('NORMAL' ,'ID'),
                            'omega_L'    : ('NORMAL' ,'ID'),  
                            'omega_P'    : ('NORMAL' ,'ID'),
                            'omega_N_2'    : ('NORMAL' ,'ID'),  
                            'omega_S_3'    : ('NORMAL' ,'ID'),  
                            'iti_RND_N'    : ('NORMAL' ,'ID'), 
                            'iti_RND_P'    : ('NORMAL' ,'ID'), 
                            'iti_RND_S'    : ('NORMAL' ,'ID')
                        }



