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

- **[Folium](https://python-visualization.github.io/folium/)**: Generates the interactive Leaflet.js map.
- **Python 3**: The core language powering the map-building logic.

The app renders a single self-contained `nuclear_fallout_map.html` file and opens it in your browser — no web server to start or stop.

## 🚀 Getting Started

### Quick start (Windows)

Double-click **`run.bat`**. It installs the dependencies on first run, builds the map, and opens it in your default browser.

### Manual

Ensure Python 3 is installed, then:

```bash
pip install -r requirements.txt
python src/main.py
```

This writes `nuclear_fallout_map.html` to the project root and opens it. State borders are loaded from the bundled `src/india_state.geojson` (fetched once from the source if that file is ever missing), so the map works offline.

## 📜 License
This project is open-source. See the `LICENSE` file for details.