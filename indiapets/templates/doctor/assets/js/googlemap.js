/////////////////* GOOGLE MAP */////////////////////////

function googlemap() {
    "use strict";
    google.maps.Map.prototype.setCenterWithOffset= function(latlng, offsetX, offsetY) {
    var map = this;
    var ov = new google.maps.OverlayView();
    ov.onAdd = function() {
        var proj = this.getProjection();
        var aPoint = proj.fromLatLngToContainerPixel(latlng);
        aPoint.x = aPoint.x+offsetX;
        aPoint.y = aPoint.y+offsetY;
        map.setCenter(proj.fromContainerPixelToLatLng(aPoint));
    }; 
    ov.draw = function() {}; 
    ov.setMap(this); 
};
    var latlng = new google.maps.LatLng(40.714353, -74.005973);
    
    var stylez = [
    {
      featureType: "all",
      elementType: "all",
      stylers: [
        { saturation: -100 }
      ]
    }
];

    var myMapOptions = {
        zoom: 17,
        scrollwheel: false,
        disableDefaultUI: true,
        mapTypeControl: true,
        zoomControl: true,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.MEDIUM,
            position: google.maps.ControlPosition.LEFT_BOTTOM
        },
        center: latlng,
        mapTypeControlOptions: {
        mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'tehgrayz']
    }
    };
    
    var map = new google.maps.Map(document.getElementById("google-map"), myMapOptions);
    map.setCenterWithOffset(latlng, 0, 40);
    
    var mapType = new google.maps.StyledMapType(stylez, { name:"Grayscale" });    
    map.mapTypes.set('tehgrayz', mapType);
    map.setMapTypeId('tehgrayz');
    var image = 'assets/images/pin.png';

    var marker = new google.maps.Marker({
        draggable: false,
        animation: google.maps.Animation.DROP,
        icon: image,
        map: map,
        position: latlng
    });
}