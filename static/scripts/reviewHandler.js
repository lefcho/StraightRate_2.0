const movieDetails = document.getElementById('movie-details');
const movieId = movieDetails.dataset.movieId;
const userAuthenticated = movieDetails.dataset.userAuth === "true"; // Boolean conversion
const userReviewContainer = document.getElementById('user-review-container');


document.addEventListener('DOMContentLoaded', () => {
    // Fetch CSRF token for POST requests
    const headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
    };

    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [key, value] = cookie.trim().split('=');
            if (key === name) return value;
        }
        return null;
    }

    if (userAuthenticated) {
        createReviewForm();
    }
});


function initStarRating() {
    const stars = document.querySelectorAll('.star');
    const ratingValue = document.getElementById('rating-value');

    // Set initial stars based on current rating
    highlightStars(ratingValue.value);

    stars.forEach(star => {
        star.addEventListener('mouseover', function () {
            resetStars(); // Reset all stars before highlighting
            highlightStars(this.getAttribute('data-value')); // Highlight stars based on hover
        });

        star.addEventListener('mouseout', function () {
            resetStars(); // Reset stars when not hovering
            highlightStars(ratingValue.value); // Highlight stars based on selected value
        });

        // Handle click event (locking in rating)
        star.addEventListener('click', function () {
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
}

function createReviewForm(review = null) {
    // Create form element
    const reviewForm = document.createElement('form');
    reviewForm.classList.add('review-form');
    reviewForm.id = 'user-review-form';

    // Create the star-rating container
    const starRatingDiv = document.createElement('div');
    starRatingDiv.classList.add('star-rating');

    // Create the hidden input for rating
    const ratingInput = document.createElement('input');
    ratingInput.type = 'hidden';
    ratingInput.name = 'rating';
    ratingInput.id = 'rating-value';
    ratingInput.value = review ? review.rating : 0;  // Set value if review exists

    // Create star icons dynamically
    for (let i = 1; i <= 5; i++) {
        const starIcon = document.createElement('i');
        starIcon.classList.add('fa', 'fa-star', 'star');
        starIcon.dataset.value = i;
        starRatingDiv.appendChild(starIcon);
    }

    // Append rating input and star rating div to the form
    reviewForm.appendChild(ratingInput);
    reviewForm.appendChild(starRatingDiv);

    // Create textarea for comment
    const commentTextarea = document.createElement('textarea');
    commentTextarea.name = 'comment';
    commentTextarea.id = 'review-comment';
    commentTextarea.rows = 4;
    commentTextarea.placeholder = "Write your review here...";
    commentTextarea.required = true;
    commentTextarea.value = review ? review.comment : '';  // Set the existing comment if review exists
    reviewForm.appendChild(commentTextarea);

    // Create the submit button
    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.classList.add('btn', 'btn-success');
    submitButton.textContent = review ? 'Update Review' : 'Submit Review';
    reviewForm.appendChild(submitButton);

    // Append the review form to the user review container
    userReviewContainer.innerHTML = ''; // Clear any existing content
    userReviewContainer.appendChild(reviewForm);

    // Initialize star rating logic
    initStarRating();
}