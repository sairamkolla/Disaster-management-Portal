
var app = angular.module('myapp', []).config(function($interpolateProvider,$httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller('myctrl', ['$scope', '$http', '$templateCache','$interval','$window',
    function($scope, $http, $templateCache,$interval,$window) {
        console.log("inside controller");

        var mapOptions = {
            zoom: 15,
            center: new google.maps.LatLng(17.447693983462845, 78.35050821129698),
            mapTypeId: google.maps.MapTypeId.TERRAIN
        };


        $scope.map = new google.maps.Map(document.getElementById('map'), mapOptions);
            $scope.map.addListener('click', function(e) {
                $scope.$apply(function(){
                    $scope.latitude = e.latLng.lat();
                    $scope.longitude = e.latLng.lng();
                });

         console.log(e.latLng.lat());
         console.log(e.latLng.lng());
         console.log($scope.latitude);
         console.log($scope.longitude);
  	    });



    }]);

