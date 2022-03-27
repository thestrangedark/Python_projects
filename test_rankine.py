from Rankine import rankine

def main():
    '''
    A test program for rankine power cycles.
    R1 is a rankine cycle object that is instantiated for turbine inlet of saturated vapor.
    R2 is a rankine cycle object that is instantiated for turbine inlet of superheated vapor.
    :return: none
    '''
    R1=rankine(p_high=#$JES MISSING CODE$, p_low=#$JES MISSING CODE$, name='Rankine cycle - saturated steam inlet')
    R1.calc_efficiency()

    R2=rankine(p_high=#$JES MISSING CODE$, p_low=#$JES MISSING CODE$, t_high=#$JES MISSING CODE$, name='Rankine cycle - superheated steam inlet')
    R2.calc_efficiency()

    R1.print_summary()
    R2.print_summary()

if __name__=="__main__":
    main()