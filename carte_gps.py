import folium
import donnes

# # Creating a map
m = folium.Map((45.166672, 5.71667), zoom_start=12)

for i in range(len(donnes.coordennees)):
    # # Adding markers
    folium.Marker(
        location=[donnes.coordennees[i]],
        tooltip="Click me!",
        popup="Timberline Lodge",
        icon=folium.Icon(color='red',
                         prefix='fa', icon=f'{i}')
    ).add_to(m)
    m.save("index.html")

# lines
trail_coordinates = []


folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)
m.save("index.html")
