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

        $scope.approval = function(id,result){
            var data = {
                disasterid : id,
                opinion : result
             };
            $http.post('http://127.0.0.1:8000/data/approval/',data).then(
            function(response){
                console.log(response.data);
            },function(error){
                console.log(error);
            });
        };
        $scope.test = function(){
            console.log("hello");
            //var data = $.param({
              //  receiver_org_id:8,
                //message_content: "hello_kolla"
            //});
            var data = {
                receiver_org_id:'8',
                message_content: 'hello_kolla'
            };
            $http.post('http://127.0.0.1:8000/data/test/',data).
            then(function(response){
                console.log(response);
            },function(error){
                console.log(error);
            }
            );
        };
    }]);

