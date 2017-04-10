function keywordusage(sentence, word) {
	var result = new Array();
    for (i = 0; i < word.length; i++) { 
		if (sentence.search(word[i]) > -1) {
			result[i] = true;
		} else
			result[i] = false;
	}
	return result;
}

function frequencies(sentence, word) {
	var result = {};
    var num;
	var words = sentence.split(/\s+/);
	var c;
	for (i = 0; i < word.length; i++) {
		c = 0;
		for (var j = 0; j < words.length; j++){
			if (words[j] == word[i]){
				c++;
			}
		}
		result[word[i]] = c;
	}
	return result;
}


function rotate() {

	var arr = arguments[0];
	var temp = 0;	
	
	if (arr.length < 2){
		return arr;
	}
	
	var num = 1;
	
	if (arguments.length == 2) {
		num = arguments[1];
		while (num < 0)	
			num = arr.length + num;
		if (num == 0) 		{
			return arr;
		}
		
	}
	
	console.log(num);
	
	for (i = 0; i < num; i++){
		temp = arr[arr.length -1];
		for (j = arr.length - 1; j > 0; j--){
			arr[j] = arr[j-1];
		}
		arr[0] = temp;
	}
		
	return arr;
}