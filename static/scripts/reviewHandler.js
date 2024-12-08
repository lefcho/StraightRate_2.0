import {setStarsInteractive} from "./editReviewButtonsHandler.js";

const movieDetails = document.getElementById('movie-data');
const movieId = movieDetails.dataset.movieId;
const userAuthenticated = movieDetails.dataset.userAuth === "true";
const submitButtonElement = document.getElementById('submit-review-button');
// const userReviewContainer = document.getElementById('user-review-container');
const editButtonElement = document.getElementById('edit-review-btn');


document.addEventListener('DOMContentLoaded', () => {

    if (userAuthenticated) {
        setStarsInteractive(true);
        submitButtonElement.addEventListener('click', handleReviewFormSubmission);
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
            populateFormWithData(ratingValue, comment)
            alert('Your review has been submitted!');
        })
        .catch(error => {
            console.error('Error submitting review:', error);
            alert('There was an error submitting your review.');
        });
}


function populateFormWithData(score, comment) {
    const starElements = document.querySelectorAll('.star');
    const commentElement = document.getElementById('review-comment');

    submitButtonElement.classList.add('hidden');
    submitButtonElement.setAttribute('disabled', 'disabled');

    for (let i = 0; i < score; i++) {
        starElements[i].classList.add('filled');
    }
    setStarsInteractive(false);

    commentElement.value = comment;
    commentElement.setAttribute('disabled', 'disabled');

    editButtonElement.classList.remove('hidden');
}
