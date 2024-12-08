let originalComment = '';
let originalRating = 0;

const commentArea = document.getElementById('review-comment');
const rating = document.getElementById('rating-value');
const editButtonElement = document.getElementById('edit-review-btn');
const cancelButtonElement = document.getElementById('cancel-review-btn');
const submitEditedButtonElement = document.getElementById('save-review-btn')

// Store the original values of the textarea and rating
if (commentArea) {
    originalComment = commentArea.value;
}
if (rating) {
    originalRating = rating.value;
}

// Get star elements
const stars = document.querySelectorAll('.star');

// Function to make stars interactive or not
export function setStarsInteractive(interactive) {
    stars.forEach(star => {
        if (interactive) {
            star.classList.remove('disabled');
            star.addEventListener('click', handleStarClick);
            star.addEventListener('mouseover', handleStarHover);
            star.addEventListener('mouseout', handleStarMouseOut);
        } else {
            star.classList.add('disabled');
            star.removeEventListener('click', handleStarClick);
            star.removeEventListener('mouseover', handleStarHover);
            star.removeEventListener('mouseout', handleStarMouseOut);
        }
    });
}

// Handle star hover
function handleStarHover() {
    resetStars();
    highlightStars(this.getAttribute('data-value'));
}

// Handle star mouse out
function handleStarMouseOut() {
    resetStars();
    highlightStars(rating.value);
}

// Handle star click
function handleStarClick() {
    const selectedRating = this.getAttribute('data-value');
    rating.value = selectedRating; // Update the hidden rating input field
    highlightStars(selectedRating);

}

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

// When the "Edit" button is clicked
editButtonElement.addEventListener('click', function () {
    originalRating = rating.value;
    originalComment = commentArea.value;

    // Enable the textarea
    if (commentArea) {
        commentArea.disabled = false;
    }

    // Show the Save and Cancel buttons
    submitEditedButtonElement.classList.remove('hidden');
    cancelButtonElement.classList.remove('hidden');

    // Hide the Edit button
    this.classList.add('hidden');

    // Make stars interactive
    setStarsInteractive(true);
});

// When the "Cancel" button is clicked
cancelButtonElement.addEventListener('click', function () {
    // Reset the textarea to its original value
    if (commentArea) {
        commentArea.value = originalComment;
        commentArea.disabled = true;
    }

    // Reset the stars to their original state
    resetStars();
    highlightStars(originalRating);

    // Reset the rating to the original value
    rating.value = originalRating;

    // Hide the Save and Cancel buttons
    submitEditedButtonElement.classList.add('hidden');
    cancelButtonElement.classList.add('hidden');

    // Show the Edit button
    editButtonElement.classList.remove('hidden');

    // Make stars non-interactive
    setStarsInteractive(false);
});


// Initialize stars as non-interactive
setStarsInteractive(false);

// Highlight the stars based on the initial rating value
highlightStars(rating.value);
