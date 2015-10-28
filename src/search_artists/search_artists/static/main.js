(function() {
  'use strict';
  if (document.getElementById('ex2')) {
    var slider = new Slider('#ex2', {});
  }

  $(function() {
    $('#myTabs a').click(function(e) {
      e.preventDefault();
      $(this).tab('show');
    });
  });
})();