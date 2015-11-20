
var app = angular.module('myapp', []).config(function($interpolateProvider,$httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});


app.controller('myctrl', ['$scope', '$http', '$templateCache','$interval',
    function($scope, $http, $templateCache,$interval) {
        console.log("inside controller");

        $scope.init = function(){
            console.log('inside init');
            $scope.presentorg=0;
            $scope.view = 0;
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

        $scope.getaccepteddisasters = function(i){

            var data = {
                userid : i
            };
            $http.post('/data/GetAcceptedDisasters/',data).
            then(function(success){
                $scope.accepteddisasters = success.data;
                $scope.presentorg = i;
                $scope.view = 1;
            },function(error){
                console.log(error);
            });

        };

        $scope.notgetaccepteddisasters = function(i){

            var data = {
                userid : i
            };
            $http.post('/data/NotGetAcceptedDisasters/',data).
            then(function(success){
                $scope.notaccepteddisasters = success.data;
            },function(error){
                console.log(error);
            });

        };

        $scope.getnoopiniondisasters = function(i){

            var data = {
                userid : i
            };
            $http.post('/data/NotOpinionDisasters/',data).
            then(function(success){
                $scope.noopiniondisasters = success.data;
            },function(error){
                console.log(error);
            });

        };


        $scope.control = function(i){
            $scope.getaccepteddisasters(i);
            $scope.notgetaccepteddisasters(i);
            $scope.getnoopiniondisasters(i);
            $scope.presentorg = i;
            $scope.view = 1;
        };

        $scope.closebox = function(){
            $scope.notaccepteddisasters = [];
            $scope.accepteddisasters = [];
            $scope.noopiniondisasters = [];
            $scope.view = 0;
            $scope.presentorg = 0;
        };


    }]);



