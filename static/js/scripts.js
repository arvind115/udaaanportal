// function showBody(){
//   document.getElementsByTagName('body')[0].style.visibility = 'visible';
//   console.log('in showBoyd()');
// }

// $(window).on('load',function() {
//   document.getElementsByTagName('body')[0].style.visibility = 'hidden';
//   setTimeout(showBody,600);
// });

$(document).ready(function() {
  const url = $(location).attr('pathname');
  console.log('url = ',url);
  if( url.includes('/membercreate') || url.includes('/memberupdate') ){
    var mylabel = $('label[for="' + $('#id_photo').attr('id') + '"]');
    mylabel.html('');
    mylabel.addClass('btn-2');

    $('#id_preferred_days').bsMultiSelect({ 
      // nonSelectedText: 'Pick your days..',
    });

    $("#id_photo").on("change", function() {
      var fileName = $(this).val().split("\\").pop();
      $(this).siblings(".btn-2").addClass("selected").html(fileName);
    });

    $('#id_username').val(document.getElementById('user').value);
    $('#id_username').prop('readonly', true);
    $('#id_working_days').prop('readonly', true);

  }

  if( url.includes('/memberupdate') ){
    $('.btn-2').css('top','65px');

    const prevImgName = $('.inputDiv:last > a').html().split('/').pop();
    $('.btn-2').html(prevImgName);

    // get the selected state ID from the HTML input
    $.ajax({                       // initialize an AJAX request
      url: '../doesnotmatter2',       // set the url of the request (= localhost:8000/doesnotmatter2/)
      data: {
        'state': $("#id_state").val()       // add the state id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_state` view function
        console.log('AJAX call successful..');
        $("#id_city").html(data);  // replace the contents of the branch input with the data that came from the server
      },
      error: function(err){
        console.log('AJAX request failed..');
      }
    });
    // get the selected course ID from the HTML input
    $.ajax({                       // initialize an AJAX request
      url: '../doesnotmatter',       // set the url of the request (= localhost:8000/doesnotmatter/)
      data: {
        'course': $('#id_course').val()       // add the course id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_branches` view function
        $("#id_branch").html(data);  // replace the contents of the branch input with the data that came from the server
      },
      error: function(err){
        console.log('AJAX request failed..');
      }
    });
  }
  $("#id_course").change(function () {
    $.ajax({                       // initialize an AJAX request
      url: '../doesnotmatter',       // set the url of the request (= localhost:8000/doesnotmatter/)
      data: {
        'course': $(this).val()       // add the course id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_branches` view function
        $("#id_branch").html(data);  // replace the contents of the branch input with the data that came from the server
      },
      error: function(err){
        console.log('AJAX request failed..');
      }
    });
  });
  $("#id_state").change(function () {
    // get the selected state ID from the HTML input
    $.ajax({                       // initialize an AJAX request
      url: '../doesnotmatter2',       // set the url of the request (= localhost:8000/doesnotmatter2/)
      data: {
        'state': $(this).val()       // add the state id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_state` view function
        console.log('AJAX call successful..');
        $("#id_city").html(data);  // replace the contents of the branch input with the data that came from the server
      },
      error: function(err){
        console.log('AJAX request failed..');
      }
    });
  });
});




