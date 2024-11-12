document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.star');
    const ratingValue = document.getElementById('rating-value');

    // Set initial stars based on current rating
    highlightStars(ratingValue.value);

    // Handle hover event
    stars.forEach(star => {
        star.addEventListener('mouseover', function() {
            resetStars(); // Reset all stars before highlighting
            highlightStars(this.getAttribute('data-value')); // Highlight stars based on hover
        });

        star.addEventListener('mouseout', function() {
            resetStars(); // Reset stars when not hovering
            highlightStars(ratingValue.value); // Highlight stars based on selected value
        });

        // Handle click event (locking in rating)
        star.addEventListener('click', function() {
            ratingValue.value = this.getAttribute('data-value'); // Set rating value
            highlightStars(ratingValue.value); // Highlight based on clicked value
        });
    });

    // Function to reset all stars to default (unfilled)
    function resetStars() {
        stars.forEach(star => star.classList.remove('filled'));
    }

    // Function to highlight stars up to the specified value
    function highlightStars(rating) {
        for (let i = 0; i < rating; i++) {
            stars[i].classList.add('filled');
        }
    }
});
