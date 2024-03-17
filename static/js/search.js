// Function to generate HTML for each search result
function generateSearchResultHTML(
  jobId,
  logo,
  title,
  location,
  employmentType,
  salaryRange
) {
  return `
      <div class="search-result">
          <img src="${logo}" alt="Company Logo" class="company-logo">
          <div class="job-details">
              <h3 class="job-title">${title}</h3>
              <p class="location">${location}</p>
              <p class="employment-type">${employmentType}</p>
              <p class="salary">${salaryRange}</p>
              <a href="/app/job-detail/${jobId}" class="btn btn-primary">View Details</a>
          </div>
      </div>
  `;
}

// Function to render search results into the search container
function renderSearchResults(searchResults) {
  const searchcontainer = document.getElementById("searchcontainer");
  searchcontainer.innerHTML = ""; // Clear existing content

  searchResults.forEach((result) => {
    const resultHTML = generateSearchResultHTML(
      result.id,
      result.logo,
      result.title,
      result.location,
      result.employmentType,
      result.salaryRange
    );
    searchcontainer.innerHTML += resultHTML;
  });
}

// Assuming you have received search results data in a variable named 'searchResults'
// Call the function to render search results into the search container
renderSearchResults(searchResults);

// Function to fetch job title suggestions from the server
function fetchJobTitleSuggestions(searchTerm) {
  $.ajax({
    url: "/api/job-titles",
    method: "GET",
    data: { search: searchTerm },
    success: function (data) {
      displayJobTitleSuggestions(data);
    },
    error: function (error) {
      console.error("Error fetching job title suggestions:", error);
    },
  });
}

// Function to display job title suggestions in the suggestions container
function displayJobTitleSuggestions(suggestions) {
  const suggestionsContainer = $("#suggestionsContainer");
  suggestionsContainer.empty();

  suggestions.forEach(function (suggestion) {
    const suggestionElement = $(
      '<div class="suggestion">' + suggestion.title + "</div>"
    );
    suggestionElement.on("click", function () {
      $("#searchInput").val(suggestion.title);
      suggestionsContainer.empty();
    });
    suggestionsContainer.append(suggestionElement);
  });
}

// Event listener for keyup event on the search input field
$("#searchInput").on("keyup", function () {
  const searchTerm = $(this).val().trim();
  if (searchTerm.length >= 2) {
    fetchJobTitleSuggestions(searchTerm);
  } else {
    $("#suggestionsContainer").empty();
  }
});

// AJAX request to fetch search results
$.ajax({
  url: "/app/api/jobs", // Update the URL to match the endpoint for fetching search results
  method: "GET", // Set the method to GET since you're fetching data
  data: { search: searchTerm }, // Include any search parameters if needed
  success: function (data) {
    console.log(data);
    // Once you receive the search results data, you can render it into the search container
    renderSearchResults(data);
  },
  error: function (error) {
    console.error("Error fetching search results:", error);
  },
});
