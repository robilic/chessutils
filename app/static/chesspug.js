
addPiece = function(e) {
	var div = document.getElementById('pieces');
	div.innerHTML += e;
	if (div.innerHTML.length == 4) {
		console.log("Sending " + div.innerHTML + " to the server as a move");
		window.location.href = "http://localhost:5000/game/1/move/" + div.innerHTML;
	}
};
