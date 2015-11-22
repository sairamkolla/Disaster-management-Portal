
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


       $scope.TestFillProfile = function(){
            console.log('inside login')
            var data = {
               OrganisationName : $scope.OrganisationName,
               OrganisationStrength : $scope.OrganisationStrength,
               OrganisationHead : $scope.OrganisationHead,
               latitude : $scope.latitude,
               longitude : $scope.longitude,
               Tags : $scope.Tags
            };
            console.log(data)
            $http.post('http://127.0.0.1:8000/data/testfillprofile/',data).then(function(response){
                console.log(response);
                if(response.hasOwnProperty('error')){
                    console.log(response.error);
                }
                if(parseInt(response.data.ok) == 1){
                  $window.location.href = '/orgs/home/';
                }
                else{
                    console.log('asdsadasddas');
                }
            },function(data){
                // on incorrect username and password
                console.log(response);
            });
        };
    }]);

