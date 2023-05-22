# This program analyzes We-Truck-It package delivery information and
# generates truck purchase type recommendations for each of the
# We-Truck-It company U.S. Delivery regions.


#import the numpy library for random number generation and data analysis
import numpy as np


# store the number of packages delivered in the northeast and northwest
# in the variables ne_num and nw_num
ne_num = 60831
nw_num = 50629
se_num = 44000


# use numpy to determine the number of packages within the recommended
# ranges for the light, medium and heavy truck types
def Calc_Counts(packages):
    light_count  = np.count_nonzero((5 < packages) & (packages < 50))
    medium_count = np.count_nonzero((51 < packages) & (packages < 100))
    heavy_count  = np.count_nonzero((101 < packages) & (packages < 150))

    return light_count, medium_count, heavy_count


# Recommend the best truck purchase type for the specified Region
def Package_Analysis(packages:np.ndarray, region:str):
    light_count, medium_count, heavy_count = Calc_Counts(packages)
 
    # print the number of trucks within the recommended package delivery weight
    # ranges for light, medium and heavy trucks
 
    print ('\n')
    print (f'\t*** {region} truck purchase analysis ***')
    print ('')
    print (f'Number of {region} packages in the LIGHT truck weight range:')
    print (light_count)
 
    print (f'Number of {region} packages in the MEDIUM truck weight range:')
    print (medium_count)
 
    print (f'Number of {region} packages in the HEAVY truck weight range:')
    print (heavy_count)


    # Generate a truck purchase recommendation based on the most common package weight
 
    if   (light_count > medium_count) and (light_count > heavy_count):
        message = (f'The LIGHT truck is the best purchase for the {region} region')
    elif (medium_count > light_count) and (medium_count > heavy_count):
        message = (f'The MEDIUM truck is the best purchase for the {region} region')
    else:
        message = (f'The HEAVY truck is the best purchase for the {region} region')
 
    print ('\n'+message)


def Region_Analysis(min_pkg_weight:float, max_pkg_weight:float, package_count:int, region:str):
 
    # Recommend the best truck purchase type for the Northeast Region
     
    # use the numpy random number function to simulate
    # package weights for the Northeast
 
    northeast_packages = np.random.uniform(low=min_pkg_weight, high=max_pkg_weight, size=(ne_num))
    
    Package_Analysis(northeast_packages, region)


Region_Analysis(5.0, 150.0, ne_num, "Northeast")
Region_Analysis(5.0, 150.0, nw_num, "Northwest")
Region_Analysis(5.0, 150.0, se_num, "Southeast")