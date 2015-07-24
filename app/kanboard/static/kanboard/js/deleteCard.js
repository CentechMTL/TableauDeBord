function deleteCard(id, baseLien){
    var myRegexp = /([0-9]+)/g;
    var match = myRegexp.exec(baseLien); //match[1] is the id of the archive
    if(match[1]){
        var pos = baseLien.lastIndexOf('/'); // position du dernier "/"
        baseLien = baseLien.substr(0, pos+1);
        var lien = baseLien+id;
    }
    var li = document.getElementById("card-"+id);

    $.ajax({
          type: 'GET',
          url: lien,

          success: function(data, status) {
                li.remove();
            },

          error: function(resultat, status, erreur) {
                alert(erreur);
            }
        });
}