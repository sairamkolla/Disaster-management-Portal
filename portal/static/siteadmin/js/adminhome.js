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

            console.log('timer running')
            reports = []
            $scope.getstatistics();
            $interval($scope.getstatistics,10000);

        };
        $scope.getstatistics = function(){
            $http.get('http://127.0.0.1:8000/data/statistics/').
            then(function(response) {
                $scope.reports=response.data

            }, function(error) {
                console.log(error);
            });
        };
    }]);
