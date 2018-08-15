app.controller('UpdateTicketsController', function ($scope, $http) {
    $scope.teamId = sessionStorage.getItem('curTeamId');
    $scope.cookie = sessionStorage.getItem('cookie');
    $scope.teamName = '';
    $scope.teamTickets = '';
    $scope.errorMessage ='';
    $http({
        method:'post',
        url:'http://localhost:8000/tickets',
        data: '{"operation":"get", "cookie":"'+$scope.cookie+'", "data":{"teamId":"'+$scope.teamId+'", "tickets":""}}',
        headers:{'Content-Type':'text/plain'}
    }).then(function success(response){

        $scope.teamName = response.data[0].team;
        $scope.teamTickets = response.data[0].tickets;
    }, function error(response)
    {
        $scope.errorMessage = response.data;
    });

    $scope.submit = function(){
        $http({
            method:'post',
            url:'http://localhost:8000/updatetickets',
            data: '{"operation":"post", "cookie":"'+$scope.cookie+'", "data":{"teamId":"'+$scope.teamId+'", "tickets":"'+$scope.teamTickets+'"}}',
            headers:{'Content-Type':'text/plain'}
        }).then(function success(goodResponse){
            window.location='index.html';
        }, function error(data)
        {
            $scope.errorMessage = 'You don\'t have permission or the tickets are blocked after 5th.';
        });
    }
})