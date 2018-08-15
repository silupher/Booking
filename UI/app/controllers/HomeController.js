app.controller('HomeController', function ($scope, $http) {
    $scope.loggedIn=false;
    $scope.cookie = sessionStorage.getItem('cookie');
    $scope.user = sessionStorage.getItem('user');
    $scope.userRole='';
    $scope.userROleMessage='';
    $scope.curMonth='';
    $scope.env = '';
    $scope.teamRecords=[];
    $scope.allowAdmin = false;
    if($scope.cookie != null)
    {
        $scope.message = 'Welcome! ' + $scope.user;
        $scope.loggedIn=true;
    }
    else
    {
        window.location='Login.html';
    }

    if($scope.loggedIn == true) {
        $http({
            method: 'post',
            url: 'http://localhost:8000/role',
            data: '{"operation":"get", "cookie":"'+$scope.cookie+'", "data":""}',
            headers:{'Content-Type':'text/plain'}
        }).then(function success(roleResponse) {
            $scope.userRoleMessage = 'Your role is '+roleResponse.data.role;
            $scope.userRole = roleResponse.data.role;
            if ($scope.userRole != "TeamMember")
            {
                $scope.allowAdmin = true;
            }
            $http({
                method: 'post',
                url: 'http://localhost:8000/sys',
                data: '{"operation":"get", "cookie":"'+$scope.cookie+'", "data":""}',
                headers:{'Content-Type':'text/plain'}
            }).then(function success(confResponse) {
                $scope.curMonth = confResponse.data.Date;
                $scope.env = confResponse.data.Env;
                $scope.loadTeamStatus();
            }, function error(confResponse) {
                console.log((confResponse))

            });
        }, function error(roleResponse) {
            console.log((roleResponse))

        });
    }

    $scope.logout = function()
    {
        sessionStorage.clear();
        $scope.loggedIn=false;
        window.location='Login.html';
    }

    $scope.loadTeamStatus = function()
    {
        $http({
            method: 'post',
            url: 'http://localhost:8000/tickets',
            data: '{"operation":"get", "cookie":"'+$scope.cookie+'", "data":""}',
            headers:{'Content-Type':'text/plain'}
        }).then(function success(teamResponse) {
            for(var i=0;i<teamResponse.data.length; i++)
            {
                $scope.teamRecords.push({"Id": teamResponse.data[i].id, "Name": teamResponse.data[i].team, "Tickets": teamResponse.data[i].tickets
                    // , "Button"
                    //     :'<button ng-click="updateTickets('+teamResponse.data[i].id+'\')"></button>'
                })
            }
        }, function error(teamResponse) {
            console.log(teamResponse)

        });
    }

    $scope.updateTickets = function(teamId)
    {
        sessionStorage.setItem('curTeamId', teamId);
        window.location='UpdateTickets.html';
    }
})