
var app = angular.module('myapp', []).config(function($interpolateProvider,$httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});



app.controller('myctrl', ['$scope', '$http', '$templateCache','$interval','$sce',
    function($scope, $http, $templateCache,$interval) {
        console.log("inside controller");

        $scope.init = function(){
            console.log('inside init');
            $scope.tweets = [];
        };

        $scope.SearchTwitter = function(){
        console.log('in here test');
            if( $scope.twittersearchparameter != ''){
                $scope.tweets = [];
                var data = {
                   keyword:$scope.twittersearchparameter,
                };
                $http.post('/data/SearchTwitter/',data).
                then(function(success){

                    $scope.tweets = success.data
                    $scope.twittersearchparameter='';


                },function(error){
                    console.log(error);
                });
            }
            else{
                $scope.tweets = [];

            }

        };



    }]);



app.filter('createAnchors', function ($sce) {
    return function (str) {
        return $sce.trustAsHtml(str.
                                replace(/</g, '&lt;').
                                replace(/>/g, '&gt;').
                                replace(/(http[^\s]+)/g, '<a href="$1">$1</a>').
//                                replace(/@([^\s]+)(/g,'<a href="http://twitter.com/$1">@$1</a>')
                                replace(/@([\w)]{1,15})/g,'<a href="http://twitter.com/$1">@$1</a>').
                                replace(/(#[^\s]+)/g,'<a href="#">$1</a>')

                               );
    }
});
