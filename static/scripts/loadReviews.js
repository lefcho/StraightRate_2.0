function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [key, value] = cookie.trim().split('=');
        if (key === name) return value;
    }
    return null;
}


const mediaDataElement = document.getElementById('media-data');
const mediaId = mediaDataElement.dataset.mediaId;
const mediaType = mediaDataElement.dataset.mediaType;
const isMovie = (mediaType === "movie");
const reviewsContainer = document.getElementById('reviews-container');
const loadingIndicator = document.getElementById('loading-indicator');
const userAuthenticated = mediaDataElement.dataset.userAuth === "true";

document.addEventListener('DOMContentLoaded', () => {
    let currentPage = 1;
    let isFetching = false;

    function fetchReviews() {
        if (isFetching) return;

        isFetching = true;
        loadingIndicator.style.display = 'block';

        let get_reviews_url;

        if (isMovie) {
            get_reviews_url = `/reviews/movie-reviews/${mediaId}/?page=${currentPage}`;
        } else {
            get_reviews_url = `/reviews/game-reviews/${mediaId}/?page=${currentPage}`
        }

        fetch(get_reviews_url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => {
                if (response.ok) return response.json();
                throw new Error('Failed to load reviews');
            })
            .then(data => {
                const reviews = data.results;
                reviews.forEach(review => appendReview(review));
                if (data.next) {
                    currentPage += 1;
                } else {
                    window.removeEventListener('scroll', handleScroll);
                }
            })
            .catch(error => {
                console.error('Error fetching reviews:', error);
            })
            .finally(() => {
                isFetching = false;
                loadingIndicator.style.display = 'none';
            });
    }

    function appendReview(review) {
        // Create the main review container
        const reviewElement = document.createElement('div');
        reviewElement.classList.add('review');

        // Create the top container
        const topDiv = document.createElement('div');
        topDiv.classList.add('review-top-div');

        // Add username
        const usernameElement = document.createElement('h3');
        usernameElement.classList.add('review-username');
        usernameElement.textContent = review.user;
        topDiv.appendChild(usernameElement);

        // Create the like container
        const likeDiv = document.createElement('div');
        likeDiv.classList.add('like-div');
        likeDiv.addEventListener('click', () => {
            if (userAuthenticated) {
                handleLike(review.id, likeCountElement, heartIcon);
            } else {
                const currentUrl = window.location.pathname + window.location.search;
                window.location.href = `/accounts/login/?next=${encodeURIComponent(currentUrl)}`;
            }
        });


        // Like count
        const likeCountElement = document.createElement('p');
        likeCountElement.classList.add('like-count');
        likeCountElement.textContent = review.like_count;
        likeDiv.appendChild(likeCountElement);

        // Heart icon
        const heartIcon = document.createElement('i');
        if (review.liked) {
            heartIcon.classList.add('fa-solid', 'fa-heart');
        } else {
            heartIcon.classList.add('fa-regular', 'fa-heart');
        }
        likeDiv.appendChild(heartIcon);

        topDiv.appendChild(likeDiv);
        reviewElement.appendChild(topDiv);

        // Add rating
        const ratingElement = document.createElement('p');
        ratingElement.classList.add('review-rating');
        const ratingText = document.createTextNode(`Rating: ${review.rating} `);
        ratingElement.appendChild(ratingText);

        const starIcon = document.createElement('i');
        starIcon.classList.add('fa-solid', 'fa-star');
        starIcon.setAttribute('aria-hidden', 'true');
        ratingElement.appendChild(starIcon);

        reviewElement.appendChild(ratingElement);

        // Add comment
        const commentElement = document.createElement('p');
        commentElement.classList.add('review-comment');
        commentElement.textContent = review.comment;
        reviewElement.appendChild(commentElement);

        // Append to container
        reviewsContainer.appendChild(reviewElement);
    }

    function handleLike(reviewId, likeCountElement, heartIcon) {

        let like_url;

        if (isMovie) {
            like_url = `/reviews/like/movie-review/${reviewId}/`;
        } else {
            like_url = `/reviews/like/game-review/${reviewId}/`;
        }

        fetch(like_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
            .then(response => response.json())
            .then(data => {

                if (data.liked) {
                    heartIcon.classList.remove('fa-regular');
                    heartIcon.classList.add('fa-solid');
                } else {
                    heartIcon.classList.remove('fa-solid');
                    heartIcon.classList.add('fa-regular');
                }

                likeCountElement.textContent = data.like_count;
            })
            .catch(error => {
                console.error('Error liking the review:', error);
            });
    }

    function handleScroll() {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 50) {
            fetchReviews();
        }
    }

    window.addEventListener('scroll', handleScroll);

    fetchReviews();
});
