// Read the instructions.html //

//some helpful debug code

$("#javascript_start").html("[OK] Started executing the javascript file");
$("#javascript_end").html("[WAITING]...this far we haven't reached the end... Maybe you should try FireBug?");

// ADD YOUR CODE BETWEEN THESE LINES //

$('a[href$=".pdf"]').addClass( "pdf" );

//$( 'a[href$="\.[a-z][a-z][a-z]"]' ).not( $('a[href$=".pdf"]')).not($('a[href$=".html"]')).addClass( "download" );//
//if ($("a").attr("href").match(/page=([0-9]+)/)[1]; //
var arr = [], l = document.links;
for(var i=0; i<l.length; i++) {
  if(l[i].href.length - l[i].href.lastIndexOf(".") == 4 && l[i].href.slice(-1) != "/"  && l[i].href.slice(-4) != ".pdf" ) 	{
	var words = l[i].href.split("/");
	$('a[href$="'+words[words.length-2]+'/'+words[words.length-1]+'"]').addClass( "download" );
  }
}
// ADD YOUR CODE BETWEEN THESE LINES //

//some helpful debug code

$("#javascript_end").html("[OK] The end of your javascript file was reached. (meaning there were no huge errors) Hopefully your code works too! ");
