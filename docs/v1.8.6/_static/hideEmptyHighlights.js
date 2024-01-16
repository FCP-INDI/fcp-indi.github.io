/* Hide highlight containers only empty spans */
document.addEventListener("DOMContentLoaded", function() {
  const highlightDivs = document.querySelectorAll('div[class^="highlight"], div[class*=" highlight"]');
  highlightDivs.forEach(function(highlightDiv) {
    if (highlightDiv.textContent.trim() === '') {
      highlightDiv.classList.add('hidden');
    }
  });
});
