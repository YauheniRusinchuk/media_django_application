$(function(){

  $(".form").on('submit', (e) => {
    e.preventDefault();
    create_comment();
  })

});


function create_comment() {
  $.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: {
      comment: $('.input_comment').val(),
      csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
    },
    success : function(data) {
      
      let newItem = document.createElement('p')
      newItem.innerHTML = data.message;
      $('.input_comment').val("");
      $('.comments_containers').append(newItem);
    }
  })
}