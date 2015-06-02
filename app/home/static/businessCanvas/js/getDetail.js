// GET for show details of an element
function getDetail(id, baseLien){
    var myRegexp = /([0-9]+)/g;
    var match = myRegexp.exec(id); //match[1] is the id of element
    var div = document.getElementById(match[1]);
    var p = div.getElementsByTagName("p")[0];
    if(p.style.visibility == "hidden"){
        var pos = baseLien.lastIndexOf('/'); // position du dernier "/"
        baseLien = baseLien.substr(0, pos+1);
        var lien = baseLien+div.id;
        var id = div.id;

        $.ajax({
          type: 'GET',
          url: lien,

          success: function(data, status) {
                p.textContent = data.comment;
                p.style.visibility = "visible";
                p.style.display = "block";
            },

          error: function(resultat, status, erreur) {
            alert(erreur); }
        });
    }
    else{
        p.style.visibility = "hidden";
        p.style.display = "none";
    }
}