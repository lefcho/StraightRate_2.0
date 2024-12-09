document.addEventListener('DOMContentLoaded', () => {
    let currentPage = 1;
    const mediaDataElement = document.getElementById('media-data');
    const mediaId = mediaDataElement.dataset.mediaId;
    const reviewsContainer = document.getElementById('reviews-container');
    const loadingIndicator = document.getElementById('loading-indicator');
    let isFetching = false;

    function fetchReviews() {
        if (isFetching) return;

        isFetching = true;
        loadingIndicator.style.display = 'block';

        fetch(`/reviews/movie-reviews/${mediaId}/?page=${currentPage}`, {
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

    // Like count
    const likeCountElement = document.createElement('p');
    likeCountElement.classList.add('like-count');
    likeCountElement.textContent = review.like_count;
    likeDiv.appendChild(likeCountElement);

    // Heart icon
    const heartIcon = document.createElement('i');
    heartIcon.classList.add('fa-regular', 'fa-heart');
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


    function handleScroll() {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 50) {
            fetchReviews();
        }
    }

    window.addEventListener('scroll', handleScroll);

    fetchReviews();
});
