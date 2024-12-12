function toggleReviewForm() {
    const reviewFormContainer = document.getElementById('review-form-container');
    const toggleReviewBtn = document.getElementById('toggle-review');

    if (reviewFormContainer.classList.contains('hidden')) {
        reviewFormContainer.classList.remove('hidden');
        toggleReviewBtn.textContent = 'Cancel';
    } else {
        reviewFormContainer.classList.add('hidden');
        toggleReviewBtn.textContent = 'Leave Review';
    }
}