// Handle Profile Edit and Cancel

// Store the original values in a variable
let originalValues = {};

// When the "Edit" button is clicked
document.getElementById('edit-profile-btn').addEventListener('click', function() {
    // Enable all input fields
    document.querySelectorAll('.profile-info input').forEach(input => {
        input.disabled = false;

        // Store the original value of each input field
        originalValues[input.name] = input.value;
    });

    // Show the Save and Cancel buttons
    document.getElementById('save-profile-btn').classList.remove('hidden');
    document.getElementById('cancel-edit-btn').classList.remove('hidden');

    // Hide the Edit button
    this.classList.add('hidden');
});

// When the "Cancel" button is clicked
document.getElementById('cancel-edit-btn').addEventListener('click', function() {
    // Reset all input fields to their original values
    document.querySelectorAll('.profile-info input').forEach(input => {
        input.value = originalValues[input.name];
        input.disabled = true;  // Disable the input fields again
    });

    // Hide the Save and Cancel buttons
    document.getElementById('save-profile-btn').classList.add('hidden');
    document.getElementById('cancel-edit-btn').classList.add('hidden');

    // Show the Edit button
    document.getElementById('edit-profile-btn').classList.remove('hidden');
});
