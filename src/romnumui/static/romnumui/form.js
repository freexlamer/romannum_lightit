function ProcessResponse(data) {
	var response = jQuery.parseJSON(data);
	document.getElementById("Output").value = response.output;
};

function DoConvert() {
	var inputvalue = document.getElementById("Input").value;
	var obj = {
		'input': inputvalue
	};

	$.ajax({
        url: "api/convert",
        type: "POST",
        data: JSON.stringify(obj),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: ProcessResponse,
        /*
        error: function (xhr, ajaxOptions, thrownError) {
        alert(xhr.status);
        alert(thrownError);
        }
        */
    });

};