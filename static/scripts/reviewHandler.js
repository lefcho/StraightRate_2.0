const movieDetails = document.getElementById('movie-details');
const movieId = movieDetails.dataset.movieId;
const userAuthenticated = movieDetails.dataset.userAuth === "true"; // Boolean conversion
const userReviewContainer = document.getElementById('user-review-container');


document.addEventListener('DOMContentLoaded', () => {

    if (userAuthenticated) {
        createReviewForm();
    }

});


function handleReviewFormSubmission(event) {
    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [key, value] = cookie.trim().split('=');
            if (key === name) return value;
        }
        return null;
    }

    event.preventDefault();

    const ratingValue = document.getElementById('rating-value').value;
    const comment = document.getElementById('review-comment').value;

    const reviewData = {
        rating: ratingValue,
        comment: comment,
        movie: movieId,
    };

    // Submit the form via fetch
    fetch(`/reviews/movies/${movieId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify(reviewData),
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to submit review');
            }
        })
        .then(data => {
            // Handle successful submission (e.g., clear the form, show a success message)
            console.log('Review submitted successfully:', data);
            createReviewForm(); // Reset the form after submission
            alert('Your review has been submitted!');
        })
        .catch(error => {
            console.error('Error submitting review:', error);
            alert('There was an error submitting your review.');
        });
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

    // Attach the submit event handler
    reviewForm.addEventListener('submit', handleReviewFormSubmission);

    // Append the review form to the user review container
    userReviewContainer.innerHTML = ''; // Clear any existing content
    userReviewContainer.appendChild(reviewForm);

}