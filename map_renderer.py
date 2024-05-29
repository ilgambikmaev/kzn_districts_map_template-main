import pandas as pd
import matplotlib.pyplot as plt

def load_hull_data(file_path):
    return pd.read_csv(file_path)

def render_map(hull_data):
    districts = hull_data['district'].unique()
    
    plt.figure(figsize=(10, 8))
    
    for district in districts:
        district_hull = hull_data[hull_data['district'] == district]
        plt.plot(district_hull['lon'], district_hull['lat'], label=district)
    
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.title('Districts of Kazan with Convex Hulls')
    plt.show()

if __name__ == "__main__":
    hull_data = load_hull_data('hulls.csv')
    render_map(hull_data)
