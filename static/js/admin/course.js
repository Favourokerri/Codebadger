search_input = document.getElementById("search_bar");
suggestions = document.getElementById("search_suggestions");

document.addEventListener('DOMContentLoaded', function(){
    const publishedLink = document.getElementById('publishedLink');
    const draftLink = document.getElementById('draftLink');

    function handelStatusClick(event){
        publishedLink.classList.remove('status-active');
        draftLink.classList.remove('status-active');
    }

    const currentLocation = window.location.href;
    if (currentLocation.includes('publishedCourse')){
        publishedLink.classList.add('status-active')
    } 

    else if (currentLocation.includes('draftCourse')){
        draftLink.classList.add('status-active')
    }

    publishedLink.addEventListener('click', handelStatusClick);
    draftLink.addEventListener('click', handelStatusClick);

})

function searchSuggestion(e) {
    if (e.target.value.length !== 0) {
        suggestions.style.display = "block";
        fetch(`searchCourse?q=${e.target.value}`, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'  // Set the header to identify this as an AJAX request
            }
        })
        .then(response => response.json())
        .then(data => {
            const item = document.createElement('li')
            suggestions.innerHTML = '';

            if (data.result.length === 0) {
                item.textContent = 'No results found';  // Message for no results
                console.log("hey")
                suggestions.appendChild(item);
            } else {       
                const limitedResults = data.result.slice(0, 7);

                limitedResults.forEach(result => {
                    const item = document.createElement('li')
                    const link = document.createElement('a');    
                    link.href = `course/${result.id}/`;
                    link.textContent = result.name; 
                    item.appendChild(link);
                    suggestions.appendChild(item);
            })
         }
        })
            .catch(error => {
                console.error('Error:', error);  // Handle any error that occurs
            });
    } else {
        suggestions.style.display = "none";
    }
}
