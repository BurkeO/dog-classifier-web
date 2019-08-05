app.controller("indexCtrl", function($scope) {
  $scope.navLinks = [{name:'Home'}, {name:'About'}, {name:'Code'}];
  $scope.logoURL = "views/assets/Black_Paw.png";

  $scope.myFile = null;

  $scope.preview = function (file) {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('#preview').attr('src', e.target.result);
    }
    reader.readAsDataURL(file);
  }

  $scope.clickUpload = function(){
      console.dir($scope.myFile);
      $scope.preview($scope.myFile);
      console.log("test");
  }

});