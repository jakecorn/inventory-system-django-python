$(document).ready(function() {
	total_payment_display("total_payment"); //this is to display total payment at the buttom of the inventory
});
function total_payment_display(class_name){
	var total = 0;
	$('.'+class_name).each(function(index, el) {
		total+=parseFloat($(this).attr("name"));
	});

	$('#total_payment_display').text(total.toFixed(2));
}