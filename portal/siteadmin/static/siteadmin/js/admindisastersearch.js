
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
            $scope.presentdisaster=0;
            $scope.view = 0;
        };

        $scope.SearchDisasters = function(i){
        console.log('in here test');
            if( $scope.disastersearchparameter != ''){
                if(i==1){
                    var data = {
                     keyword:$scope.disastersearchparameter,
                     code:1
                    };
                }
                else{
                    var data = {
                     keyword:$scope.disastersearchparameter
                    };
                }
                $http.post('/data/getdisasterlist/',data).
                then(function(success){

                    $scope.requireddisasters = success.data
                    $scope.disastersearchparameter='';


                },function(error){
                    console.log(error);
                });
            }
            else{
                $scope.requireddisasters = [];

            }

        };

        $scope.getacceptedorgs = function(i){

            var data = {
                disasterid : i
            };
            $http.post('/data/GetAcceptedOrgs/',data).
            then(function(success){
                $scope.acceptedorgs = success.data;
                $scope.presentdisaster = i;
                $scope.view = 1;
            },function(error){
                console.log(error);
            });

        };

        $scope.notgetacceptedorgs = function(i){

            var data = {
                disasterid : i
            };
            $http.post('/data/NotGetAcceptedOrgs/',data).
            then(function(success){
                $scope.notacceptedorgs = success.data;
            },function(error){
                console.log(error);
            });

        };

        $scope.getnoopinionorgs = function(i){

            var data = {
                disasterid : i
            };
            $http.post('/data/NotOpinionOrgs/',data).
            then(function(success){
                $scope.noopinionorgs = success.data;
            },function(error){
                console.log(error);
            });

        };


        $scope.control = function(i){
            $scope.getacceptedorgs(i);
            $scope.notgetacceptedorgs(i);
            $scope.getnoopinionorgs(i);
            $scope.presentdisaster = i;
            $scope.view = 1;
        };

        $scope.closebox = function(){
            $scope.notacceptedorgs = [];
            $scope.acceptedorgs = [];
            $scope.noopinionorgs = [];
            $scope.view = 0;
            $scope.presentdisaster = 0;
        };


    }]);



