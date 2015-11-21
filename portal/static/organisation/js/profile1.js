
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
                    $scope.getnumbers();
                    $scope.getmails();
                    console.log($scope.userdetails.username)
                },function(error){
                    console.log(error);
                });
        }
        $scope.init = function(){
            console.log('inside init');
            $scope.messages = [];

            $scope.messageid=0;

            $scope.is_search = 0;
            $scope.receiver = 0;
            console.log('dropdown disabled');
            $http.get('http://127.0.0.1:8000/orgs/getuserid/').then(
                function(response){
                    $scope.id = response.data.id
                    console.log('useris fetched');
                    console.log($scope.id);

                    $scope.getmessages();
                }, function(error){
                    console.log(error);
                });

            $scope.getuserdetails();

            console.log('timer running')
            $interval($scope.getmessages,5000);
            $interval($scope.getdisasters,10000);


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

        $scope.getnumbers = function(){
            var data = {
                userid:$scope.userdetails['userid']
            };
            $http.post('http://127.0.0.1:8000/data/GetNumbers/',data).
            then(function(success){
                $scope.numbers = success.data;
            },function(error){
                console.log(error)
            });

        };

        $scope.getmails = function(){
            var data = {
                userid:$scope.userdetails['userid']
            };
            $http.post('http://127.0.0.1:8000/data/GetEmails/',data).
            then(function(success){
                $scope.emails = success.data;
            },function(error){
                console.log(error)
            });

        }


        $scope.GetSearchOrgs = function(){
        console.log('in here test');
            if( $scope.searchword != ''){

                var data = {
                    keyword:$scope.searchword
                };
                $http.post('/data/getorglist/',data).
                then(function(success){

                    $scope.searchorgs = success.data
                    $scope.is_search = 1;

                },function(error){
                    console.log(error);
                });
            }
            else{
                $scope.searchorgs = [];
                $scope.is_search = 0;

                $scope.receiver = 0;
            }

        };

        $scope.selectorg = function(id,name){


            $scope.searchword = name
            $scope.searchorgs = [];
            $scope.is_search = 0;
            $scope.receiver = id;

        };

        $scope.sendmessage = function(){
            if($scope.sender !=0){
                console.log($scope.messagecontent);
                console.log($scope.receiver);
                var data = {
                    messagecontent:$scope.messagecontent,
                    receiver: $scope.receiver
                };
                $http.post('/data/CreateMessage/',data).
                then(function(success){
                    $scope.messagecontent = '';
                    $scope.searchword = '';
                    $scope.receiver = 0;
                },function(error){
                    console.log(error);
                });
            }
        };

        $scope.addnumber = function(){
            if($scope.enternumber!=''){
                var data = {
                    number:$scope.enternumber,
                    userid:$scope.userdetails['userid']
                };
                $http.post('http://127.0.0.1:8000/data/AddNumber/',data).
                then(function(success){
                    console.log("Number Added");
                    $scope.enternumber='';
                    $scope.getnumbers();
                },function(error){
                    console.log("Number Not Added")
                    $scope.enternumber=''
                });
            }
        };

        $scope.addemail = function(){
            if($scope.enteremail!=''){
                var data = {
                    email:$scope.enteremail,
                    userid:$scope.userdetails['userid']
                };
                $http.post('http://127.0.0.1:8000/data/AddEmail/',data).
                then(function(success){
                    console.log("Email Added");
                    $scope.enteremail=''
                    $scope.getmails();

                },function(error){
                    console.log("Email Not Added")
                    $scope.enteremail=''
                });
            }
        };
    }]);



