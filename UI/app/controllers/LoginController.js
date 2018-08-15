app.controller('LoginController', function ($scope, $http) {
    $scope.message = 'login not called';
    $scope.user='';
    $scope.pwd='';
    $scope.errorMessage ='';
    $scope.login = function(){
        $http({
            method:'post',
            url:'http://localhost:8000/login',
            data:'{"name":"'+$scope.user+'", "credential":"'+$scope.pwd+'"}',
            headers:{'Content-Type':'text/plain'}
        }).then(function success(response){
            sessionStorage.setItem('cookie',response.data.cookie);
            sessionStorage.setItem('user', $scope.user);
            window.location='index.html';
        }, function error(response)
        {
            $scope.errorMessage =response;
        });
    }
})