function showLocation() {
    var lat = parseFloat(document.getElementById('latitude').value);
    var long = parseFloat(document.getElementById('longitude').value);

    if (isNaN(lat) || isNaN(long)) {
        alert("Please enter valid coordinates!");
        return;
    }

    if (marker) {
        map.removeLayer(marker);
    }

    if (circle) {
        map.removeLayer(circle);
    }

    marker = L.marker([lat, long]);
    circle = L.circle([lat, long], { radius: 100 }).addTo(map); // Default radius for entered coordinates

    var featureGroup = L.featureGroup([marker, circle]).addTo(map);

    map.fitBounds(featureGroup.getBounds());

    console.log("Entered coordinate is: Lat: " + lat + " Long: " + long);
}
