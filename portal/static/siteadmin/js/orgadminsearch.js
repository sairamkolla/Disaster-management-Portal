
var app = angular.module('myapp', []).config(function($interpolateProvider,$httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});


app.controller('myctrl', ['$scope', '$http', '$templateCache','$interval',
    function($scope, $http, $templateCache,$interval) {
        console.log("inside controller");

        $scope.getuserdetails = function(){
            $http.get('/data/GetUserDetails/').
                then(function(success){
                    $scope.userdetails = success.data;
                    console.log($scope.userdetails.username)
                },function(error){
                    console.log(error);
                });
        }
        $scope.init = function(){
            console.log('inside init');
        };

        $scope.SearchOrgs = function(i){
        console.log('in here test');
            if( $scope.orgsearchparameter != ''){
                if(i==1){
                    var data = {
                     keyword:$scope.orgsearchparameter,
                     tag:1
                    };
                }
                else{
                    var data = {
                     keyword:$scope.orgsearchparameter
                    };
                }
                $http.post('/data/getorglist/',data).
                then(function(success){

                    $scope.requiredorgs = success.data
                    $scope.orgsearchparameter='';


                },function(error){
                    console.log(error);
                });
            }
            else{
                $scope.requiredorgs = [];

            }

        };


    }]);



