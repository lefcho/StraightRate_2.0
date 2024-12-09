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
        const reviewElement = document.createElement('div');
        reviewElement.classList.add('review');

        reviewElement.innerHTML = `
            <div class="review-header">
                <p><strong>${review.user}</strong></p>
                <p>${review.rating} <i class="fa fa-star"></i></p>
            </div>
            <p>${review.comment}</p>
        `;
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
