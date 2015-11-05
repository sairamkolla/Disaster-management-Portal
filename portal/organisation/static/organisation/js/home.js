/**
 * Created by sairam on 6/11/15.
 */

var app = angular.module('myapp', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.controller('myctrl', ['$scope', '$http', '$templateCache','$interval',
    function($scope, $http, $templateCache,$interval) {
        console.log("inside controller");

        $scope.init = function(){
            console.log('inside init');
            $scope.messages = [];
            $scope.disasters = [];
            $scope.messageid=0
            $scope.disasterid=0
            $http.get('http://127.0.0.1:8000/orgs/getuserid/').then(
                function(response){
                    $scope.id = response.data.id
                    console.log('useris fetched')
                    console.log($scope.id)
                }, function(error){
                    console.log(error);
                });
            console.log('timer running')
            $interval($scope.getmessages,5000);
            $interval($scope.getdisasters,10000);

        };
        $scope.getdisasters = function(){
            //console.log($scope.id)
            $http.get('http://127.0.0.1:8000/data/getdisasters/'+ $scope.id +'/'+ $scope.disasterid + '/').
            then(function(response) {
                var temp = response.data.length
                for(i=0;i<temp;i++){
                    $scope.disasters.push(response.data[i]);
                }
                $scope.disasterid=$scope.disasters[$scope.disasters.length-1]["id"];

            }, function(error) {
                console.log(error);
            });
        };
        $scope.getmessages = function(){
            //console.log($scope.id)
            $http.get('http://127.0.0.1:8000/data/getmessages/'+ $scope.id +'/'+ $scope.messageid + '/').
            then(function(response) {
                var temp = response.data.length
                for(i=0;i<temp;i++){
                    $scope.messages.push(response.data[i]);
                }
                $scope.messageid=$scope.messages[$scope.messages.length-1]["id"];


            }, function(error) {
                console.log(error);
            });


        };
    }]);

