$(document).ready(function(){

	var categories = [];
	var searchQuery = [];
	var clicks = 0;
						
	function addCat(cat) {
		categories.push(cat);
	}

	function queryBuilder(categoryArray) {
		for (i = 0; i < 3; i++) {
			searchQuery.push(categoryArray[i]);
			if (i < 2) {
				searchQuery.push("%2C+");
			}
		}
	}

	

	$(".category").click(function(e){
		if (clicks <= 3) {
			++clicks;
			thisCategory = document.getElementById("cat_id").textContent;

			text = $(e.target).text();
			var number = text.replace(/[^0-9]/g, '')

    		addCat(number);
    			

    		$(this).css('color','red');

    		if (clicks == 3) {
    			addCat(number);

				queryBuilder(categories);
				stringQuery = searchQuery.join('');
				stringQuery = escape(stringQuery);
    		}
		} else if (clicks > 3) {
			alert("You can only make three choices!");
			clicks++;
		}
	});	
});