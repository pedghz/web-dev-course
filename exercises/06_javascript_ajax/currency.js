$(document).ready(function() {
  'use strict';
  
  $('#search').click(function(e) {
	  e.preventDefault();
	  $("#currencies tr").remove(); 
	  $.getJSON( "http://api.fixer.io/" + $('#date').val() + "?callback=?" , function( data ) {
			var items = [];
			$.each( data.rates, function( key, val ) {
				items.push( "\n<tr>\n<td>" + key + "</td>\n<td>" + val + "</td>\n</tr>" );
			});
			$('#currencies').append(items);
		});
	});
});