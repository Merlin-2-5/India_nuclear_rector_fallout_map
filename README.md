# India Nuclear Reactor Fallout Risk Map

A dynamic, interactive web application built with Dash and Folium that visualizes the emergency planning zones and theoretical fallout risks surrounding India's major nuclear power plants.

## 🌟 Features

- **Interactive Map Interface**: A full-screen, responsive map built with Folium, offering pan and zoom capabilities.
- **Nuclear Reactor Locations**: Pinpoints 7 major nuclear power plants across India (e.g., Tarapur, Kudankulam, Narora), clustered intelligently for readability at lower zoom levels.
- **Emergency Planning Zones (Concentric Circles)**: Visualizes 5 levels of fallout severity/emergency planning zones around each reactor:
  - 🔴 5 km: Exclusion Zone
  - 🟠 30 km: Evacuation Planning
  - 🟡 80 km: Relocation Consideration
  - 🔵 300 km: Food/Water Monitoring
  - 🟣 1000 km: Trace Detection Envelope
- **Toggleable Layers**: Users can easily filter and view specific fallout severity zones using a built-in interactive layer control panel.
- **Major Cities Overlay**: Highlights major metropolitan areas (New Delhi, Mumbai, Bengaluru, etc.) to assess population centers' proximity to potential fallout zones.
- **Geopolitical Borders**: Dynamically fetches and renders Indian state borders via GeoJSON for better geographical context.
- **Measurement Tool**: Built-in interactive tool to calculate straight-line distances and areas on the map.
- **Informative Legend**: A floating, stylized legend providing clear context for all map markers, zones, and colors.

## 🛠️ Technology Stack

- **[Dash (Plotly)](https://dash.plotly.com/)**: Serves the web framework and user interface.
- **[Folium](https://python-visualization.github.io/folium/)**: Handles the generation of the interactive Leaflet.js map.
- **Python 3**: The core language powering the backend logic.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed on your machine. You will also need the required Python libraries. You can install the core dependencies via pip:

```bash
pip install dash folium branca
```

### Running the Application

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the main application file:
```bash
python src/main.py
```
4. Open your web browser and navigate to `http://127.0.0.1:8050/`.

## 📜 License
This project is open-source. See the `LICENSE` file for details.