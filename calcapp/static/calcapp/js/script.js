$(document).ready(function(){
	var testNumLength = function(number) {
        if (number.length > 9) {
            totaldiv.text(number.substr(number.length-9,9));
            if (number.length > 15) {
                number = "";
                totaldiv.text("Err");
            }
        } 
    };
	var number = "";
    var newnumber = "";
    var operator = "";
    var totaldiv = $("#total");
    var query = $("#query");
    totaldiv.text("0");

    $("#numbers a").not("#clear,#clearall").click(function(){
		number += $(this).text();
		totaldiv.text(number);
		testNumLength(number);
    });
    $("#operators a").not("#equals").click(function(){
		operator = $(this).text();
		newnumber = number;
		number = "";
		totaldiv.text("0");
    });
    $("#clear,#clearall").click(function(){
		number = "";
		totaldiv.text("0");
		if ($(this).attr("id") === "clearall") {
			newnumber = "";
		}
    });
    //Add your last .click() here!
    var querystring = "";
    $("#equals").click(function(){
    	if (operator === "+"){
            querystring = newnumber + operator + number + "=" ;
    		number = (parseInt(number, 10) + parseInt(newnumber,10)).toString(10);
    	} else if (operator === "-"){
            querystring = newnumber + operator + number + "=" ;
    		number = (parseInt(newnumber, 10) - parseInt(number,10)).toString(10);
    	} else if (operator === "/"){
            querystring = newnumber + operator + number + "=" ;
    		number = (parseInt(newnumber, 10) / parseInt(number,10)).toString(10);
    	} else if (operator === "*"){
            querystring = newnumber + operator + number + "=" ;
    		number = (parseInt(newnumber, 10) * parseInt(number,10)).toString(10);
    	}
    	totaldiv.text(number);
    	testNumLength(number);
        var querystringfinal = querystring + number; 
        query.text(querystringfinal);
        query.append('<button type="submit">POST</button>');
        document.getElementById('query_value').value = querystringfinal;
        querystring = "";
        querystringfinal = "";
    	// number = "";
    	newnumber = "";
    });

});