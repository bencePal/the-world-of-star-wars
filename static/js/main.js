
$('#residents').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var planetName = button.data('planet-name') // Extract info from data-* attributes
    var residents = button.data('residents') // Extract info from data-* attributes
    var modal = $(this)
    var arrayResidentsLink = residents.split(",");
    modal.find('.modal-title').text('Residents of ' + planetName)

    modal.find('.modal-body').append('<table class="table-bordered residents-table table-hover"><tr>' +
                                    '<td>Name</td>' +
                                    '<td>Height</td>' +
                                    '<td>Mass</td>' +
                                    '<td>Hair color</td>' +
                                    '<td>Skin color</td>' +
                                    '<td>Eye color</td>' +
                                    '<td>Birth year</td>' +
                                    '<td>Gender</td>' +
                                     '</tr></table>');

    for (var i = 0; i < arrayResidentsLink.length; i++) {
        $.ajax({
            type: 'GET',
            url: arrayResidentsLink[i],
            success: function(data) {
                modal.find('.residents-table').append('<tr>' +
                    '<td>' + data.name + '</td>' +
                    '<td>' + formatHeight(data.height) + '</td>' +
                    '<td>' + formatMass(data.mass) + '</td>' +
                    '<td>' + data.hair_color + '</td>' +
                    '<td>' + data.skin_color + '</td>' +
                    '<td>' + data.eye_color + '</td>' +
                    '<td>' + data.birth_year + '</td>' +
                    '<td>' + data.gender + '</td>' +
                    '</tr>')
            }
        })
    };

})

function formatMass(string) {
    if (string === 'unknown') {
        return string
    }
    return string + ' kg'
}

function formatHeight(string) {
    if (string.length === 3) {
        return string.substr(0, 1) + "," + string.substr(1) + ' m'
    } else if (string.length === 2) {
        return '0,' + string + ' m'
    } else {
        return string
    }
}

$('#residents').on('hidden.bs.modal', function () {
    $(this).find('.modal-body').text('');
})
