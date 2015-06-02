// GET for delete an element
function deleteArchive(name, baseLien){
    var myRegexp = /([0-9]+)/g;
    var match = myRegexp.exec(name); //match[1] is the id of the archive
    if(match[1]){
        var pos = baseLien.lastIndexOf('/'); // position du dernier "/"
        baseLien = baseLien.substr(0, pos+1);
        var lien = baseLien+match[1];
        var div = document.getElementById("archive"+match[1]);
        $.ajax({
          type: 'GET',
          url: lien,

          success: function(data, status) {
                div.remove();
            },

          error: function(resultat, status, erreur) {
                alert(erreur);
            }
        });
    }
}