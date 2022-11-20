$("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/patient",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/details/";
      console.log(resp);
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});