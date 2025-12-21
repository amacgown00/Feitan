document.addEventListener("DOMContentLoaded", () => {
	const hovers = document.querySelectorAll("hover");
	hovers.forEach(el => {
		let bubble;
		const showDisplay = () => {
			bubble = document.createElement("div");
			bubble.className = "display-bubble";
			bubble.textContent = el.dataset.display;
			el.appendChild(bubble);