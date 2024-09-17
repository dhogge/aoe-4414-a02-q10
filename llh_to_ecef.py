# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Converts lattiude, longitude, height above ellipsoid to 3d vector 
# Parameters:
#  lat_deg:lattitude in degrees
#  lon_deg: longitutde degree
#  hae_km: height above ellipsoid in km
#  ...
# Output:
#  x, y, z
#
# Written by Dylan Hogge
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math # math module

# Constants
R_E_KM = 6378.1363
E_E = 0.081819221456

# Helper function
def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0 - ecc**2.0 * math.sin(lat_rad)**2.0)

# Initialize script arguments
lat_deg = float('nan')
lon_deg = float('nan')
hae_km = 0.0

# Parse script arguments
if len(sys.argv) == 4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
else:
    print('Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km')
    exit()

# write script below this line
lat_rad = lat_deg * math.pi / 180.0
lon_rad = lon_deg * math.pi / 180.0
denom = calc_denom(E_E, lat_rad)
C_E = R_E_KM / denom
S_E = R_E_KM * (1 - E_E**2) / denom

r_x_km = (C_E + hae_km) * math.cos(lat_rad) * math.cos(lon_rad)
r_y_km = (C_E + hae_km) * math.cos(lat_rad) * math.sin(lon_rad)
r_z_km = (S_E + hae_km) * math.sin(lat_rad)

print(round(r_x_km, 6))
print(round(r_y_km, 6))
print(round(r_z_km, 6))

