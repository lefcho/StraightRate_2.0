document.addEventListener('DOMContentLoaded', () => {
    const movieId = {{ movie.id }}; // Assume this is passed in context
    const apiBaseUrl = '/api/';
    const userReviewContainer = document.getElementById('user-review-container');
    const reviewsContainer = document.getElementById('reviews-container');
    const averageRatingEl = document.getElementById('average-rating');

    const headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
    };

    // Helper to get CSRF token
    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [key, value] = cookie.trim().split('=');
            if (key === name) return value;
        }
        return null;
    }

    // Fetch and render reviews
    async function fetchReviews() {
        try {
            const response = await fetch(`${apiBaseUrl}reviews/?movie_id=${movieId}`);
            const data = await response.json();
            reviewsContainer.innerHTML = '';
            let totalRating = 0;

            data.forEach(review => {
                const reviewDiv = document.createElement('div');
                reviewDiv.classList.add('review');

                reviewDiv.innerHTML = `
                    <h3 class="review-username">${review.user.username}</h3>
                    <p class="review-rating">Rating: ${review.rating} <i class="fa-solid fa-star"></i></p>
                    <p class="review-comment">${review.comment}</p>
                    <button class="like-btn" data-id="${review.id}">
                        Like (${review.like_count})
                    </button>
                `;

                reviewsContainer.appendChild(reviewDiv);
                totalRating += review.rating;
            });

            // Update average rating
            const averageRating = data.length ? (totalRating / data.length).toFixed(1) : 'Not reviewed yet.';
            averageRatingEl.textContent = averageRating;

            // Attach like handlers
            attachLikeHandlers();
        } catch (error) {
            console.error('Error fetching reviews:', error);
        }
    }

    // Handle like toggling
    async function toggleLike(reviewId) {
        try {
            const response = await fetch(`${apiBaseUrl}reviews/${reviewId}/like/`, {
                method: 'POST',
                headers,
            });

            const data = await response.json();
            fetchReviews(); // Re-fetch reviews to update UI
        } catch (error) {
            console.error('Error toggling like:', error);
        }
    }

    // Attach click handlers for like buttons
    function attachLikeHandlers() {
        const likeButtons = document.querySelectorAll('.like-btn');
        likeButtons.forEach(button => {
            button.addEventListener('click', () => {
                const reviewId = button.dataset.id;
                toggleLike(reviewId);
            });
        });
    }

    // Handle creating/updating user review
    async function saveUserReview(reviewId = null, rating, comment) {
        try {
            const method = reviewId ? 'PUT' : 'POST';
            const url = reviewId
                ? `${apiBaseUrl}reviews/${reviewId}/`
                : `${apiBaseUrl}reviews/`;

            const response = await fetch(url, {
                method,
                headers,
                body: JSON.stringify({
                    movie: movieId,
                    rating,
                    comment,
                }),
            });

            if (response.ok) {
                fetchReviews();
            } else {
                console.error('Error saving review:', response.statusText);
            }
        } catch (error) {
            console.error('Error saving review:', error);
        }
    }

    // Render user's review form
    async function renderUserReview() {
        // Fetch the user's review if exists
        try {
            const response = await fetch(`${apiBaseUrl}reviews/?movie_id=${movieId}`);
            const data = await response.json();
            const userReview = data.find(review => review.user.id === currentUser.id);

            userReviewContainer.innerHTML = `
                <form id="user-review-form">
                    <div class="star-rating">
                        <label for="rating">Rating:</label>
                        <input type="number" id="rating" name="rating" value="${userReview ? userReview.rating : ''}" required min="1" max="5">
                    </div>
                    <textarea id="comment" name="comment" placeholder="Write your review..." required>
                        ${userReview ? userReview.comment : ''}
                    </textarea>
                    <button type="submit" class="btn btn-primary">${userReview ? 'Update' : 'Submit'} Review</button>
                </form>
            `;

            // Attach form submit handler
            const reviewForm = document.getElementById('user-review-form');
            reviewForm.addEventListener('submit', async event => {
                event.preventDefault();
                const rating = document.getElementById('rating').value;
                const comment = document.getElementById('comment').value;
                await saveUserReview(userReview?.id, rating, comment);
            });
        } catch (error) {
            console.error('Error rendering user review:', error);
        }
    }

    // Initialize
    fetchReviews();
    renderUserReview();
});
