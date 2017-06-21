var residentsButton = "asd";

$('#residents').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var planetName = button.data('planet-name') // Extract info from data-* attributes
    var residents = button.data('residents') // Extract info from data-* attributes
    var modal = $(this)

    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library 
    // or other methods instead.
    
    modal.find('.modal-title').text('Residents of ' + planetName)
    modal.find('.modal-body').text('list: ' + residents)
    // modal.find('.modal-body input').val(recipient)
})
