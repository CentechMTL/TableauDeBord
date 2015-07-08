function createCard(id, baseLien, linkDeleteCard, linkFounder, username){
    var linkGetDetail = baseLien;
    var myRegexp = /([0-9]+)/g;
    var match = myRegexp.exec(baseLien); //match[1] is the id of the archive
    if(match[1]){
        var pos = baseLien.lastIndexOf('/'); // position du dernier "/"
        var lien = baseLien.substr(0, pos+1);
        lien = lien+id;
        $.ajax({
            type: 'GET',
            url: lien,

            success: function(data, status) {
                //Create card
                var li = document.createElement('li');
                li.className = "card ui-sortable-handle";
                li.id = "card-"+data.id;

                //Add card on the phase
                var ul = document.getElementById("phase-"+data.phase);
                ul.appendChild(li);

                refreshCard(id, baseLien, linkDeleteCard, linkFounder, username);
            },

            error: function(resultat, status, erreur) {
                alert(erreur);
            }
        });
    }
}