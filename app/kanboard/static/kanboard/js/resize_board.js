function resize_board() {
	var width = $('#board').width();
	var columns = $('#board .column').length;
	var col_width = parseInt(width / columns);
	var last_width = width - (col_width * (columns - 1)) - 18;
	$('#board .column').each(function(i) {
		$(this).width(i == columns - 1 ? last_width : col_width);
	});
}