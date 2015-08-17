// Change the form for update element
function editElement(id, baseLien){
    var myRegexp = /([0-9]+)/g;
    var match = myRegexp.exec(id); //match[1] is the id of element
    if(match[1]){
        idElement = match[1];
        var myRegexp = /([a-zA-Z]+)/g;
        var match = myRegexp.exec(id); //match[1] is the id of element
        if(match[1]){
            type = match[1];
            var pos = baseLien.lastIndexOf('/'); // position du dernier "/"
            baseLien = baseLien.substr(0, pos+1);
            var lien = baseLien+idElement;

            $.ajax({
              type: 'GET',
              url: lien,

              success: function(data, status) {
                    var form = document.getElementById(type);
                    var inputs = form.getElementsByTagName("input");
                    //inputs[0] -> token CSRF
                    inputs[1].value = data.title;
                    inputs[2].value = data.comment;
                    inputs[3].value = idElement;

                    updateDisplayForm(type, "True");
                },

              error: function(resultat, status, erreur) {
                alert(erreur); }
            });
        }
    }
}