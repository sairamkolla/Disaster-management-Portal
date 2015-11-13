/**
 * Created by sairam on 6/11/15.
 */

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
            $scope.orgs = [];
            $scope.orgid=0;
            $scope.key='fire';
            console.log('timer running')
            //$interval($scope.getorgs,3000);
        };

        $scope.set = function(abc){
            $scope.key = abc
            var data = {
                keyword : $scope.key
            };
            console.log(data)
            $http.post('http://127.0.0.1:8000/data/orglist/',data).
            then(function(response){
                console.log(response.data);
               // var temp = response.data.length;
               // for(i=0;i<temp;i++){
               //     $scope.orgs.push(response.data[i]);
               // }
               // $scope.orgid=$scope.orgs[$scope.orgs.length-1]["id"];
               // console.log(response);
               $scope.orgs = response.data;
            },function(error){
                console.log(error);
            });
        };
        //$scope.set = function(abc){
         //   console.log(abc)
         //   $scope.key = abc;
         //   $scope.getorgs();
        //};
    }]);

