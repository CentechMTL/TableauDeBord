function editCard(id, baseLien){
    var myRegexp = /([0-9]+)/g;
    var match = myRegexp.exec(baseLien); //match[1] is the id of the archive
    if(match[1]){
        var pos = baseLien.lastIndexOf('/'); // position du dernier "/"
        baseLien = baseLien.substr(0, pos+1);
        var lien = baseLien+id;

        $.ajax({
            type: 'GET',
            url: lien,

            success: function(data, status) {
                //We change the title of the form
                var titleForm = document.getElementById('ui-id-1');
                titleForm.innerHTML = gettext("Edit the task");

                //We populate the form
                var form = document.getElementById('form');
                document.getElementById('phase').value = data.phase;
                document.getElementById('title').value = data.title;
                document.getElementById('comment').value = data.comment;
                document.getElementById('update').value = data.id;
                document.getElementById('state').checked = data.state;
                if(data.deadline){
                    document.getElementById('deadline').value = data.deadline;
                }
                if(data.assigned){
                    document.getElementById('assigned').value = data.assigned;
                }

                document.getElementById('create-card').click();
            },

            error: function(resultat, status, erreur) {
                alert(erreur);
            }
        });
    }
}