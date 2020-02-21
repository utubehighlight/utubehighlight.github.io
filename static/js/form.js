
$(document).ready(function() {
	$('form').on('submit', function(event) {
        console.log("I am sumiititngs");
		req=$.ajax({
			data : {
                title : $('#title').val(),
                error: $('dkjsdi').val()
			},
			type : 'POST',
            url : '/process',
            dataType: 'json'
		})
		req.done(function(data) {
            console.log("I am done");
            alert('file naof fajid');
            $('#edit').text(data.title).show();
        });
        
       // alert('file naof fajid');
        $('#edit').text(data.title).show();

		event.preventDefault();

	});

});