import {setStarsInteractive} from "./editReviewButtonsHandler.js";

const movieDetails = document.getElementById('movie-data');
const movieId = movieDetails.dataset.movieId;
const userAuthenticated = movieDetails.dataset.userAuth === "true";
const userReviewId = movieDetails.dataset.userReviewId;
const submitButtonElement = document.getElementById('submit-review-button');
const ratingValueElement = document.getElementById('rating-value');
const reviewCommentElement = document.getElementById('review-comment');
const editButtonElement = document.getElementById('edit-review-btn');
const submitEditedButtonElement = document.getElementById('save-review-btn')
const cancelButtonElement = document.getElementById('cancel-review-btn');

document.addEventListener('DOMContentLoaded', () => {
    const hasReviewed = !(userReviewId === "0")

    if (userAuthenticated && !hasReviewed) {
        setStarsInteractive(true);
        submitButtonElement.addEventListener('click', handleReviewFormSubmission);
    } else if (userAuthenticated && hasReviewed) {
        setStarsInteractive(true);
        fetchAndPopulateReview()
        submitEditedButtonElement.addEventListener('click', handleReviewUpdate)
    }

});


function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [key, value] = cookie.trim().split('=');
        if (key === name) return value;
    }
    return null;
}

function handleReviewFormSubmission(event) {

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
            console.log('Review submitted successfully:', data);
            populateFormWithData(ratingValue, comment)
        })
        .catch(error => {
            console.error('Error submitting review:', error);
            alert('There was an error submitting your review.');
        });
}


function fetchAndPopulateReview() {
    const reviewUrl = `/reviews/movie-review/${userReviewId}/`;

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
            const {rating, comment} = data;
            populateFormWithData(rating, comment);
        })
        .catch(error => {
            console.error('Error fetching review data:', error);
            alert('There was an error loading your review.');
        });
}


function handleReviewUpdate(event) {
    event.preventDefault();

    const reviewUrl = `/reviews/movie-review/${userReviewId}/`;

    const updatedRating = ratingValueElement.value;
    const updatedComment = reviewCommentElement.value;

    const updatedReviewData = {
        rating: updatedRating,
        comment: updatedComment,
        movie: movieId,
    };

    fetch(reviewUrl, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify(updatedReviewData),
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to update review');
            }
        })
        .then(data => {
            // Handle successful update
            console.log('Review updated successfully:', data);
            populateFormWithData(updatedRating, updatedComment);
            submitEditedButtonElement.classList.add('hidden');
            cancelButtonElement.classList.add('hidden');
        })
        .catch(error => {
            console.error('Error updating review:', error);
            alert('There was an error updating your review.');
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

    ratingValueElement.value = score;
    setStarsInteractive(false);

    commentElement.value = comment;
    commentElement.setAttribute('disabled', 'disabled');

    editButtonElement.classList.remove('hidden');
}
