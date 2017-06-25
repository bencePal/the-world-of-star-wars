
$('#residents').on('show.bs.modal', function (event) {
    
    var button = $(event.relatedTarget)

    var planetName = button.data('planet-name')
    var residents = button.data('residents')
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

$('#residents').on('hidden.bs.modal', function () {
    $(this).find('.modal-body').text('');
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




$(".add-vote").on("click", function() {

    var vote = {
        planetId: this.getAttribute('data-planet-id'),
        userId: this.getAttribute('data-user-id'),
        planetName: this.getAttribute('data-planet-name')
    }

    $.ajax({
        type: 'POST',
        url: '/',
        data: JSON.stringify(vote),
        contentType: 'application/json;charset=UTF-8',
        success: function() {
            $('.table-responsive').prepend('<div class="alert alert-success"><strong>Your vote has been saved</strong></div>')
            setTimeout(function(){ 
                $('.alert-success').remove()
            }, 2000);
        }
    })

});
    


$('#votes').on('show.bs.modal', function (event) {
    
    var modal = $(this)
    modal.find('.modal-title').text('Votes')
    
    modal.find('.modal-body').append('<table class="table-bordered votes-table table-hover"><tr>' +
                                     '<td>Planet name</td>' +
                                     '<td>Vote number</td>' +
                                     '</tr></table>');

    $.ajax({
        type: 'GET',
        url: '/planet_votes',
        success: function(data) {
            $.each(data, function(key, value) {
                modal.find('.votes-table').append('<tr>' +
                                                  '<td>' + key + '</td>' +
                                                  '<td>' + value + '</td>' +
                                                  '</tr>')
            });
        }
    })
})

$('#votes').on('hidden.bs.modal', function () {
    $(this).find('.modal-body').text('');
})