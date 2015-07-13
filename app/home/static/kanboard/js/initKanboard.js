function initKanboard(baseLien, id, lienGetDetail, linkDeleteCard, linkFounder, username, state){
    var pos = baseLien.lastIndexOf('/'); // position du dernier "/"
    baseLien = baseLien.substr(0, pos+1);
    baseLien = baseLien + state

    $.ajax({
        type: 'GET',
        url: baseLien,

        success: function(data, status) {
            var board = document.getElementById('board');
            board.innerHTML = "";
            var compteurPhase = 0;

            for(phase in data){
                compteurPhase = compteurPhase +1;

                var div = document.createElement('div');
                div.className = "column";

                var titlePhase = document.createElement('h2');
                titlePhase.innerHTML = data[phase][0];

                var ul = document.createElement('ul');
                ul.className = "sortable phase";
                ul.id = "phase-"+compteurPhase;

                for(card in data[phase][1]){
                    var li = document.createElement('li');
                    li.className = "card";
                    li.id = "card-"+card;

                    ul.appendChild(li);

                    refreshCard(card, lienGetDetail, linkDeleteCard, linkFounder, username);
                }

                div.appendChild(titlePhase);
                div.appendChild(ul);
                board.appendChild(div);
            }

        initSortable();
        },

        error: function(resultat, status, erreur) {
            alert(erreur);
        }
    });
}