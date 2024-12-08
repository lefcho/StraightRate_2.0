import {setStarsInteractive} from "./editReviewButtonsHandler.js";

const movieDetails = document.getElementById('movie-data');
const movieId = movieDetails.dataset.movieId;
const userAuthenticated = movieDetails.dataset.userAuth === "true";
const userReviewId = movieDetails.dataset.userReviewId;
const submitButtonElement = document.getElementById('submit-review-button');
const ratingValueElement = document.getElementById('rating-value');
const reviewCommentElement = document.getElementById('review-comment');
const editButtonElement = document.getElementById('edit-review-btn');


document.addEventListener('DOMContentLoaded', () => {
    const hasReviewed = !(userReviewId === "0")

    if (userAuthenticated && !hasReviewed) {
        setStarsInteractive(true);
        submitButtonElement.addEventListener('click', handleReviewFormSubmission);
    } else if (userAuthenticated && hasReviewed) {
        fetchAndPopulateReview()
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

    const ratingValue = ratingValueElement.value;
    const comment = reviewCommentElement.value;

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


function fetchAndPopulateReview() {
    const reviewUrl = `/reviews/${userReviewId}/`; // Construct the URL for the GET request

    fetch(reviewUrl, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to fetch review data');
            }
        })
        .then(data => {
            const { rating, comment } = data;
            populateFormWithData(rating, comment);
        })
        .catch(error => {
            console.error('Error fetching review data:', error);
            alert('There was an error loading your review.');
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
