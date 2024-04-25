  // code for the modal
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
  });
  
  // Or with jQuery
  
  $(document).ready(function(){
    $('.modal').modal();
  });
  
  // code for collapsable modal
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, options);
  });
  
  // Or with jQuery
  
  $(document).ready(function(){
    $('.collapsible').collapsible();
  });