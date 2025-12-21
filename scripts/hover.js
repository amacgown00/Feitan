document.addEventListener("DOMContentLoaded", () => {
		const hovers = document.querySelectorAll(".hover");
		
		hovers.forEach(el => {
				let bubble;
				
				const showDisplay = () => {
						bubble = document.createElement("div");
						bubble.className = "display-bubble";
						bubble.textContent = el.dataset.display;
						el.appendChild(bubble);
				};
				
				const hideDisplay = () => {
						if (bubble) {
										bubble.remove();
										bubble = null;
						}
				};
		
				el.addEventListener("mouseenter", showDisplay);
		  el.addEventListener("mouseleave", hideDisplay);
		
		  el.addEventListener("click", (e) => {
			     e.stopPropagation();
								bubble ? hideDisplay() : showDisplay();
				});
				
				document.addEventListener("click", hideDisplay);
		});
});