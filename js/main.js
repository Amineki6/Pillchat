function handleKeyDown(event) {
	if (event.keyCode === 13) {
		event.preventDefault();
		sendMessage();
	}
}
