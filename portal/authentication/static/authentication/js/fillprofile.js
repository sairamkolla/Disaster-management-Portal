
var app = angular.module('myapp', []).config(function($interpolateProvider,$httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller('myctrl', ['$scope', '$http', '$templateCache','$interval','$window',
    function($scope, $http, $templateCache,$interval,$window) {
        console.log("inside controller");

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

