/*
    // Clean version
    $(function() {
      $('.sortable').sortable({connectWith: '.sortable'}).disableSelection();
    });
//*/
//*
function initSortable(){
	$('.sortable').sortable({
		connectWith: '.sortable',
		stop: function(e, ui) {
            var sender = ui.sender ? ui.sender[0].id : "(none)";
            var item = ui.item[0].id;
            var target = e.target.id;
            var data = {};
            $('ul.phase').each(function() {
                data[this.id] = $.map($(this).find('li.card'), function(y) { return y.id})
            });

            $.ajax({
                type: 'post',
                url: 'update/',
                data: data,

                success: function(data) {
                },
                error: function(resultat, status, erreur) {
                    alert(resultat + " - " + status + " - " + erreur);
                }
            });
	    }
	}).disableSelection();
	resize_board();
	$(window).bind('resize', resize_board);
}
//*/

