
// hide line numbers in code pieces right before we copy the code

$(document).ready(function () {
	$("code").bind("copy", function () {
	    var innerHtml = this.innerHTML;
	    $(this).find('.lineno').remove();
	    var that = this;
	    setTimeout(function(){
	        $(that).children().remove();
	        that.innerHTML = innerHtml;
	    },0);
	});
});

