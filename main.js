// Инициализация всех каруселей
	document.querySelectorAll('.carousel').forEach(carousel => {
		const track = carousel.querySelector('.carousel-track');
		const slides = Array.from(track.children);
		const nextButton = carousel.querySelector('.next');
		const prevButton = carousel.querySelector('.prev');
		const dotsNav = carousel.querySelector('.carousel-dots');

		// Создаём точки
		slides.forEach((_, index) => {
			const dot = document.createElement('span');
			dot.classList.add('dot');
			if (index === 0) dot.classList.add('active');
			dotsNav.appendChild(dot);
		});

		const dots = Array.from(dotsNav.children);
		let currentSlide = 0;

		function updateCarousel(index) {
			track.style.transform = `translateX(-${index * 100}%)`;
			slides.forEach(slide => slide.classList.remove('active'));
			slides[index].classList.add('active');
			dots.forEach(dot => dot.classList.remove('active'));
			dots[index].classList.add('active');
			currentSlide = index;
		}

		nextButton.addEventListener('click', () => {
			let nextIndex = (currentSlide + 1) % slides.length;
			updateCarousel(nextIndex);
		});

		prevButton.addEventListener('click', () => {
			let prevIndex = (currentSlide - 1 + slides.length) % slides.length;
			updateCarousel(prevIndex);
		});

		dots.forEach((dot, index) => {
			dot.addEventListener('click', () => {
				updateCarousel(index);
			});
		});
	});