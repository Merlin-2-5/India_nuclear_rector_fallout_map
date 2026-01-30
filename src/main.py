import dash
from dash import dcc, html
import folium
from folium.plugins import MarkerCluster, MeasureControl
import urllib.request
import json
from branca.element import Element

# Sample data: List of nuclear reactors in India with their latitude and longitude
nuclear_reactors = [
    {"name": "Tarapur Nuclear Power Station", "latitude": 19.8400, "longitude": 72.7758},
    {"name": "Rawatbhata (Rajasthan) Nuclear Power Plant", "latitude": 24.9980, "longitude": 76.3060},
    {"name": "Madras (Kalpakkam) Nuclear Power Plant", "latitude": 12.7719, "longitude": 80.1822},
    {"name": "Kaiga Nuclear Power Plant", "latitude": 14.9167, "longitude": 74.5833},
    {"name": "Kudankulam Nuclear Power Plant", "latitude": 8.1636, "longitude": 77.7020},
    {"name": "Narora Atomic Power Station", "latitude": 28.1600, "longitude": 78.4900},
    {"name": "Kakrapar Nuclear Power Plant", "latitude": 21.8394, "longitude": 75.6400}
]

# Define radii, colors, and labels for the fallout zones
radii = [5, 30, 80, 300, 1000]
colors = ['#ff0000', '#ff7f00', '#ffd700', '#1f78b4', '#6a3d9a']
labels = ['5 km (exclusion zone)', '30 km (evacuation planning)',
          '80 km (relocation consideration)', '300 km (food/water monitoring)',
          '1000 km (trace detection envelope)']

def create_map_html():
    m = folium.Map(location=[20, 78], zoom_start=5)
    marker_cluster = MarkerCluster().add_to(m)

    # Prepare toggleable feature groups (one per radius/severity)
    feature_groups = {}
    for color, label in zip(colors, labels):
        fg = folium.FeatureGroup(name=label, show=True)
        feature_groups[label] = (fg, color)
    for fg, _ in feature_groups.values():
        m.add_child(fg)

    # Draw concentric circles for each reactor into appropriate feature groups
    for reactor in nuclear_reactors:
        lat, lon = reactor['latitude'], reactor['longitude']
        folium.Marker([lat, lon], popup=reactor['name'], tooltip=reactor['name']).add_to(marker_cluster)
        for r_km, label in zip(radii, labels):
            fg, color = feature_groups[label]
            folium.Circle(
                location=(lat, lon),
                radius=r_km * 1000,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.18,
                weight=2,
                popup=f"{reactor['name']} — {label}",
                tooltip=label
            ).add_to(fg)

    # Add major cities
    major_cities = [
        ("New Delhi", 28.6139, 77.2090),
        ("Mumbai", 19.0760, 72.8777),
        ("Kolkata", 22.5726, 88.3639),
        ("Chennai", 13.0827, 80.2707),
        ("Bengaluru", 12.9716, 77.5946),
        ("Hyderabad", 17.3850, 78.4867),
        ("Ahmedabad", 23.0225, 72.5714),
        ("Pune", 18.5204, 73.8567),
        ("Lucknow", 26.8467, 80.9462),
        ("Jaipur", 26.9124, 75.7873),
        ("Bhopal", 23.2599, 77.4126),
        ("Patna", 25.5941, 85.1376),
        ("Surat", 21.1702, 72.8311),
        ("Indore", 22.7196, 75.8577)
    ]
    for name, lat, lon in major_cities:
        folium.CircleMarker([lat, lon], radius=4, color='#000000', fill=True, fill_color='#000000', fill_opacity=0.9,
                           popup=name, tooltip=name).add_to(m)

    # Attempt to fetch and overlay India state borders (public GeoJSON)
    try:
        geojson_url = 'https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson'
        with urllib.request.urlopen(geojson_url, timeout=10) as resp:
            states_geo = json.load(resp)
        folium.GeoJson(states_geo, name='State borders', style_function=lambda f: {
            'fillOpacity': 0,
            'color': '#444444',
            'weight': 1
        }, control=False).add_to(m)
    except Exception:
        # If fetching fails, continue without borders
        pass

    # Add measure control (distance/area) as a scale helper
    m.add_child(MeasureControl(position='bottomleft', primary_length_unit='kilometers'))

    # Add LayerControl (top-left) so user can toggle zones by severity
    folium.LayerControl(collapsed=False, position='bottomright').add_to(m)

    # Add legend (HTML) at top-right with color swatches and instructions
    legend_html = '''
    <div style="position: fixed; top: 20px; right: 20px; width: 280px; z-index:9999; background-color:rgba(255,255,255,0.95); padding:15px; border-radius:8px; box-shadow:0 4px 12px rgba(0,0,0,0.15); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size:13px;">
    <h4 style="margin-top:0; margin-bottom:10px; font-size:15px;">Emergency Planning Zones</h4>
    <div style="margin-bottom:10px; color:#555;">Use the layer checkboxes to enable/disable zones.</div>
    ''' + ''.join([f'<div style="margin-bottom:4px;"><i style="background:{c};opacity:0.7;width:18px;height:12px;display:inline-block;margin-right:8px;border-radius:2px;"></i>{l}</div>' for c, l in zip(colors, labels)]) + '''
    <hr style="margin:12px 0; border:0; border-top:1px solid #eee;">
    <div><b>Markers:</b></div>
    <div style="margin-top:4px;"><span style="font-size:16px;">📍</span> Reactors (clustered)</div>
    <div style="margin-top:4px;"><span style="display:inline-block;width:8px;height:8px;background:black;border-radius:50%;margin-right:6px;margin-left:4px;"></span> Major Cities</div>
    </div>
    '''

    m.get_root().html.add_child(Element(legend_html))

    # Add title (HTML) at top-center
    title_html = '''
    <div style="position: fixed; top: 20px; left: 50%; transform: translateX(-50%); z-index:9999; background-color:rgba(255,255,255,0.9); padding:10px 20px; border-radius:50px; box-shadow:0 2px 5px rgba(0,0,0,0.3); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
        <h3 style="margin:0; font-size:18px; color:#333;">Nuclear Fallout Risk Map</h3>
    </div>
    '''
    m.get_root().html.add_child(Element(title_html))

    return m.get_root().render()

app = dash.Dash(__name__)
app.title = "Nuclear Fallout Risk Map"

app.layout = html.Div([
    html.Iframe(
        id='map',
        srcDoc=create_map_html(),
        style={'width': '100%', 'height': '100vh', 'border': 'none', 'margin': '0', 'padding': '0'}
    )
], style={'width': '100vw', 'height': '100vh', 'margin': '0', 'padding': '0', 'overflow': 'hidden'})

if __name__ == '__main__':
    app.run(debug=True)
