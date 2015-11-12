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
            $scope.disasters = [];
            $scope.disasterid=0
            console.log('timer running')
            $interval($scope.getnotapproveddisasters,10000);

        };
        $scope.getnotapproveddisasters = function(){
            $http.get('http://127.0.0.1:8000/data/getnotapproveddisasters/'+ $scope.disasterid + '/').
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

        $scope.approval = function(disasterid,opinion){

            $http.post('http://127.0.0.1:8000/data/approval/' + disasterid + '/' + result + '/').then(
            function(response){
                console.log(response.data);
            },function(error){
                console.log(error);
            });
        };
    }]);

