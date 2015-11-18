
var app = angular.module('myapp', []).config(function($interpolateProvider,$httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller('myctrl', ['$scope', '$http', '$templateCache','$interval','$window',
    function($scope, $http, $templateCache,$interval,$window) {
        console.log("inside controller");

         $scope.login = function(){
            console.log('inside login')
            var data = {
               username : $scope.username,
               password : $scope.password
            };
            console.log(data)
            $http.post('http://127.0.0.1:8000/accounts/login/',data).then(function(response){
                // on good username and password
                console.log(response);
                $window.location.href = '/orgs/home/';
            },function(data){
                // on incorrect username and password
                console.log(response);
            });
        };
       $scope.register = function(){
            console.log('inside login')
            var data = {
               OrganisationName : $scope.OrganisationName,
               password : $scope.password1,
               password1 : $scope.password2,
               username : $scope.username1,
               OrganisationStrength : $scope.OrganisationStrength,
               OrganisationHead : $scope.OrganisationHead,
               latitude : $scope.latitude,
               longitude : $scope.longitude,
               Tags : $scope.Tags
            };
            console.log(data)
            $http.post('http://127.0.0.1:8000/accounts/register/',data).then(function(response){
                // on good username and password
                console.log(response);
                //if(response.loggedin == 1){
                //    $window.location.href = '/orgs/home/';
                //}
            },function(data){
                // on incorrect username and password
                console.log(response);
            });
        };
    }]);

