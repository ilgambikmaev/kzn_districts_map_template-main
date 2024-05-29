import pandas as pd
import numpy as np
from scipy.spatial import ConvexHull

def load_data(file_path):
    return pd.read_csv(file_path)

def compute_convex_hull(points):
    hull = ConvexHull(points)
    hull_points = points[hull.vertices]
    return hull_points

def generate_hulls(data):
    districts = data['district'].unique()
    hulls = {}
    
    for district in districts:
        district_points = data[data['district'] == district][['lat', 'lon']].values
        hull_points = compute_convex_hull(district_points)
        hulls[district] = hull_points
    
    return hulls

def save_hulls(hulls, output_file):
    hull_data = []
    
    for district, points in hulls.items():
        for point in points:
            hull_data.append({
                'lat': point[0],
                'lon': point[1],
                'district': district
            })
    
    hull_df = pd.DataFrame(hull_data)
    hull_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    data = load_data('c:/Users/Redmi/OneDrive/Desktop/АИСД/kzn_districts_map_template-main/points.csv')
    hulls = generate_hulls(data)
    save_hulls(hulls, 'hulls.csv')
