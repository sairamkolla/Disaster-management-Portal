
var app = angular.module('myapp', []).config(function($interpolateProvider,$httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller('myctrl', ['$scope', '$http', '$templateCache','$interval','$window',
    function($scope, $http, $templateCache,$interval,$window) {
        console.log("inside controller");

       $scope.TestFillCredentials = function(){
            console.log('inside login');
            var data = {
               username : $scope.username,
               password : $scope.password,
               password1 : $scope.password1
            };
            console.log(data)
            $http.post('http://127.0.0.1:8000/data/testfillcredentials/',data).then(function(response){
                console.log(response);
                if(response.hasOwnProperty('error')){
                    console.log(response.error);
                }
                if(response.ok == 1){
                    $window.location.href = '/orgs/home/';
                }
            },function(data){
                // on incorrect username and password
                console.log(response);
            });
        };
    }]);

